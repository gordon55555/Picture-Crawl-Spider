#encoding: utf-8
"""
author:WuXupeng
email:765074575@qq.com
date:2015.6.4
verison:0.1.0
function: baidu's small picture, which is saved in the file of image
"""

import time,math,os,re,urllib,urllib2,cookielib
from bs4 import BeautifulSoup
import time


""" 自动抓取百度图片 """
class BaiduImage:
    """
    image_links     图片URL链接
    image_dir       图片存放文件夹
    current_page    当前页面地址
    next_page       下一页面地址
    image_count     已下载图片数量
    """
    
    image_links = []
    image_dir = 'image'
    current_page = ''
    next_page = ''
    image_count = 0
    
    def __init__(self):
        self.cj =cookielib.LWPCookieJar()
        try:
            self.cj.revert('baiduimage.cookie')
        except:
            None        
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)
        self.opener.addheaders = [
            ("User-agent", "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.9.1) Gecko/20090704 Firefox/3.5"),
            ("Accept", "*/*")]


    """ 得到当前页面中图片的链接地址 """
    def get_image_links(self):
        try:
            html = self.opener.open(self.current_page).read()
            #print html
        except Exception,e:
            self.write_log(e)
            return
            
        soup = BeautifulSoup(html)
        self.image_links = []
        for link in soup.findAll('img',src = re.compile(".jpg$")):
              l = dict(link.attrs)['src']
              
              self.image_links.append(l)
                
                
    """ 得到下一页地址 """
    def get_next_page(self):
        html = self.opener.open(self.current_page).read()
        soup = BeautifulSoup(html)
        spans = soup.findAll('a',href = re.compile("pos=next$"))
        for span in spans:
            self.current_page = str('http://image.baidu.com')+str(dict(span.attrs)['href'])
            self.write_log('Going next page...')
            return                

        self.write_log('This is the latest page')
        self.next_page = ''
        return False
        

    """ 下载self.image_links中的图片 """
    def download(self):
        if not self.image_links:
            return False
        print "download page : " + self.current_page
        self.write_log('Current page - %s' %self.current_page)

        for link in self.image_links:
            try:
                data = urllib.urlopen(link).read()
            except Exception,e:
                self.write_log('Connect error:%s' %e)
                return
            self.write_log('Downloading... - %s' %link)                
            file_name = str(int(time.time()))+'.jpg'
            file_path = os.path.join(self.image_dir,file_name)
            image = open(file_path,'wb')
            
            try:                
                image.write(data)
            except Exception,e:
                self.write_log('Download faild:%s' %e)
            else:
                self.write_log('Download Success!-%s' %link)
            
            self.image_count += 1
            image.close()
            del image
            time.sleep(2)

    def write_log(self,text):
        #os.system('clear')
        log = open('log.txt','a')
        log.write(text)
        log.write('\n')
        log.close()          

    
    """ 给出wap起始页开始下载 """
    def run(self,start_page):
        self.current_page = start_page

        while True:
            # 获取后下载首页图片
            self.get_image_links()
            self.download()
            self.get_next_page()
            self.write_log('Image total:%d' %self.image_count)
            time.sleep(1)
            

app = BaiduImage()
app.run(start_page="http://image.baidu.com/i?tn=wisemidresult&ie=utf8&word=%E4%BA%BA%E7%BE%A4%E5%9B%BE%E7%89%87&pn=0&rn=6&size=big&fmpage=result&pos=prev")
