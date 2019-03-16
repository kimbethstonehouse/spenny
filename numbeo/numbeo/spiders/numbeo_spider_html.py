import scrapy

class NumbeoHTMLSpider(scrapy.Spider):
    name = "numbeo-html"

    def start_requests(self):
        urls = [
            'https://www.numbeo.com/cost-of-living/in/Edinburgh',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'numbeo-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
