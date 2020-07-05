# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from maoyan.lib.mySql import ConnDB

class MaoyanPipeline:
    def process_item(self, item, spider):
        data = dict(name=item['name'],classic=item['classic'],date=item['date']) 

        db = ConnDB()
        db.insertData(data)
        
        return item
