# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyTestPipeline(object):
    @staticmethod
    def process_item(item, spider):
        path = '/Users/cloudin/Desktop/LiuFeng/Fiction_Factory/temp/'
        with open(path+item.name+'.txt', 'w+') as f:
            f.write(item.content)        
