import scrapy


from skechers.items import ProductItem

class AllmenshoesSpider(scrapy.Spider):
    name = "allmenshoes"
    allowed_domains = ["www.skechers.id"]
    start_urls = ["https://www.skechers.id/pria/shoes.html"]

    def parse(self, response):
        for item in response.css("div.product-item-info"):
            product = ProductItem()

            product["name"]= item.css("a.product-item-link::text").get().strip()
            product["price"]= item.css("span.price::text").get()
            product["image_url"]= item.css("img.product-image-photo::attr(src)").get()
            product["product_url"]= item.css("a.product-item-link::attr(href)").get()

            yield product

        next_page = response.css("a[title=Selanjutnya]::attr(href)").get()
        print(f"Next page: {next_page}")
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)