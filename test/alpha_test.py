

from pandas import DataFrame

from app.alpha import to_usd, AlphavantageService


def test_usd_formatting():
    assert to_usd(123456789.5) == '$123,456,789.50'


def test_fetch_stocks_daily():
    service = AlphavantageService()

    # with valid symbol, returns the data:
    df = service.fetch_stocks_daily(symbol="GOOGL")
    assert isinstance(df, DataFrame)
    assert not df.empty
    assert df.columns.tolist() == ['timestamp', 'open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient']
    assert len(df) >= 100

    # with invalid symbol, returns empty DataFrame:
    df = service.fetch_stocks_daily(symbol="OOPS")
    assert isinstance(df, DataFrame)
    assert df.empty
