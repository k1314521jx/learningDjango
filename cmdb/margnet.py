#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年8月13日
@author: DontinstallB凯
'''
import requests
import re
import time
import os,sys

text_data = []
def get_magnet(search):

    avgril_name = search
    # os.system('cls') 
    # print('正在搜索%s相关信息....[ctrl+c]停止搜索'%avgril_name)
    num =1
    r = requests.get('http://www.btcar.net/search/'+avgril_name+'_ctime_'+ str(num) +'.html')
    # print("正在获取第[%d]页数据..."%num)
    regx = r'/[0-9A-Z]{10}[\S]*\.html'
    pattern = re.compile(regx)
    get_url = re.findall(pattern,r.text)
    if get_url==[]:
        return 'No data'
        # return get_magnet()
    else:
        for i in get_url:
            #time.sleep(1);
            rr = requests.get('http://www.btcar.net' + i)
            regx_tar = r'magnet:[?]xt=urn:btih:[A-Z0-9]{40}' 
            re_name = r'<h1 class="T1">[\s|\S]*</h1>'  #匹配标题
            pattern_tar = re.compile(regx_tar)
            pattern_name = re.compile(re_name)
            get_targ = re.findall(pattern_tar,rr.text)
            get_name = re.findall(pattern_name,rr.text)
            try:
                # get_name[0][15:len(get_name[0])-5] + ':' +
                text = get_name[0][15:len(get_name[0])-5] + '\n' + get_targ[0]
                # print(get_name[0][15:len(get_name[0])-5]) #字符串切割
                # print(get_targ[0])
                text_data.append(text)
                
            except UnicodeEncodeError:
                continue
    return text_data
if __name__ == '__main__':
    print(get_magnet('西游记'))
