# Scrapy
Use Scrapy to extract category. Website name. Website URL. website title tag on https://dmoztools.net/

# To run the code
open terminal and cd to DMOZspider fold

scrapy crawl DMOZ_Crawler_sub_cat -o sub_cat.csv

scrapy crawl DMOZ_Crawler_top_cat -o top_cat.csv

scrapy crawl DMOZ_Crawler_website -o website.csv

scrapy crawl DMOZ_Crawler_title_tag -o title_tag.csv
