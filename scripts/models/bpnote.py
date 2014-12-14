#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'

from datetime import datetime


class BpNote(object):
    """
    BPNote Lite Excel モデル
    """
    # 計測日
    COLUMN_DATE = 'date'
    # 計測時間(朝)
    COLUMN_MORNING_TIME = 'morning_time'
    # 収縮期血圧(朝)
    COLUMN_MORNING_BPS = 'morning_bp_s'
    # 拡張期血圧(朝)
    COLUMN_MORNING_BPD = 'morning_bp_d'
    # 脈拍(朝)
    COLUMN_MORNING_HR = 'morning_hr'
    # 計測時間(夜)
    COLUMN_EVENING_TIME = 'evening_time'
    # 収縮期血圧(夜)
    COLUMN_EVENING_BPS = 'evening_bp_s'
    # 拡張期血圧(夜)
    COLUMN_EVENING_BPD = 'evening_bp_d'
    # 脈拍(夜)
    COLUMN_EVENING_HR = 'evening_hr'
    # 体重
    COLUMN_WEIGHT = 'weight'
    # 服薬してるか否か
    COLUMN_INGESTION = 'ingestion'
    # メモ
    COLUMN_MEMO = 'memo'

    # 服薬フラグ
    INGESTION_FLGS = {
        '有': True,
        '無': False
    }

    def __init__(self, excel_class, datemode):
        self.excel = excel_class
        self.datemode = datemode
        self.row = {}

    def set_excel_row(self, row):
        """
        Excel行データから値をセット
        :param row:Excel行データ(list)
        """
        self.row = {
            self.COLUMN_DATE: self.excel.date(row[0].value, self.datemode),
            self.COLUMN_MORNING_TIME: self.excel.date(row[1].value, self.datemode),
            self.COLUMN_MORNING_BPS: row[2].value,
            self.COLUMN_MORNING_BPD: row[3].value,
            self.COLUMN_MORNING_HR: row[4].value,
            self.COLUMN_EVENING_TIME: self.excel.date(row[5].value, self.datemode),
            self.COLUMN_EVENING_BPS: row[6].value,
            self.COLUMN_EVENING_BPD: row[7].value,
            self.COLUMN_EVENING_HR: row[8].value,
            self.COLUMN_WEIGHT: row[9].value,
            self.COLUMN_INGESTION: self.INGESTION_FLGS.get(row[10].value, False),
            self.COLUMN_MEMO: row[11].value,
        }
