import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # Ensure prices are sorted by ticker and date
    prices = prices.sort_values(by=['ticker', 'date'])
    
    # Calculate log returns
    prices['log_return'] = prices.groupby('ticker')['price'].apply(lambda x: np.log(x / x.shift(1)))
    
    # Calculate standard deviation of log returns for each ticker
    volatility = prices.groupby('ticker')['log_return'].std()
    
    # Get the ticker with the highest standard deviation of log returns
    most_volatile_ticker = volatility.idxmax()
    
    return most_volatile_ticker

def test_run(filename='data/prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()
