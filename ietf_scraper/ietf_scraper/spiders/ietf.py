import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        # title = response.css('span.title::text').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        author_name = response.xpath('//span[@class="author-name"]/text()').get()
        author_company = response.xpath('//span[@class="author-company"]/text()').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        address = response.xpath('//span[@class="address"]/text()').get()
        email = response.xpath('//span[@class="email"]/text()').get()
        phone = response.xpath('//span[@class="phone"]/text()').get()
        return {"title": title, 'author_name': author_name, 'author_company': author_company, 'date': date,
                'address': address, 'email': email, 'phone': phone}
