#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BPNote Liteのデータ(excel)をJSON/Databaseにコンバートするクラス
"""
__author__ = 'Shinichi Nakagawa'


import os
import shutil
import xlrd
import json


class BpNoteExcelToJson(object):

    FILE_EXT = '.csv'
    INPUT_EXTS = (
        '.xlsx'
    )
    OUTPUT_EXT = '.json'
    ENCODING = 'utf-8'

    def __init__(self, path='', output_path=''):
        # パスとか設定
        self.path = path
        self.data_files = os.listdir(self.path)
        self.output_path = output_path

    def run(self):
        """
        実行
        """

        # 出力先を削除&生成
        if os.path.exists(self.output_path):
            shutil.rmtree(self.output_path)
        os.mkdir(self.output_path)

        for data_file in self.data_files:
            # JSONにDump
            self._dump_json(data_file)

    def _dump_json(self, data_file):
        """
        ファイルを読み込んでJSONにダンプ
        """
        root, ext = os.path.splitext(data_file)
        # 指定拡張子以外は読まない
        if ext in BpNoteExcelToJson.INPUT_EXTS:
            print(data_file)
        else:
            return

    def _get_obj(self, header, row):
        """
        Headerと本文をchunk
        """
        pass

    def _get_output_filename(self, root):
        """
        Output File
        """
        # root名+拡張子
        return os.path.join(self.output_path, "".join([root, self.OUTPUT_EXT]))


def main(args):
    """

    :param args: scriptオプション
    """
    lh = BpNoteExcelToJson(path=args.input, output_path=args.output)
    lh.run()


import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='BPNote Lite data converter.')
    parser.add_argument(
        '-i',
        '--input',
        required=True,
        help='BPNote Lite Excel data directory path.'
    )
    parser.add_argument(
        '-o',
        '--output',
        required=True,
        help='Output data directory path.'
    )
    args = parser.parse_args()
    main(args)
