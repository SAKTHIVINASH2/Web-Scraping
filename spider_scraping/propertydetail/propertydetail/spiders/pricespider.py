import re
import json
import scrapy

class PricespiderSpider(scrapy.Spider):
    name = "pricespider"
    allowed_domains = ["www.rightmove.co.uk"]
    start_urls = [
        "https://www.rightmove.co.uk/house-prices/nw3.html?searchLocation=NW3&useLocationIdentifier=false&locationIdentifier=&pageNumber=1"
    ]

    def parse(self, response):
        # Extract the entire script content
        script_text = response.xpath("//script[contains(text(),'window.PAGE_MODEL')]//text()").get()
        
        if not script_text:
            self.logger.error("[-] PAGE_MODEL script not found")
            return

        # Use regex to extract JSON safely
        match = re.search(r"window\.PAGE_MODEL\s*=\s*(\{.*\});?", script_text, re.DOTALL)
        if not match:
            self.logger.error("[-] PAGE_MODEL data not matched by regex")
            return

        json_str = match.group(1)

        try:
            data = json.loads(json_str)
        except json.JSONDecodeError as e:
            self.logger.error(f"[-] JSON parsing failed: {e}")
            return

        properties = data.get('searchResult', {}).get('properties', [])

        for property_item in properties:
            yield {
                "address": property_item.get('address'),
                "type": property_item.get('propertyType'),
                "bedrooms": property_item.get('bedrooms'),
                "transactions": property_item.get('transactions', [{}])[0].get('displayPrice'),
                "location": property_item.get('location'),
                "detail_url": property_item.get('detailUrl'),
            }
