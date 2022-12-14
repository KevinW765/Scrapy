# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MainItem(scrapy.Item):
    top_category_name = scrapy.Field()
    top_category_link = scrapy.Field()
    sub_category_name = scrapy.Field()
    sub_category_link = scrapy.Field()

class TitleItem(scrapy.Item):
    title_tag = scrapy.Field()

class TopCatItem(scrapy.Item):
    top_category = scrapy.Field()
    
class SubCatItem(scrapy.Item):
    sub_category = scrapy.Field()

class UrlItem(scrapy.Item):
    url_name = scrapy.Field()
    url_link = scrapy.Field()
