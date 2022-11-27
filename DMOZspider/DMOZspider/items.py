# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Fiel   
    Category = scrapy.Field()
    Website_name = scrapy.Field()
    Website_url = scrapy.Field()
    website_title_tag = scrapy.Field()
    
