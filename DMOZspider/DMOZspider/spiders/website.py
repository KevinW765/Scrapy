import scrapy
# from bs4 import BeautifulSoup
# from DMOZspider.items import DmozItem

class DMOZ_Crawler_website(scrapy.Spider):
    name = 'DMOZ_Crawler_website'
    allowed_domains = ['dmoztools.net/']
    start_urls = [
        'https://dmoztools.net/'
    ]
    
    def parse(self, response):
        '''test response (response.body.decode("utf-8") can be replaced by response.body)'''
        # filename = 'dmoztools.html'
        # open(filename, 'w').write(response.body.decode("utf-8"))
        # filename.close()

        # soup = BeautifulSoup(response.body, 'html.parser')
        # Category_tags = soup.find_all('a')
        # for tag in Category_tags:
            # print(tag.text.strip())
            # print(tag.get('href'))

        # print(1)
        urls1 = response.xpath('//a')
        for url in urls1:
            url_name = url.xpath('./text()').getall()
            url_link = url.xpath('./@href').getall()
            yield{'url_name':url_name,'url_link':url_link}