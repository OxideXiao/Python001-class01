# -*- coding: utf-8 -*-
import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector

class MaoyanmSpider(scrapy.Spider):
    name = 'maoyanM'
    allowed_domains = ['m.maoyan.com']
    start_urls = ['https://m.maoyan.com/?showType=3&sortId=2#movie/classic']
    
    # def parse(self, response):
    #    pass

    def start_requests(self):
        url = f'https://m.maoyan.com/ajax/moreClassicList?sortId=1&showType=3&limit=10&offset=0&optimus_uuid=08611400B95511EA97E61368F9F12EB0B674A282971E456585A998518150437C&optimus_risk_level=71&optimus_code=10'
        # url = 'http://httpbin.org/ip'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        infos = Selector(response=response).xpath('//div[@class="classic-movie"]')
    
        for info in infos:
            item = MaoyanItem()

            name = info.css('.title').xpath('./text()').extract_first()
            classic = info.css('.actors').xpath('./text()').extract_first()
            date = info.css('.show-info').xpath('./text()').extract_first()
            #print(name, classic, date)
            item['name'] = name
            item['classic'] = classic
            item['date'] = date
            yield item

        