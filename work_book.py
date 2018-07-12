

import requests
import json



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

    def word_one(self):
        query_url=self.baidu_url+self.getBookKey()
        work_html=self.getHtml(query_url)

        print(work_html)




if __name__ == '__main__':
    work_book().word_one()