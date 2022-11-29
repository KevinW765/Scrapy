import scrapy
# from DMOZspider.items import MainItem

class DMOZ_Crawler_main(scrapy.Spider):
    name = 'DMOZ_Crawler_main'
    allowed_domains = ['dmoztools.net/']
    start_urls = [
        'https://dmoztools.net/'
    ]

    def parse(self, response):

        category_div = response.xpath('//div[contains(@class, "category ")]')

        for signle_category_div in category_div:

            top_category = signle_category_div.xpath('./h2/a/text()').getall()

            top_category_link = signle_category_div.xpath('./h2/a/@href').getall()

            sub_category = signle_category_div.xpath('./h3/a/text()').getall()
 
            sub_category_link = signle_category_div.xpath('./h3/a/@href').getall()

            i=0

            while i<len(sub_category):

                yield{'top_category_name':top_category,
                'top_category_link':top_category_link, 
                'sub_category_name':sub_category[i], 
                'sub_category_link':sub_category_link[i]
                }

                i+=1
