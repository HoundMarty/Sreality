import scrapy
import json
from sreality.items import FlatItem


class FlatSpider(scrapy.Spider):
    name = 'sreality'

    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500']

    def parse(self, response):
        jsonresponse = response.json()
        for item in jsonresponse['_embedded']['estates']:
            yield scrapy.Request( 'https://www.sreality.cz/api' + item['_links']['self']['href'] ,
                          callback=self.parse_flat)
            
    def parse_flat(self,response):
        jsonresponse = response.json()

        # with open('res.json', "w") as json_file:
        #     json.dump(jsonresponse, json_file, indent=4)

        flat = FlatItem()
        flat['name'] = jsonresponse['name']['value'] #+ item['locality']
        for image in jsonresponse['_embedded']['images']:
            if image['_links']['dynamicDown']:
                flat['img_url'] = image['_links']['dynamicDown']['href'].replace('{width}','400').replace('{height}','400')
            else:
                flat['img_url'] = image['_links']['dynamicUp']['href'].replace('{width}','400').replace('{height}','400')

        yield flat
