# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from books_to_scrape.items import BooksToScrapeItem


class ImagestoscrapeSpider(scrapy.Spider):
    name = 'imagestoscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        for article in response.xpath("//article[@class='product_pod']"):
            loader = ItemLoader(item=BooksToScrapeItem(), selector=article)
            relative_url = article.xpath(".//div[@class='image_container']/a/img/@src").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('image_urls', absolute_url)
            loader.add_xpath('book_name', './/h3/a/@title')  # adding this path to the main response.xpath()
            yield loader.load_item()
