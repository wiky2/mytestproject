#!/usr/bin/env python
# coding: utf-8

stocks = { 'APPL': 201,'GOOG': 800, 'Fox': 54,'MSFT': 313, 'TUNA': 68}
min_price=min(zip(stocks.values(),stocks.keys()))
print min_price
