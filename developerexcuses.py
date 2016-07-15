import requests
from bs4 import BeautifulSoup


class ReturnExcuse:
    def __init__(self):
        print ('Title requested.')

    def getExcuse(self):
        content = self._getContent()
        if content:
            excuse = self._getStringFromContent(content)
            return excuse
        else:
            return "No access to the website anymore."

    @staticmethod
    def _getContent():
        r = requests.get('http://developerexcuses.com/')
        if r:
            return r
        else:
            return False

    @staticmethod
    def _getStringFromContent(content):
        soup = BeautifulSoup(content.text, "html.parser")
        elem = soup.find('a')
        return elem.text.encode('utf-8', 'ignore')


if __name__ == "__main__":
    T = ReturnExcuse()
    print T.getExcuse()
