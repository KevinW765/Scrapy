import scrapy
# from bs4 import BeautifulSoup
# from DMOZspider.items import DmozItem

class DMOZ_Crawler_title_tag(scrapy.Spider):
    name = 'DMOZ_Crawler_title_tag'
    allowed_domains = ['dmoztools.net/']
    start_urls = [
        'https://dmoztools.net/'
    ]
    
    def parse(self, response):
        title_tag = response.xpath('//title/text()').getall()
        print(title_tag)
        yield{'title_tag':title_tag}