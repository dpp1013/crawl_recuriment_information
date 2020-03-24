# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# 数据字段的存储地方
import scrapy


class RecruitmentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = scrapy.Field()
    companyname = scrapy.Field()
    workingplace = scrapy.Field()
    salary = scrapy.Field()
    posttime = scrapy.Field()
