import hashlib
from io import StringIO
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline, ImageException


class ArtistImagePipeline(object):
    def process_item(self, item, spider):
        return item
    # def get_media_requests(self, item, info):
    #     # return [Request(x) for x in item.get('image_urls', [])]
    #     for image_url in item['image_urls']:
    #         image_url = "http://" + image_url
    #         yield Request(image_url)
    #
    # def item_completed(self, results, item, info):
    #     # item['images'] = [x for ok, x in results if ok]
    #     # return item
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem("Item contains no images")
    #     return item
    #
    # # Override the convert_image method to disable image conversion
    # def convert_image(self, image, size=None):
    #     buf = StringIO()
    #     try:
    #         image.save(buf, image.format)
    #     except Exception as ex:
    #         raise ImageException("Cannot process image. Error: %s" % ex)
    #
    #     return image, buf
    #
    # def image_key(self, url):
    #     image_guid = hashlib.sha1(url).hexdigest()
    #     return 'full/%s.jpg' % (image_guid)
