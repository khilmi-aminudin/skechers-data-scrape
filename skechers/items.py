# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SkechersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProductItem(scrapy.Item):
    # Product name
    name = scrapy.Field()
    # Product price
    price = scrapy.Field()
    # Product image URL
    image_url = scrapy.Field()
    # Product URL
    product_url = scrapy.Field()