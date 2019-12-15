import scrapy

class amazon_mobile(scrapy.Spider):
    name='amazon'
    start_urls=['https://www.amazon.in/s?k=mobile&i=electronics&rh=n%3A1389401031&qid=1576442620&ref=sr_pg_1']
    page_number=2

    def parse(self,response):
        name=response.xpath("//span[@class='a-size-medium a-color-base a-text-normal']/text()").extract()
        price = response.xpath("//span[@class='a-price-whole']/text()").extract()
        k=0
        for i in range(len(price)):
            yield {
            'name':name[i],
            'price':price[k]

            }
            k+=1
        next_page="https://www.amazon.in/s?k=mobile&i=electronics&rh=n%3A1389401031&page="+str(amazon_mobile.page_number)+"&qid=1576442631&ref=sr_pg_2"
        amazon_mobile.page_number+=1
        if amazon_mobile.page_number<=400:
            yield response.follow(next_page,callback=self.parse)