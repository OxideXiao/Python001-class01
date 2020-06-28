# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline:
     def process_item(self, item, spider):
        name = item['name']
        classic = item['classic']
        date = item['date']
        output = f'|{name}|\t|{classic}|\t|{date}|\n\n'
        with open('./movieFile_scp.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
