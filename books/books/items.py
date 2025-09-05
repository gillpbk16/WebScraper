import scrapy


class BooksItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()    
    price = scrapy.Field()
    title = scrapy.Field()
    availability = scrapy.Field()
