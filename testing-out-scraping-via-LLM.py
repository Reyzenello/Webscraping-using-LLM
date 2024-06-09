import os
import subprocess
import json
import openai
from scrapy import Spider, signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

# Set up OpenAI API key
openai.api_key = 'your_open_ai_key'

# Define the Scrapy spider
class TokenSpider(Spider):
    name = "token_spider"
    
    def __init__(self, *args, **kwargs):
        super(TokenSpider, self).__init__(*args, **kwargs)
        self.token = kwargs.get('token')
        self.start_urls = [
            f'https://www.google.com/search?q={self.token}'  # Replace with the actual URL where you need to view the token
        ]

    def parse(self, response):
        found = self.token in response.text
        yield {
            'token': self.token,
            'found': found
        }

# Function to run the Scrapy spider
def run_scrapy_spider(token):
    output_data = []

    def crawler_results(signal, sender, item, response, spider):
        output_data.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_passed)

    process = CrawlerProcess(settings={
        "FEEDS": {
            "output.json": {"format": "json"},
        },
    })

    process.crawl(TokenSpider, token=token)
    process.start()  # the script will block here until the crawling is finished
    
    return output_data

# Function to interact with OpenAI's API
def use_openai(data):
    token = data[0]['token']
    found = data[0]['found']

    result = {
        'token': token,
        'found': found
    }
    
    with open('result.json', 'w') as f:
        json.dump(result, f)

    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    token = "your_token"
    data = run_scrapy_spider(token)
    if data:
        use_openai(data)
