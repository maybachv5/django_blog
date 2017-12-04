# -*- coding: utf-8 -*-
import requests
import re
import json
import time
import random

class TB_WordSearch(object):
    '''淘宝搜索'''
    def __init__(self,word):
        self.word = word
        self.base_url = 'https://suggest.taobao.com/sug'
        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/57.0.2987.110 Safari/537.36',
            'referer':'https://www.taobao.com/',
        }

    def get_result(self):
        d = {
            'extras':'1',
            'code':'utf-8',
            'callback':'KISSY.Suggest.callback',
            'q':self.word
        }
        html = requests.get(self.base_url,params=d,headers=self.headers).text
        data = re.findall('callback\(({.*})\)',html)
        if data:
            data = data[0]
        else:
            data = None
        try:
            data = json.loads(data)
            results = data.get('result')
        except:
            results = None
        return results

class TM_WordSearch(object):
    '''天猫搜索'''
    def __init__(self,word):
        self.word = word
        self.baseurl = 'https://suggest.taobao.com/sug'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/57.0.2987.110 Safari/537.36',
            'referer':'https://www.tmall.com/',
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
        data = re.findall('jsonp.*?\(({.*})\)', html)
        if data:
            data = data[0]
        else:
            data = None
        try:
            data = json.loads(data)
            results = data.get('result')
        except:
            results = None
        return results

class JD_WordSearch(object):
    '''京东搜索'''
    def __init__(self,word):
        self.word = word
        self.baseurl = 'https://dd-search.jd.com/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/57.0.2987.110 Safari/537.36',
            'Host':'dd-search.jd.com',
            'Referer':'https://www.jd.com/',
        }

    def get_results(self):
        t = time.time()
        info = {
            'terminal':'pc',
            'ver':'2',
            'zip':'1',
            'key':self.word,
            't':str(int(t*1000)),
            'curr_url':'search.jd.com/Search',
            'callback':'jQuery'+str(random.randint(3432434,5444229)),
        }
        html = requests.get(self.baseurl,params=info,headers=self.headers).text
        data = re.findall('({"key".*?})',html)
        try:
            results = [json.loads(each) for each in data]
        except:
            results = None
        return results

class VIP_WordSearch(object):
    '''唯品会搜索'''
    def __init__(self,word):
        self.word = word
        self.baseurl = 'https://category.vip.com/ajax/getSuggest.php'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
            'Host':'category.vip.com',
            'Referer':'https://category.vip.com/',
        }

    def get_results(self):
        t = time.time()
        info = {
            'callback':'searchSuggestions',
            'warehouse':'VIP_NH',
            'keyword':self.word,
            '_':str(int(t*1000)),
        }
        html = requests.get(self.baseurl, params=info, headers=self.headers).text
        data = re.findall('search.*?\(({.*})\)',html)
        if data:
            data = data[0]
        else:
            data = None
        try:
            data = json.loads(data)
            results = data.get('data')
            last_results = []
            for each in results:
                product = {}
                product['word'] = each.get('word')
                product['goodscount'] = each.get('goodsCount')
                wordlist = each.get('props')
                if wordlist:
                    words = '，'.join([w.get('name') for w in wordlist])
                    product['words'] = words
                else:
                    product['words'] = ''
                last_results.append(product)
        except:
            last_results = None
        return last_results

if __name__ == '__main__':
    word = '机械键盘'
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

    jd = JD_WordSearch(word)
    print('京东结果：')
    jj = jd.get_results()
    for m in jj:
        print(m)

    vip = VIP_WordSearch(word)
    print('唯品会结果：')
    vv = vip.get_results()
    for v in vv:
        print(v)
