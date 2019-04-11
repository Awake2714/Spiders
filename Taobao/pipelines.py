# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class TaobaoPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item

class MongoPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient()
    def process_item(self, item, spider):
        self.client.Taobao.clothes.update({'link': item['link']}, {'$set': item}, True)
        return item
    def close(self):
        self.client.close()
