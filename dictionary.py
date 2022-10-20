import requests
from bs4 import BeautifulSoup

class Dictionary:
    def __init__(self,word):
        self.word=word
    def get_url(self):
        return "http://www.vocabulary.com/dictionary/"+str(self.word)
    def soup_code(self):
        source_code=requests.get(self.get_url())
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,'html.parser')
        return soup

    def get_short_meaning(self):
        soup=self.soup_code()
        link=soup.find('p',{'class':'short'})
        return (link.get_text().replace(".",".\n"))
    def get_long_meaning(self):
        soup=self.soup_code()
        link = soup.find('p', {'class': 'long'})
        return (link.get_text().replace(". ",".\n"))



