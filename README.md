# getquote

![GitHub](https://img.shields.io/github/license/jeanralphaviles/getquote)
[![PyPI](https://img.shields.io/pypi/v/getquote)](https://pypi.org/project/getquote/)

A [ledger-cli](https://www.ledger-cli.org) getquote implementation using the
free [IEX Cloud API](https://iexcloud.io/).

## Setup

1. Create a free [IEX Cloud API account](https://iexcloud.io/).
1. Verify your account and generate API tokens.
1. Install `getquote`:

    ```bash
    pip3 install getquote --prefix /usr/local
    ```

1. Create a `getquote.ini` config file in your ledger directory.

    ```ini
    [IEX]
    TOKEN = <your publishable IEX API token here>
    ```

    * Alternatively, set the `IEX_TOKEN` environment variable.

    ```bash
    export IEX_TOKEN=pk_deadbeefdeadbeefdeadbeefdeadbeef
    ```

1. Test

    ```bash
    $ getquote GOOG
    2020/08/30 09:56:54-0400 GOOG $1644.41
    ```

## Maintenance

### Uploading new packages to PyPi

```bash
pip install twine
./setup.py sdist
twine upload dist/getquote-*.tar.gz
```

## Author

[Jean-Ralph (JR) Aviles](https://jr.expert)
