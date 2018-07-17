from bs4 import BeautifulSoup
import requests
import json
import re
from urllib.parse import urljoin


class book_bookkey():
    def __init__(self):
        self.version = '0.0.1'
        self.server_url = 'http://oa.9oe.com/index.php/book/apibook'
        self.baidu_url = 'https://www.baidu.com/s?wd='

    def getHtml(self, query_url):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        req = requests.get(query_url, headers=header)
        req.encoding = req.apparent_encoding
        if req.status_code == 200:
            return req.text
        print(req.text)
        return

    def getBookKey(self):
        book_key = ''
        data = {
            'model': 'book_key_get',
        }
        req = requests.post(url=self.server_url, data=data)
        # html=req.text
        print(req.text)
        json_data = req.json()
        # json_data=json.loads(html)
        book_key = json_data['data']
        print(book_key['book_key'])
        return book_key['book_key']

    def serverSwap(self, data):
        req = requests.post(url=self.server_url, data=data)
        html = req.text
        return html

    def soupLinkAll(self, query_url, book_name='大王饶命'):
        html = self.getHtml(query_url)
        if html is None:
            return
        soup = BeautifulSoup(html, 'html.parser')
        # a_all=soup.find_all('a',attrs={'href':re.compile("^https://www.baidu.com")})
        a_all = soup.find_all('a')
        for item in a_all:
            text_lower = item.get_text().lower()
            if text_lower.find(book_name) >= 0:
                # print(item.get_text(), item.attrs['href'])
                self.work_two_1(item.attrs['href'])

    def getIndexUrl(self, query_url, index=0):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        try:
            req = requests.get(query_url, headers=header, timeout=2)
        except:
            print(query_url)
            return None, None

        req.encoding = req.apparent_encoding
        soup = BeautifulSoup(req.text, 'html.parser')
        title_text = soup.title.get_text()
        title_url = req.url

        data = {
            'model': 'index_url',
            'index': index,
            'name': title_url,
            'title': title_text
        }
        print(self.serverSwap(data=data))

        return title_text, title_url

    def work_two_1(self, query_url):
        book_title, book_url = self.getIndexUrl(query_url)
        if book_url is None:
            return
        bese_url = urljoin(book_url, '/')
        if bese_url == book_url:
            return
        ceshi_title, ceshi_url = self.getIndexUrl(bese_url, index=1)
        print(ceshi_title, ceshi_url)
        return True

    def word_one(self, book_name='大王饶命'):
        query_url = self.baidu_url + book_name
        print(query_url)
        self.soupLinkAll(query_url, book_name=book_name)

    def run(self):
        get_book_key = self.getBookKey()
        self.word_one(get_book_key)


if __name__ == '__main__':
    book_bookkey().run()
