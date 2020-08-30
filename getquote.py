#!/usr/bin/python3
"""getquote script for ledger-cli."""

import configparser
import os
import sys
from urllib import error
from urllib import request
from datetime import datetime

cfg = configparser.ConfigParser()
cfg.read('getquote.ini')
IEX_TOKEN = os.getenv('IEX_TOKEN') or cfg.get('IEX', 'TOKEN')

def quote(symbol: str) -> int:
    """Returns the current price of a security.

    Args:
        symbol: security to quote.
    Returns:
        Price of the security.
    """
    url = f'https://cloud.iexapis.com/stable/stock/{symbol}/quote/latestPrice?token={IEX_TOKEN}'
    try:
        with request.urlopen(url) as resp:
            return resp.read().decode('utf-8')
    except error.HTTPError as exp:
        raise LookupError(f'Unable to quote "{symbol}"') from exp

def ledger_format(symbol: str) -> str:
    """Returns a quote formated for ledger-cli.

    Args:
      symbol: security to quote.
    Returns:
      Ledger-Cli Price db entry for the quote.
    """
    date = datetime.now().astimezone().strftime('%Y/%m/%d %H:%M:%S%z')
    price = quote(symbol)
    return f'{date} {symbol} ${price}'

def main():
    """Entrypoint for getquote."""
    symbol = sys.argv[1]
    print(ledger_format(symbol))

if __name__ == '__main__':
    main()
