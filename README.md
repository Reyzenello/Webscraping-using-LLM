# Webscraping-using-LLM
Personal project to test it out web-scraping tools with dark web engine and retrieving API keys

Here are the result, which you can use for example retrieve API key:


![image](https://github.com/Reyzenello/Webscraping-using-LLM/assets/43668563/9e8670b0-c8cc-4d74-8dbc-ce8773fc2d32)


1. Importing Libraries: Imports necessary libraries for web scraping, interacting with the operating system, JSON handling, and OpenAI's API.

2. Setting up OpenAI API Key: Sets the API key for accessing OpenAI's services. Remember to replace 'your_open_ai_key' with your actual key.

3. Defining the Scrapy Spider (TokenSpider class):

class TokenSpider(Spider):
    name = "token_spider"
    # ...
Use code with caution.
Python
name: A unique name for the spider.

__init__: Constructor.

Takes the token as an argument and stores it.

Constructs the starting URL using an f-string. You'll likely need to replace f'https://www.google.com/search?q={self.token}' with the actual URL of the page you want to scrape.

parse: The method called for each response received from a URL.

found = self.token in response.text: Checks if the token is present in the response's text content.

yield {'token': self.token, 'found': found}: Yields a dictionary containing the token and whether it was found. This is how Scrapy collects data.

4. Running the Scrapy Spider (run_scrapy_spider function):

def run_scrapy_spider(token):
    # ...
Use code with caution.
Python
output_data = []: A list to store scraped data.

crawler_results: A callback function to collect the scraped items. It appends each item to output_data.

dispatcher.connect(...): Connects the crawler_results callback to the signals.item_passed signal. This ensures the callback is invoked whenever an item is scraped.

process = CrawlerProcess(...): Creates a Scrapy CrawlerProcess to manage the spider's execution.

Sets up a feed to save the output to output.json.

process.crawl(TokenSpider, token=token): Starts crawling with the TokenSpider and passes the token as an argument.

process.start(): Starts the crawling process. This blocks until crawling is finished.

Returns the collected output_data.

5. Interacting with OpenAI (use_openai function):

def use_openai(data):
    # ...
Use code with caution.
Python
Extracts the token and found status from the scraped data.

Creates a dictionary result and saves it to result.json.

Prints the result in formatted JSON. It's here that you would typically integrate your OpenAI API call. Currently, it just saves and prints the scraped data.

6. Main Execution Block (if __name__ == "__main__":)

if __name__ == "__main__":
    token = "your_token" # Replace with your token
    data = run_scrapy_spider(token)
    if data:
        use_openai(data)
Use code with caution.
Python
Sets the token to search for. Replace "your_token" with the actual token.

Runs the Scrapy spider with the token.

If data is returned, calls the use_openai function.
