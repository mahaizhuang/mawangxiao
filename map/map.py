# /bin/python
import requests
import json
import os 
import sys
import math
#
class ssh1(object):
        def __init__(self,file1):
             self.file2 = file1
             key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.file2)
             with open(key_path, 'r', encoding='utf-8') as f:
                key = f.read()
                print(key)
                self.key1 = key
        def run_poi2(self,keywords1,region1):
            url1 = 'https://restapi.amap.com/v5/place/text?parameters'
            params1={
            'key':self.key1,
            'keyworlds':keywords1,
            'region':region1,
            'output':'json'
            }
            result1= requests.get(url1,params1)
            result1 = result1.json()
            print (result1)
        def run_geocode(self,address2,city2):
            url2 = 'https://restapi.amap.com/v3/geocode/geo?parameters'
            params2={
                'key':self.key1,
                'address':address2,
                'city':city2,
                'output':'json'
                }
            result2 = requests.get(url2,params2)
            result2 = result2.json()
            print (result2)
#
if __name__ == '__main__':
    a=ssh1("user-key.txt")
    a1 = a.run_poi2("沙县小吃","杭州")
    #a2 = a.run_geocode("五金机电城","郑州")
#

