# CSS Selectors

next_page = response.css('a[title=Selanjutnya]::attr(href)').get()
all_products = response.css('div.product-item-info')
product_detail_page_link = response.css('div.product.details.product-item-details')
product_price = response.css('span.price::text').get()
product_name = response.css('a.product-item-link::text').get()
product_imgae = response.css('img.product-image-photo::attr(src)').get()