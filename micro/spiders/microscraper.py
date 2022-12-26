import scrapy


class MicroscraperSpider(scrapy.Spider):
    name = 'microscraper'
    allowed_domains = ['tienda.bricogeek.com']
    start_urls = ['http://tienda.bricogeek.com/94-raspberry-pi/']


    def parse(self, response):

         for item in response.xpath("//div[@id='page']/div[@class='columns-container']/div[@class='container']/div[@class='row']/div[@id='center_column']/ul[@class='product_list product_content grid ']/li[@class='ajax_block_product item_out col-xs-6 col-sm-4 col-lg-3']/div[@class='product-container item']/div[@class='right-block']"):
            name = item.xpath(".//h5/a/@title").get()
            model = item.xpath(".//h5/span/text()").get()
            description = item.xpath(".//p[@class='product-desc']/text()").get().strip()
            price = item.xpath(".//div[@class='price-box']/span[@class='price']/text()").get().strip()
            yield {
                "name": name,
                "model": model,
                "description": description,
                "price": price
            }
