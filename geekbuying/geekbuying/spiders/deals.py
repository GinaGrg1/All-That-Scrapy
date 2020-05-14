# -*- coding: utf-8 -*-
import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.geekbuying.com']
    start_urls = ['https://www.geekbuying.com/deals/categorydeals']

    def parse(self, response):
        products = response.xpath("//div[@class='flash_li']")
        for product in products:
            product_name = product.xpath(".//a[@class='flash_li_link']/text()").get(),
            product_url = product.xpath(".//a[@class='flash_li_link']/@href").get(),
            product_price = product.xpath(".//div[@class='flash_li_price']/span/text()").get()           
            yield {
                'product_name': product_name,
                'product_url': product_url,
                'product_price': product_price
            }
        next_page = response.xpath("//a[@class='next']/@href").get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
