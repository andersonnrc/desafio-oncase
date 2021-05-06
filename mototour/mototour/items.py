# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MototourItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    titulo = scrapy.Field()
    autor = scrapy.Field()
    dt_postagem = scrapy.Field()
    texto = scrapy.Field()
    site = scrapy.Field()
