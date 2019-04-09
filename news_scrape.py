"""
Program: news_scrape.py 
Author: James Jutt
Date: 3/21/19

Uses the Beautiful Soup web scraper to pull RSS data from a public news feed URL.
Requires pip install beautifulsoup4
and pip install lxml which is an xml parse
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from breezypythongui import EasyFrame
class News(EasyFrame):
    """Displays output after user inputs a question and clicks the button"""
    def __init__(self):
        """Sets up the window and widgets"""
        EasyFrame.__init__(self, title = "News Scrape", resizable = False)
        self.mainLabel = self.addLabel(text = "Enter RSS URL", row = 0, column = 0, columnspan = 4, sticky = "NSEW")
        self.inputField = self.addTextField(text = "", row = 1, column = 1)
        self.myBtn = self.addButton(text = "                Enter               ", row = 2, column = 1, command = self.scrape)

    def scrape(self):

        news_url = self.inputField.getText()
        Client = urlopen(news_url)
        xml_page = Client.read()
        Client.close() # Closes the connection to the RSS feed

        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item")

        self.output = self.addTextArea(text = "", row = 3, column = 0, columnspan = 5, width = 80, height = 40)
        for x in news_list:
            self.output.appendText("\n" + x.title.text)
            self.output.appendText("\n" + x.link.text)
            self.output.appendText("\n" + x.pubDate.text)
            self.output.appendText("\n" + "-" * 60)

def main():
    News().mainloop()

if __name__ == "__main__":
    main()

