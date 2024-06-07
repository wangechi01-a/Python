import scrapy
import os
import html2text
from urllib.parse import urljoin

class HuggingfaceSpider(scrapy.Spider):
    name = "huggingface"
    allowed_domains = ["huggingface.co"]
    start_urls = ["https://huggingface.co/doc/diffusers/index"]

def __init__(self, *args, **kwargs):
    super(HuggingfaceSpider, self).__init__(*args, **kwargs)

    # Create the output folder if it doesn't exist
    if not os.path.exists("output"):
        os.makedirs("output")
    
    # Initialize the html2text converter
    self.converter = html2text.HTML2Text()
    self.coverter. ignore_links = True
    self.coverter. ignore_images = True
    self.coverter. ignore_emphasis = True
    self.coverter. ignore_tables = True
    self.coverter. ignore_width = 0



    def parse(self, response):
        # Convert the HTML content to plain text
        text = self.converter.handle(response.body.decode())
        text = text.replace("<|endoftext|>"," ")
        
        # Clean up the text
        text = text.strip()

        # Determine the filename based on the URL
        url = response.url.strip("/")
        # Generate a random filename using hash of the url
        filename = f"output/{hash(url)}.text"
        # write the text to a separate file
        with open(filename,"w") as f:
            f.write(text)
        # follow the link to the other page
        for link in response.xpath("//ahref"):
            href = link.get()
            if href.startswith("/docs/diffusers"):
                # Join the relative URL with the base URL of the current page
                url = urljoin(response.url, href)
                yield scrapy.Request(url, callback = self.parse) 



