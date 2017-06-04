import scrapy
from ..items import Items


class GitJobSpider(scrapy.Spider):
    name = "final"
    allowed_domains = ["github.com"]
    start_urls = ['https://www.github.com/awesome-jobs/vietnam/issues/']

    def parse(self, response):
        # Get url in every page
        url_selector = response.xpath('//*[@class="float-left col-9 p-2'
                                      'lh-condensed"]/a/@href').extract()
        for url in url_selector:
            yield scrapy.Request((response.urljoin(url)),
                                 callback=self.parse_inside_item)

        # Get next page url
        next_page = response.xpath("//*[@class='next_page']/"
                                   "@href").extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page))

    def parse_inside_item(self, response):
        # Crawler data title and link from web site
        item = Items()
        item['title'] = response.xpath('//*[@class="js-issue-title"]/'
                                       'text()')[0].extract().strip()
        item['link'] = response.url
        yield item
