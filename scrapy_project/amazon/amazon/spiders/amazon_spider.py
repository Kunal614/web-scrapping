import scrapy
from scrapy.utils.response import open_in_browser
from ..items import AmazonItem
class amazon(scrapy.Spider):
    name="amazon"
    start_urls=[
        'https://www.amazon.in/s?k=books&ref=nav_signin'
    ]
    
    def parse(self,response):
        items = AmazonItem()
        open_in_browser(response)
        title= response.css(".a-color-base.a-text-normal").css("::text").extract()
        price = response.css(".a-price-whole").css("::text").extract()
        dilivery_charge=response.css(".s-align-children-center+ .a-row span").css("::text").extract()
        image_link = response.css(".s-image::attr(src)").extract()
        items['title']=title
        items['price']=price
        items['dilivery_charge']=dilivery_charge
        items['image_link']=image_link
        yield items