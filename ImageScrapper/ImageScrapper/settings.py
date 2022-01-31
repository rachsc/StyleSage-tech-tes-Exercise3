BOT_NAME = 'ImageScrapper'

SPIDER_MODULES = ['ImageScrapper.spiders']
NEWSPIDER_MODULE = 'ImageScrapper.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'ImageScrapper.pipelines.ArtistImagePipeline': 300,
}

# Set image thumbnail
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (250, 250),
}
# Image filter, minimum height and width, no download below this size
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110