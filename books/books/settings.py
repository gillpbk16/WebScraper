# Scrapy settings for books project

BOT_NAME = "books"

SPIDER_MODULES = ["books.spiders"]
NEWSPIDER_MODULE = "books.spiders"

ADDONS = {}

ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {
    "books.pipelines.MongoPipeline": 300,
}

FEED_EXPORT_ENCODING = "utf-8"

MONGO_URI = "mongodb://localhost:27017"
MONGO_DATABASE = "books_db"

LOG_LEVEL = "WARNING"
LOG_FILE = "book_scraper.log"