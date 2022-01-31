from scrapy.item import Item, Field


class ImageItem(Item):
    artist_name = Field()
    image_urls = Field()
