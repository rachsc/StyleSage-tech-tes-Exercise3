import scrapy
import requests
import io
import unicodedata
import pandas as pd
from urllib.parse import quote
from ..items import ImageItem


class SearchImageSpider(scrapy.Spider):
    name = 'image-search'

    # Artists names are in artists.csv file, so I need those names for the urls to find their images
    columns = ['name']
    with open("artists.csv", "r") as file:
        lines = [line for line in file]
    df = pd.read_csv(io.StringIO(''.join(lines)), usecols=columns, delimiter=";", dtype={'name': str})
    names = df['name'].to_list()
    # I need the artists names in lowercase
    names_lower = [each_name.lower() for each_name in names]
    # I need to return the normal form NFKD for the unicode names.
    # NFKD: replace all compatibility characters with their equivalents.
    names_form = [unicodedata.normalize("NFKD", each_name) for each_name in names_lower]
    # I replace letters like â with a, and to remove b' in front of every string, I decode back to utf-8
    names_encode = [each_name.encode('ascii', 'ignore').decode('utf-8') for each_name in names_form]
    # Finally I need to escape characters as these names are going to be in the url to look for images
    names_url = [quote(each_name) for each_name in names_encode]
    names_url_final = [each_name.replace('/', '%20') for each_name in names_url]

    start_urls = []
    for each_name in names_url:
        start_urls.append('https://www.allmusic.com/search/all/' + each_name)

    def parse(self, response, **kwargs):
        items = ImageItem()

        image_url = response.xpath(
            '//div[contains(@class, "photo")]/a/img[contains(@class, "cropped-image")]/@src').get()
        name_url = response.xpath(
            '//div[contains(@class, "photo")]/a/img[contains(@class, "cropped-image")]/@alt').get()
        items['image_urls'] = [image_url]
        items['artist_name'] = [name_url]
        # for url in image_url:
        #     for artist_name in self.names_encode:
        with open('./images/'+str(name_url)+'.jpg', 'wb') as handler:
            image = requests.get(image_url)
            handler.write(image.content)

        yield items
