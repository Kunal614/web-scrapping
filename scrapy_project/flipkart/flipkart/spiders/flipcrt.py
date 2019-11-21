import scrapy
from scrapy.utils.response import open_in_browser
from ..items import FlipkartItem

class flip(scrapy.Spider):
    name="flipkart"

    start_urls=[
        'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    ]
    def parse(self,response):
        open_in_browser(response)
        items =  FlipkartItem()
        mobile_name = response.css('._3wU53n').css('::text').extract()
        mobile_specification = response.css('.tVe95H').css('::text').extract()
        mobile_price = response.css('._2rQ-NK').css('::text').extract()

        items['mobile_name']=mobile_name
        items['mobile_specification']=mobile_specification
        items['mobile_price']=mobile_price
        
        yield items

   