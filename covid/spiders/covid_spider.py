from scrapy import Spider
from scrapy.selector import Selector
from covid.items import CovidItem

class CovidSpider(Spider):
    name = "covid"
    # allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread"]

    def parse(self, response):
        countries = response.xpath('table[@id="table3"]/tbody/tr')
        for country in countries:
            item = CovidItem()
            item['country'] = country.xpath('td[1]/text()').get()
            item['cases'] = country.xpath('td[2]/text()').get()
            item['deaths'] = country.xpath('td[3]/text()').get()
            item['region'] = country.xpath('td[4]/text()').get()
            yield item
        pass
