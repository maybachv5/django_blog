# -*- coding: utf-8 -*-
import requests
import re
import json
import time

class TB_WordSearch(object):
    def __init__(self,word):
        self.word = word
        self.base_url = 'https://suggest.taobao.com/sug'
        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/57.0.2987.110 Safari/537.36',
            'host':'suggest.taobao.com',
        }

    def get_result(self):
        d = {
            'extras':'1',
            'code':'utf-8',
            'callback':'KISSY.Suggest.callback',
            'q':self.word
        }
        html = requests.get(self.base_url,params=d,headers=self.headers).text
        data = re.findall('callback\(({.*})\)',html)[0]
        data = json.loads(data)
        results = data.get('result')
        return results

class TM_WordSearch(object):
    def __init__(self,word):
        self.word = word
        self.baseurl = 'https://suggest.taobao.com/sug'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/57.0.2987.110 Safari/537.36',
        }

    def get_result(self):
        t = str(time.time()).replace('.', '')
        k = '{}_{}'.format(t[0:13], t[-5:-1])
        data = {
            'code':'utf-8',
            'q':self.word,
            '_ksTS':k,
            'callback':'jsonp{}'.format(int(t[-5:-1])+1),
            'area':'b2c',
            'code':'utf-8',
            'k':'1',
            'bucketid':'18',
            'src':'tmall_pc'
        }
        html = requests.get(self.baseurl,params=data,headers=self.headers).text
        data = re.findall('jsonp.*?\(({.*})\)', html)[0]
        data = json.loads(data)
        results = data.get('result')
        return results

if __name__ == '__main__':
    word = '键盘'
    tb = TB_WordSearch(word)
    b = tb.get_result()
    print('淘宝结果：')
    for j in b:
        print(j)
    tm = TM_WordSearch(word)
    print('天猫结果：')
    t = tm.get_result()
    for i in t:
        print(i)