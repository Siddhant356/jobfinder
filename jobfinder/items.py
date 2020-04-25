# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobfinderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class ClickItem(scrapy.Item):
    title = scrapy.Field()
    location = scrapy.Field()
    skills = scrapy.Field()
    role = scrapy.Field()
    experience = scrapy.Field()
    job_type = scrapy.Field()
    description = scrapy.Field()
    mobile =  scrapy.Field()
    landline = scrapy.Field() 