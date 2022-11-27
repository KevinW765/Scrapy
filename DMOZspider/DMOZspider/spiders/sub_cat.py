import scrapy
# from bs4 import BeautifulSoup
# from DMOZspider.items import DmozItem

class DMOZ_Crawler_sub_cat(scrapy.Spider):
    name = 'DMOZ_Crawler_sub_cat'
    allowed_domains = ['dmoztools.net/']
    start_urls = [
        'https://dmoztools.net/'
    ]
    
    def parse(self, response):
        subcategorys = response.xpath('//*[@class="sub-cat"]')
        for category in subcategorys:
            sub_category = category.xpath('./a/text()').getall()
            print(sub_category)
            yield{'sub_category':sub_category}
