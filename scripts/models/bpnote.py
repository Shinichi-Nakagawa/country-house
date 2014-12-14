#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


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
    COLUMN_EVENING_BPS = 'morning_bp_s'
    # 拡張期血圧(夜)
    COLUMN_EVENING_BPD = 'morning_bp_d'
    # 脈拍(夜)
    COLUMN_EVENING_HR = 'morning_hr'
    # 体重
    COLUMN_WEIGHT = 'weight'
    # 服薬してるか否か
    COLUMN_INGESTION = 'ingestion'
    # メモ
    COLUMN_MEMO = 'memo'

    # EXCEL上のCOLUMN位置
    SHEET_COLUMNS = {
        COLUMN_DATE: 0,
        COLUMN_MORNING_TIME: 1,
        COLUMN_MORNING_BPS: 2,
        COLUMN_MORNING_BPD: 3,
        COLUMN_MORNING_HR: 4,
        COLUMN_EVENING_TIME: 5,
        COLUMN_EVENING_BPS: 6,
        COLUMN_EVENING_BPD: 7,
        COLUMN_EVENING_HR: 8,
        COLUMN_WEIGHT: 9,
        COLUMN_INGESTION: 10,
        COLUMN_MEMO: 11,
    }

    def __init__(self):
        self.row = {}

    def set_excel_row(self, row):
        """
        Excel行データから値をセット
        :param row:Excel行データ(list)
        """
        for k, v in self.SHEET_COLUMNS.items():
            self.row[k] = row[v].value
