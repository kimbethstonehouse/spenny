import scrapy

class NumbeoSpider(scrapy.Spider):
    name = "numbeo"

    def start_requests(self):
        urls = [
            'https://www.numbeo.com/cost-of-living/in/Edinburgh',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        listItems = response.xpath('//table/tr[th/text()="Restaurants"]/../tr/td[text()!="\n"]/text()').getall()
        listLowRanges = response.xpath('//span[@class="barTextLeft"]/text()').getall()
        listHighRanges = response.xpath('//span[@class="barTextRight"]/text()').getall() 
        length = len(listItems)

        # really really basic error checking
        # this should never occur
        if length % 2 == 0:
            # first element is text
            # element immediately after is price
            for i in range(0, length, 2):
                yield {
                    'text': listItems[i],
                    'price': listItems[i+1],
                }

            for i in range(0, length):
                yield {
                    'lowRange': listLowRanges[i],
                    'highRange': listHighRanges[i],
                }
