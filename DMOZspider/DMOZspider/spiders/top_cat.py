import scrapy
# from bs4 import BeautifulSoup
# from DMOZspider.items import DmozItem

class DMOZ_Crawler_top_cat(scrapy.Spider):
    name = 'DMOZ_Crawler_top_cat'
    allowed_domains = ['dmoztools.net/']
    start_urls = [
        'https://dmoztools.net/'
    ]
    
    def parse(self, response):
        categorys = response.xpath('//*[@class="top-cat"]')
        for category in categorys:
            top_category = category.xpath('./a/text()').getall()
            print(top_category)
            yield{'top_category':top_category}