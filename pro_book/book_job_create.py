# -*- coding: utf-8 -*-
import requests

joburl = 'https://www.biquta.com/{cate}_{subcate}/'

serverUrl = 'http://oa.9oe.com/index.php/book/apibook/job_append'


# serverUrl='http://www.123.com/index.php/book/apibook/job_append'


def job_append(data):
    req = requests.post(serverUrl, data=data)
    print(req.text)


for i in range(1, 3):
    for j in range(1, 999999):
        abc = joburl
        abc = abc.replace('{cate}', str(i))
        abc = abc.replace('{subcate}', str(j))
        print(abc)
        data = {
            'url': abc,
        }
        job_append(data)
