
from bs4 import BeautifulSoup
import requests
import json
import re



class work_book():
    def __init__(self):
        self.server_url='http://oa.9oe.com/index.php/book/apibook'
        self.baidu_url='https://www.baidu.com/s?wd='


    def getHtml(self,query_url):
        header={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        req = requests.get(query_url,headers=header)
        req.encoding=req.apparent_encoding
        if req.status_code==200:
            return req.text
        print(req.text)
        return

    def getBookKey(self):
        book_key=''

        data={
            'model':'book_key_get',
        }
        req=requests.post(url=self.server_url,data=data)
        html=req.text
        json_data=json.loads(html)
        book_key=json_data['data']
        print(book_key['book_key'])
        return book_key['book_key']

    def soupLinkAll(self,query_url):
        html=self.getHtml(query_url)
        if html is None:
            return
        soup = BeautifulSoup(html, 'html.parser')
        #a_all=soup.find_all('a',attrs={'href':re.compile("^https://www.baidu.com")})
        a_all = soup.find_all('a')
        for item in a_all:
            text_lower=item.get_text().lower()
            if text_lower.find('aaaa')>=0:
                #print(item)
                print(item.get_text(),item.attrs['href'])




    def word_one(self):
        query_url=self.baidu_url+self.getBookKey()
        #work_html=self.getHtml(query_url)
        print(query_url)
        self.soupLinkAll(query_url)

        #print(work_html)




if __name__ == '__main__':
    work_book().word_one()