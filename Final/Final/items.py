# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import time
import datetime
from scrapy.item import Item, Field


class Items(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    link = Field()
    job = Field()
    skill = Field()
    time = Field()

    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    pass


def time_convert(n):
    ''' Convert string time to ISO format '''
    return n.strftime('%Y_%m_%d_%H_%M_%S')


def cvstring(l):
    return ','.join(l)


def cvlist(l):
    return l.split(',')