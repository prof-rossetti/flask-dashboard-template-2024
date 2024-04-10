

import os
from dotenv import load_dotenv
from pandas import read_csv, DataFrame


load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def to_usd(my_price):
    """
        Converts a numeric value to usd-formatted string, for printing and display purposes.

        Param: my_price (int or float) like 4000.444444

        Example: to_usd(4000.444444)

        Returns: $4,000.44
    """
    return f"${my_price:,.2f}"


class AlphavantageService:

    def __init__(self, api_key=ALPHAVANTAGE_API_KEY):
        self.api_key = api_key

    def fetch_stocks_daily(self, symbol="MSFT"):
        """
            Fetches stock data for the given symbol.
            Returns the data, or an empty DataFrame if none is available.
        """
        request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={self.api_key}&datatype=csv"
        df = read_csv(request_url) #> pandas.DataFrame
        if "timestamp" not in df.columns:
            # sometimes we might not get the data
            # ... when using the demo key or
            # ... when hitting rate limits,
            # ... or when supplying invalid symbols
            return DataFrame()
        else:
            return df




if __name__ == "__main__":

    alpha = AlphavantageService()

    symbol = input("Please input a stock symbol: ")
    print(symbol)

    stocks_df = alpha.fetch_stocks_daily(symbol=symbol)
    if stocks_df.empty:
        print("OOPS, something went wrong. Please check your inputs and try again...")
    else:
        print(stocks_df.head())

        print("-----------------")
        print("LATEST DATA:")
        latest = stocks_df.iloc[0] # get the first row in the dataset
        print(latest["timestamp"])
        print(to_usd(latest["close"]))
