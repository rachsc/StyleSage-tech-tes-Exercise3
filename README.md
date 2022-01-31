# EXERCISE 3

## Requirements
- Python 3.8
- Scrapy 2.5.1 4.0
- Requests 2.27.1
- Pandas 1.4
- Pillow 9

## Installation
After you cloned the respository, you want to create a virtual environment, so you have a clean python installation. 
```
python -m venv env
```
Once you´ve created a virtual environment, you may activate it.
```
(On Windows): env\Scripts\activate.bat
(On Unix or MacOS): source env/bien/activate
```
You can install all the required dependencies by running
```
pip install -r requirements.txt
```
## Use
This is a Scrapy project. It needs to have a **artists.csv** file at the project´s root directory as it is the file downloaded from exercise 1 with the artists names.

The spider will use each name in that file to complete this url: https://www.allmusic.com/search/all/

That way, we can find the image of that artists in that web page. This web page does not have images for all the artists though.

To execute it, just run:
```
scrapy crawl image-search
```

This will download an image for each artist if there is one in the page selected. They will be stored in the folder **images**.