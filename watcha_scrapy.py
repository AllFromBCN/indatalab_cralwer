import scrapy

class watchaSpider(scrapy.spider):
    name = "watcha-reviews"

    def startRequests(self):
        urls = ['https://watcha.net/login',]
        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):

