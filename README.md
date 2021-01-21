# calam-voyager
Python package for interacting with Yardi Voyager.

## Installation
Download from github and install an editable version:
```
# download repository from github
git clone https://github.com/benr-calam/calam-voyager
cd calam-voyager

# create your development environment with venv first
python3 -m venv venv

# activate the virtual environment
# Windows
.\venv\Scripts\activate

# Mac and Linux
source venv/bin/activate

# Install requirements
pip install -e .
```

Or pip install master branch:
```
pip install git+https://github.com/benr-calam/calam-voyager@master
```

Or specific version once those are released:
```
pip install git+https://github.com/benr-calam/calam-voyager@v1.0
```

## Overview
Package consists of a set of functions that execute HTTP requests against either an `aiohttp.ClientSession` for the asynchronous parts of the package or a `requests.Session` for the blocking parts.

### Core Functionalities (so far)
- Logging into voyager
- Pull a report by name with parameters

## Testing
This package uses the `unittest` framework to run tests while also supplying a few utilities to allow for easily running async code in tests.

It is recommended to create a separate testing virtual environment named `testing-venv` in which to install `testing_requirements.txt` and run tests.

```
# create your testing environment with venv first
python3 -m venv testing-venv

# activate the virtual environment (see above)
...

# install requirements
pip install -r testing_requirements.txt

# run tests
python -m unittest tests/*
```

## Best Practices
- Add type-hints to the code you write.
- Document the code you write.
- Test the code you write.
- Don't push to master; review each others' code.
- Write examples.
- Write code for both async and blocking calls.
- Use constants and enums instead of string literals. Keep them in `calam_voyager/base.py`.
- Keep functions small; write a function to only GET/POST data from/to a page, not to parse it (e.g. with pandas).
- Keep all async code in the top-level package while any blocking functions in the blocking sub-package.
- Pass a cookie jar to `aiohttp.ClientSession` that does not quote cookies. This will save a word of hurt.
```python
jar = aiohttp.CookieJar(quote_cookie=False)
async with aiohttp.ClientSession(cookie_jar=jar) as s:
    ...
```