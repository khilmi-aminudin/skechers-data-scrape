# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import pandas as pd
from itemadapter import ItemAdapter
from collections import defaultdict
from openpyxl import load_workbook


class SkechersPipeline:
    def process_item(self, item, spider):
        return item


class ExcelMultiSheetPipeline:
    def __init__(self):
        self.data_per_spider = {}
        self.file_path = "output.xlsx"

    def process_item(self, item, spider):
        if spider.name not in self.data_per_spider:
            self.data_per_spider[spider.name] = []
        self.data_per_spider[spider.name].append(dict(item))
        return item

    def close_spider(self, spider):
        data = self.data_per_spider.get(spider.name, [])
        if not data:
            return

        df = pd.DataFrame(data)
        sheet_name = spider.name[:31]  # Excel sheet name limit is 31 characters
        # sheet_name = self._get_unique_sheet_name(spider.name[:31]

        if self._file_exists(self.file_path):
            with pd.ExcelWriter(
                self.file_path, engine="openpyxl", mode="a", if_sheet_exists="new"
            ) as writer:
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        else:
            with pd.ExcelWriter(self.file_path, engine="openpyxl", mode="w") as writer:
                df.to_excel(writer, sheet_name=sheet_name, index=False)

    def _file_exists(self, file_path):
        try:
            if not os.path.isfile(file_path):
                return False
            load_workbook(file_path)
            return True
        except Exception:
            return False
