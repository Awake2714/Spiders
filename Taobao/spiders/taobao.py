# -*- coding: utf-8 -*-
import scrapy
from Taobao.items import TaobaoItem
from Taobao.settings import KEYWORD, STARTPAGE, ENDPAGE

class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["taobao.com"]
    base_url = 'https://re.taobao.com/search?keyword={keyword}&page={num}'

    def start_requests(self):
        for page in range(STARTPAGE, ENDPAGE+1):
            self.url = self.base_url.format(keyword= KEYWORD, num=page)
            yield scrapy.Request(url=self.url)


    def parse(self, response):
        goods = response.xpath('//div[@id="J_waterfallWrapper"]/div[@class="item"]')
        for good in goods:
            title = good.xpath('.//span[@class="title"]/@title').extract_first()
            print('正在爬取：%s' % title)
            link = good.xpath('./a/@href').extract_first()
            shop = good.xpath('.//p[@class="shopName"]//span[@class="shopNick"]/text()').extract_first()
            price = good.xpath('.//p[@class="price"]/span[@class="pricedetail"]/strong/text()').extract_first(default=0)
            paynum = good.xpath('.//p[@class="shopName"]/span[@class="payNum"]/text()').extract_first(default=0)[:-3]
            score = good.xpath('.//div[@class="dsr-info"]//span[@class="dsr-info-num"]/text()').extract_first(default=0)
            yield {
                'title': title,
                'link': link,
                'shop': shop,
                'price': price,
                'paynum': paynum,
                'score': score
            }
