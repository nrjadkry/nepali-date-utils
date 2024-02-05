# Nepali Date Utils

[![PyPI version](https://badge.fury.io/py/nepali-date-utils.svg)](https://pypi.org/project/nepali-date-utils/)
[![CI status](https://github.com/nrjadkry/nepali-date-utils/actions/workflows/python-publish.yml/badge.svg?branch=master)](https://github.com/opensource-nepal/py-nepali/actions)
[![Downloads](https://img.shields.io/pypi/dm/nepali.svg?maxAge=180)](https://pypi.org/project/nepali-date-utils/)


## Overview
This lightweight package allows easy conversion between Nepali (BS) and English (AD) dates. Simplify date transformations in your applications with this straightforward utility.

## Installation
You can install the package via pip:
```bash
pip install nepali_date_utils
```

To convert English date (AD) to Nepali date (BS):

```python
from nepali-date-utils import converter
converter.ad_to_bs("2024/02/03")
```

To convert Nepali date (BS) to English date (AD):

```python
from nepali_date_utils import converter
converter.bs_to_ad("2080/02/03")
```
