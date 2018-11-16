import time

import scrapy
from scrapy import Request

from scrapy_test.scrapy_test.items import ScrapyItemName


class BookSpider(scrapy.Spider):
    name = 'Intresting_name'
    allowed_domains = ['613ww.com']
    start_urls = ['https://www.613ww.com/Html/84/index-2.html']

    def parse(self, response):
        try:
            for item in response.xpath('//div[@class="box list channel"]/ul//a[@target="_blank"]'):
                name = item.xpath('text()').extract()[0]
                link = item.xpath('@href').extract()[0]
                yield Request('https://www.613ww.com' + link,
                              meta={'name': name},
                              callback=self.parse_book)

        except IndexError:
            pass
        link = response.xpath('//div[@class="pagination"]/a[@class="next pagegbk"]')
        if link is not None:
            # /html/body/div[15]/div/div[2]/a[7]
            link = link[0].xpath('@href').extract()[0]
            yield scrapy.Request('https://www.613ww.com' + link, callback=self.parse)

    def parse_book(self, response):
        try:
            item = ScrapyItemName()
            item['name'] = response.meta['name'].replace(' ', '')
            item['content'] = response.xpath('//div[@class="content"]/font/text()').extract()[0]
            yield item
        except IndexError:
            pass
