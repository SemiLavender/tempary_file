import scrapy
from scrapy import Request

from scrapy_test.items import ScrapyItemName


class BookSpider(scrapy.Spider):
    name = 'Intresting_name'
    allowed_domains = ['']
    start_urls = ['']

    def parse(self, response):

        yield scrapy.Request(response.url, callback=self.parse_page)

        for page in response.xpath('//div[@class="pagination"]/a'):
            link = page.xpath('@href').extract()[0]
            print(''+link)
            yield Request(url=''+link, callback=self.parse_page)

    def parse_page(self, response):
        for item in response.xpath('/html/body/div[15]/div/ul'):
            book = ScrapyItemName()
            # /html/body/div[15]/div/ul/li[1]/a/text()
            book.name = item.xpath('a/text()').extract()[0]
            # /html/body/div[15]/div/ul/li[1]/a
            yield Request(item.xpath('a/@href'),
                          meta={'item': item},
                          callback=self.parse_book,
                          dont_filter=True)

    @staticmethod
    def parse_book(response):
        item = response.meta['item']
        item.content = response.xpath('//div[@class="content"]/font/text()')
        yield item
