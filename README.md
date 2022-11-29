# Scrapy
Use Scrapy to extract category. Website name. Website URL. website title tag on https://dmoztools.net/

# Version Control
Python Version - Python 3.10.0

Other Modules and Packages used - refer to requirements.txt in Scrapy/DMOZspider/

# Explanation

The results are in 'CSV result' folder in DMOZspider folder.

A Scrapy spider is usually responsible for extract a specific target. In this task, the goal is to make the Scrapy be able to write to the output Category. Website name. Website URL. Extract the website title tag content if possible. 

In my first attempt, for each of the four targets, I used four spiders to extract the title tag of the website, top as well as sub categories, all the urls appeared on the site. 

However, combining all the results from these 4 aspects together in a csv via Scrapy seems a little bit hard. Since I found that creating 4 items in items.py and yielding them separately but all in main.py is not actually acceptable for scrapy to output these results together in a single csv. I am not sure why and tried different methods such as modifying the settings.py, pipelines.py, using signle item but with array field... The ideal csv result is file ideal_result.csv.

# To run the code
open terminal and cd to DMOZspider folder

scrapy crawl DMOZ_Crawler_sub_cat -o sub_cat.csv

scrapy crawl DMOZ_Crawler_top_cat -o top_cat.csv

scrapy crawl DMOZ_Crawler_website -o website.csv

scrapy crawl DMOZ_Crawler_title_tag -o title_tag.csv