# create a web crawler that can crawl through a website and output the links
# and text of each page.
# A Web crawler, sometimes called a spider or spiderbot and often shortened to crawler, is an Internet bot that systematically browses the World Wide Web and that is typically operated by search engines for the purpose of Web indexing (web spidering)
# Web search engines and some other websites use Web crawling or spidering software to update their web content or indices of other sites' web content. Web crawlers copy pages for processing by a search engine, which indexes the downloaded pages so that users can search more efficiently.
# Crawlers consume resources on visited systems and often visit sites unprompted. Issues of schedule, load, and "politeness" come into play when large collections of pages are accessed.

# import the necessary packages
import requests
from bs4 import BeautifulSoup

# define the main function
def main():
    # ask the user for the url
    url = input("Enter a URL: ")
    # use the requests library to get the url
    r = requests.get(url)
    # use the BeautifulSoup library to parse the html
    soup = BeautifulSoup(r.text, "html.parser")
    # print the title of the page
    print(soup.title.string)
    # print the text of the page
    print(soup.get_text())

    # loop through the links on the page
    for link in soup.find_all('a'):
        # print the href of the link
        print(link.get('href'))

        
        # call the main function
if __name__ == "__main__":
    main()
