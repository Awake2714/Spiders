# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    shop = scrapy.Field()
    price = scrapy.Field()
    paynum = scrapy.Field()
    score = scrapy.Field()
