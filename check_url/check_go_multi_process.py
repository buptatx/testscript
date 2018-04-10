#! /usr/bin/python
#! -*- coding:utf-8 -*-

import Queue
import time
import urllib2

from multiprocessing import Process
from multiprocessing import Queue


def check(curl_queue, bad_url_queue):
    '''
    验证url的可用性
    使用标准库中的urllib2.urlopen
    判断httpcode
    '''
    while(True):
        code = -1
        try:
            url = curl_queue.get(False)
        except Exception as e:
            break
    
        try:
            res = urllib2.urlopen(urllib2.Request(url))
            code = res.getcode()
            res.close()
        except Exception as e:
            print("[curl url]{}".format(str(e)))
    
        if code != 200:
            #将死链存入结果Queue
            bad_url_queue.put(url)


def load_data(filename):
    '''
    从文件中加载url
    @input:文件名
    @output:url列表
    '''
    curl_list = []

    with open(filename, "r") as ff:
        for line in ff:
            curl_list.append(line.strip("\r\n"))

    return curl_list

    
def store_result(url_list):
    '''
    将结果url列表写入到文件中
    @input:结果url列表
    @output:none
    ''' 
    with open("./result.txt", "w") as rf:
        rf.write("\n".join(url_list))
        rf.write("\n")
 
       
def check_entrance(filename, pNum):
    '''
    遍历死链程序入口
    @input:url存储文件名，进程数
    @output:none
    '''
    start_t = time.time()
    curl_list = load_data(filename)
    bad_url_list = []

    #initial input queue
    curl_queue = Queue()
    for item in curl_list:
        curl_queue.put(item)
    
    #initial result queue
    bad_url_queue = Queue()

    proc_list = []
    for i in range(pNum):
        p = Process(target=check, args=(curl_queue, bad_url_queue,))
        proc_list.append(p)

    #多进程遍历
    for item in proc_list:
        item.start()
        item.join()

    for idx in range(bad_url_queue.qsize()):
        bad_url_list.append(bad_url_queue.get(False))

    #conclusion
    end_t = time.time()
    time_cost = end_t - start_t

    total_url = len(curl_list)
    bad_url = len(bad_url_list)
    bad_url_rate = float(bad_url)/total_url
    conclusion = "[total url]{}[bad url]{}[bad url rate]{}[time cost]{}s".format(\
        total_url, bad_url, bad_url_rate, time_cost)
    print(conclusion)

    store_result(bad_url_list)
  

if __name__ == "__main__":
    check_entrance("./data.txt", pNum=6)
