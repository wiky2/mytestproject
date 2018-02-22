#!/usr/bin/env python
# coding: utf-8
income = [10, 30, 75]


def double_money(dollars):
    return dollars*2
#把一个迭代变量放入一个函数。
new_income=list(map(double_money, income))
print new_income
