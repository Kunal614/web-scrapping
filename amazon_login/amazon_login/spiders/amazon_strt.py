import scrapy
from scrapy.http import FormRequest
from ..items import AmazonLoginItem
from scrapy.utils.response import open_in_browser

class amazon(scrapy.Spider):
    name='amazon'    
    start_urls=[
            'https://www.amazon.com/ap/signin?accountStatusPolicy=P1&clientContext=258-3200785-8273163&language=en_US&openid.assoc_handle=amzn_prime_video_desktop_us&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_encoding%3DUTF8%26location%3D%252Fref%253Dav_nav_sign_in'
    ]
    page_number=2  
    def parse(self,response):
            
            token = response.css("form input::attr(value)").extract_first()
            
            return FormRequest.from_response(response,formdata={
                    'appActionToken':token,
                    'Email':'8864084790',
                    'password':'kunalka@1'
            },callback=self.start_scrapping)
            
            
          
    def start_scrapping(self,response):
        open_in_browser(response)
        item = AmazonLoginItem()
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
            yield response.follow(next_page , callback = self.start_scrapping)



         