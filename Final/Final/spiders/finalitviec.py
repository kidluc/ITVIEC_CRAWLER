import scrapy
import datetime
from Final.items import Items, time_convert, cvstring


class ItvietSpider(scrapy.Spider):
    name = "itfinal"
    allowed_domain = 'itviet.com'
    start_urls = ['https://itviec.com/it-jobs']

    def parse(self, response):
        # Get url in every link
        url_selector = response.xpath('//h2[@class="title"]/a/@href').extract()
        for url in url_selector:
            yield scrapy.Request((response.urljoin(url)),
                                 callback=self.parse_inside_item)

    def parse_inside_item(self, response):
        now = datetime.datetime.now()
        item = Items()
        item['title'] = response.xpath('//h1[@class="job_title"]'
                                       '/text()')[0].extract().strip()
        item['link'] = response.url
        item['job'] = cvstring(response.xpath('//div[@class="description"]/'
                                              '/text()').extract()[1:-1])
        item['skill'] = cvstring(response.xpath('//div[@class="experience"]/'
                                                '/text()').extract()[1:-1])
        item['time'] = time_convert(now)
        yield item
