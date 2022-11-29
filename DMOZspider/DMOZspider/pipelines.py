# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DmozspiderPipeline:
    def process_item(self, item, spider):
        return item

# class TitleItemPipeline(object):
#     def process_item(self, item, spider):
#         if isinstance(item, CommentItem):
#            # Your business here

# class UrlItemPipeline(object):
#     def process_item(self, item, spider):
#         if isinstance(item, UrlItem):
#           # Your business here