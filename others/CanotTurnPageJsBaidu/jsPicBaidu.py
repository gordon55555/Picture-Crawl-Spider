'''
    sorry to say: this version can not be run well.
'''

import time,math,os,re,urllib,urllib2,cookielib
    #from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import time

import json,socket  
import random,os  
import sys,datetime  
      
starttime = datetime.datetime.now()  
socket.setdefaulttimeout(10)   
dir ='/root/reptile/pic/'  
if not os.path.isdir(dir):  
    os.mkdir(dir)  
i=0  
j=1  
p=30  
while i<10:  
          
    if i%2==0:  
        zipname = 'baiduzip_'+str(i)+'.zip'  
        print 'make a zip file'  
        os.system('zip -6qrm /root/reptile/'+zipname+' /root/reptile/pic/*')  
        print zipname+' file is ok!' 
        url = "http://image.baidu.com/i?tn=baiduimage&ct=201326592&lm=-1&cl=2&word=%B9%E3%B3%A1%C8%CB%C8%BA%CD%BC%C6%AC&fr=ala&ala=2"
        #url = "http://image.baidu.com/i?ct=503316480&z=0&tn=baiduimagedetail&ipn=d&word=%E5%B9%BF%E5%9C%BA%E4%BA%BA%E7%BE%A4&step_word=&pn=0&spn=0&di=31145830320&pi=&rn=1&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=273&cl=2&lm=-1&st=-1&cs=2464798593%2C1293171584&os=751438383%2C1141025444&adpicid=0&ln=1996&fr=%2C&fmq=1433401874615_R&ic=0&s=undefined&se=1&sme=0&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&objurl=http%3A%2F%2Ft.jxcn.cn%2Fimages%2Ftopic%2F5%2F8%2F159675_o.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fp_z%26e3B3xvg_z%26e3BvgAzdH3Fp5rtvAzdH3Fcnn9ma" 
        #http://image.baidu.com/i?tn=listjson&word=liulan&oe=utf-8&ie=utf8&tag1=%E6%90%9E%E7%AC%91&tag2=%E5%85%A8%E9%83%A8&sorttype=0&pn=30&rn=60&requestType=1&1357639151100  
        #url ='http://image.baidu.com/i?tn=listjson&word=liulan&oe=utf-8&ie=utf8&tag1=%E6%91%84%E5%BD%B1&tag2=%E5%85%A8%E9%83%A8&sorttype=0&pn='+str(p*i)+'&rn=60&requestType=1&'+str(random.random())  "
        print url      
    try:  
        ipdata = urllib.urlopen(url).read()  
        print ipdata
    except IOError,e:  
        #if e.message=="time out":  
        print('img %s_%s is false1' % (i,j) )  
        break  
    else:     
        ipdata1 = json.loads(ipdata)  
        if ipdata1['data']:  
            for n in ipdata1['data']:  
                if n and n['obj_url']:  
                    try:  
                        dataimg = urllib.urlopen(n['obj_url']).read()  
                    except IOError,e:  
                        #if e.message=="time out":  
                        print('img %s_%s is false2' % (i,j) )  
                        break  
                    else:                     
                        fPostfix = os.path.splitext(n['obj_url'])[1]  
                        if (fPostfix == '.png' or fPostfix == '.jpg' or fPostfix == '.PNG' or fPostfix == '.JPG'):  
                            filename = dir+os.path.basename(n['obj_url'])  
                        else:  
                            filename = dir+os.path.basename(n['obj_url'])+'.jpg'  
                        try:  
                            file_object = open(filename,'w')  
                            file_object.write(dataimg)  
                            file_object.close()  
                        except socket.timeout,e:  
                            #if e.message=="timed out":  
                            print('img %s_%s is false3' % (i,j) )  
                            break  
                        else:  
                            #urllib.urlretrieve(n['obj_url'],filename)  
                            print('img %s_%s is ok' % (i,j) )  
                            j +=1  
        else:  
            break  
    i +=1     
endtime = datetime.datetime.now()  
print (endtime-starttime).seconds  
os.system('zip -6qrm /root/reptile/pic_'+str(i)+'.zip /root/reptile/pic/*')  
sys.exit()  
