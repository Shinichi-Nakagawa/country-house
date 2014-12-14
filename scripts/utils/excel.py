#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


import xlrd


class Excel(object):

    @classmethod
    def book(cls, filename):
        """
        Excel book取得
        :param filename: Excel file name
        :return: excel book
        """
        return xlrd.open_workbook(filename)

    @classmethod
    def sheets(cls, book):
        """
        Excel sheets取得
        :param book: excel book
        :return: excel sheets
        """
        return book.sheets()

    @classmethod
    def get_rows(cls, filename):
        """
        ファイル内の全sheets全行を取得
        :param filename:
        :param filename: Excel file name
        """
        return Excel.sheets(Excel.book(filename))

    @classmethod
    def date(cls, value, datemode):
        """
        xldateを日付に変換
        :param value: Cell value
        :param datemode: Excel book datemode
        :return: tuple(yyyy, mm, dd)
        """
        if isinstance(value, float):
            # 24:00以降のケースもあるので調整
            if value >= 1:
                _value = value - 1
            else:
                _value = value
            return xlrd.xldate_as_tuple(_value, datemode)
        else:
            value