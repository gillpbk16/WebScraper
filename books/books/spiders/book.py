import scrapy
from books.items import BooksItem


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        for book in response.css("article.product_pod"):
            item = BooksItem()
            item['url'] = response.urljoin(book.css("h3 a::attr(href)").get())
            item['price'] = book.css("div.product_price p.price_color::text").get(default="").strip()
            item['title'] = book.css("h3 a::attr(title)").get(default="").strip()

            availability_parts = book.css("p.instock.availability::text").getall()
            item["availability"] = " ".join(part.strip() for part in availability_parts if part.strip())
            
            yield item

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
