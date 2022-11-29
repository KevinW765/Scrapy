import scrapy

from DMOZspider.items import TitleItem
from DMOZspider.items import TopCatItem
from DMOZspider.items import UrlItem
from DMOZspider.items import SubCatItem
# from DMOZspider.items import MainItem

class DMOZ_Crawler_Attempt(scrapy.Spider):
    name = 'DMOZ_Crawler_Attempt'
    allowed_domains = ['dmoztools.net/']
    start_urls = [
        'https://dmoztools.net/'
    ]

    def parse(self, response):

        # Create Item
        # Main_Item = MainItem()
        Title_Item = TitleItem()
        TopCat_Item = TopCatItem()
        SubCat_Item = SubCatItem()
        Url_Item = UrlItem()
        # item_list = []

        # title_tag
        title_tag = response.xpath('//title/text()').getall()
        Title_Item['title_tag'] = title_tag
        yield Title_Item

        # title_tag = response.xpath('//title/text()').getall()
        # yield{'title_tag':title_tag}

        # Top Category
        top_categorys = response.xpath('//*[@class="top-cat"]')
        # Main_Item['top_category'] = top_categorys
        # i = 0
        # while i < len(top_categorys):
        # for top_category in top_categorys:
            # print(top_categorys[i])
            # top_category = top_category.xpath('./a/text()').getall()
            # Main_Item['top_category_array'] = top_category
            # i += 1
            # TopCat_Item = TopCatItem()
            # top_category = top_category.xpath('./a/text()').getall()
            # Main_Item['top_category'] = top_category
        for top_category in top_categorys:
            SubCat_Item = SubCatItem()
            top_category = top_category.xpath('./a/text()').getall()
            TopCat_Item['top_category'] = top_category
            yield TopCat_Item

        # Sub Category
        sub_categorys = response.xpath('//*[@class="sub-cat"]')
        for sub_category in sub_categorys:
            SubCat_Item = SubCatItem()
            sub_category = sub_category.xpath('./a/text()').getall()
            SubCat_Item['sub_category'] = sub_category
            yield SubCat_Item

        # Url
        urls = response.xpath('//a')
        for url in urls:
            url_name = url.xpath('./text()').getall()
            url_link = url.xpath('./@href').getall()
            Url_Item['url_name'] = url_name
            Url_Item['url_link'] = url_link
            yield Url_Item
            # item_list.append(Url_Item)

        # yield Main_Item
