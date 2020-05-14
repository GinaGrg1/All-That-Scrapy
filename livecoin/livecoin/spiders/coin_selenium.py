# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CoinSpiderSelenium(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['www.livecoin.net/en']
    start_urls = ['https://www.livecoin.net/en']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome("/Users/reginagurung/Documents/Drivers/chromedriver", options=chrome_options)
        driver.set_window_size(1920, 1080)  # browser resolution so that we get the full page
        driver.get("https://www.livecoin.net/en")

        ltc_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        ltc_tab[4].click()

        # Selenium does not have callback() so we need to pass this html markup to parse()
        self.html = driver.page_source
        driver.close()


    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class,'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)': currency.xpath(".//div[2]/span/text()").get(),
            }
