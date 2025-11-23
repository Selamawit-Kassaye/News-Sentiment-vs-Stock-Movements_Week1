# src/quant_analysis.py

import pandas as pd
import talib

def load_stock_data(filepath: str) -> pd.DataFrame:
    """
    Load stock price data from CSV into a pandas DataFrame.

    Expected columns: Date, Open, High, Low, Close, Volume
    Converts 'Date' to datetime and sets it as index.

    Parameters
    ----------
    filepath : str
        Path to CSV file containing stock price data.

    Returns
    -------
    pd.DataFrame
        Stock price dataframe with datetime index.
    """
    df = pd.read_csv(filepath)
    df.columns = [col.strip().capitalize() for col in df.columns]  # standardize column names

    # Ensure required columns exist
    required_cols = {'Date', 'Open', 'High', 'Low', 'Close', 'Volume'}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Convert Date to datetime and set as index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    return df


def apply_talib_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply common TA-Lib indicators: SMA, EMA, RSI, MACD.

    Parameters
    ----------
    df : pd.DataFrame
        Stock price dataframe with columns Open, High, Low, Close, Volume

    Returns
    -------
    pd.DataFrame
        DataFrame with new columns for indicators.
    """
    # Moving Averages
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['EMA_20'] = talib.EMA(df['Close'], timeperiod=20)
    df['EMA_50'] = talib.EMA(df['Close'], timeperiod=50)

    # RSI
    df['RSI_14'] = talib.RSI(df['Close'], timeperiod=14)

    # MACD
    macd, macdsignal, macdhist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['MACD'] = macd
    df['MACD_signal'] = macdsignal
    df['MACD_hist'] = macdhist

    return df
