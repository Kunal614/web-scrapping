import scrapy
from scrapy.utils.response import open_in_browser
from ..items import FlipkartItem

class flip(scrapy.Spider):
    name="flipkart"

    start_urls=[
        'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    ]
    def parse(self,response):
        #open_in_browser(response)
        items =  FlipkartItem()
        mobile_name = response.css('._3wU53n').css('::text').extract()
        mobile_specification = response.css('.tVe95H').css('::text').extract()
        mobile_price = response.css('._2rQ-NK').css('::text').extract()
        k=0
        y=0
        print(len(mobile_name))
        for i in range(len(mobile_name)):
            items['mobile_name']=mobile_name[i]
            items['mobile_specification']=mobile_specification[k]
            items['mobile_price']=mobile_price[y]
            k+=1
            y+=1
            yield items
        
        

   
