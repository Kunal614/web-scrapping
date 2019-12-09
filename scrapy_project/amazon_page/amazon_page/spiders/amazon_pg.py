import scrapy
from ..items import AmazonPageItem

class amazon(scrapy.Spider):
    
    name='amazon'
    start_urls=[
        'https://www.amazon.in/s?k=books&ref=nb_sb_noss_2'
    ]
    page_number=2
    def parse(self,response):
        item = AmazonPageItem()
        book_name= response.css('.a-color-base.a-text-normal').css('::text').extract()
        book_author=response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        book_price = response.css('.a-price-whole').css('::text').extract()
        k=0
        y=0
       

        for i in range(len(book_name)):
            item['book_name']=book_name[i]
            item['book_author']=book_author[k]
            item['book_price']=book_price[y]
            k+=1
            y+=1
            yield item
        next_page='https://www.amazon.in/s?k=books&page=' + str(amazon.page_number) +'&qid=1575269122&ref=sr_pg_2' 
        if amazon.page_number<=100:
            amazon.page_number+=1
            yield response.follow(next_page , callback = self.parse)


               

        
       


