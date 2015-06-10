##################################################################
#author   : Wuxupeng                                             #
#date     : 2015.6.6                                             #
#function : Crawl the crowd picture in four websit               #
#         : baidu, bing , haosou , soso                          #
##################################################################

from selenium import webdriver
import time
import urllib
import cPickle
import os
import socket

class Crawl(object):
    '''
    class for Crawl
    '''
    def __init__(self,name,num,url,pic_xpath,next_xpath):
        self.name = name
        self.global_num = 0
        self.url        = url
        self.num        = num
        self.pic_xpath  = pic_xpath
        self.next_xpath = next_xpath
        self.driver     = webdriver.Firefox()
        self.ISOTIMEFORMAT='%Y-%m-%d %X'

    def write_log(self,add,text):
        #os.system('clear')
        log = open(add +'log.txt','a')
        log.write(text)
        log.write('\n')
        log.close()
 
    def get_url(self):
        img_url_dic = {}
        #driver.maximize_window()
        self.driver.get(self.url)
        tem = self.num
        tem_url = []
 
        for i in range(tem):
            i = i + 1 
            print "skip :" + str(i) +"!"
            try:
                self.driver.find_element_by_xpath( self.next_xpath ).click()
            except Exception as err:
                print "end"
                break
            time.sleep(1)
            for element in self.driver.find_elements_by_xpath(self.pic_xpath):
                img_url = element.get_attribute('src')
                if img_url != None and not img_url_dic.has_key(img_url):
                    tem_url.append(img_url)
                    img_url_dic[img_url] = ''
        f0 = open('./link/' + self.url[-10:-1]+'.pkl','wb')
        cPickle.dump(tem_url,f0)
        f0.close()
        self.driver.close()

    def crawl(self):
        f0 = open('./link/' + self.url[-10:-1]+'.pkl','rb')
        tem_url = cPickle.load(f0)
        f0.close()
        tim =  time.strftime( self.ISOTIMEFORMAT, time.localtime( time.time() ) )
        path ='./link/'
        title = tim
        new_path = os.path.join(path, self.url[-10:-1]+'+'+title)
        if not os.path.isdir(new_path):
            os.makedirs(new_path)

        self.write_log(new_path+r'/', 'the '+self.name + ' picture url of file:')
        self.write_log(new_path+r'/', self.url[-10:-1]+'.pkl')
        self.write_log(new_path+r'/', 'The full address :')
        self.write_log(new_path+r'/', self.url)

        i = 1
        for url in tem_url:
            if i % 20 == 0:
                print "Have crawl :" + str(i) + ".."
                self.write_log(new_path+r'/', "Have crawl :" + str(i) + "..")
            self.global_num += 1
            ext = url.split('.')[-1]
            filename = str(self.global_num) + '.' + ext
            try:
                #$socket.setdefaulttimeout(10)
                time.clock()                   
                data = urllib.urlopen(url).read()
                time.sleep(3)
                text = "Crawl this picture need :" + str(time.clock()) +" s"
                f = open(new_path+r'/'+filename, 'wb')

                self.write_log(new_path+r'/', text)
                print text
                f.write(data)
                f.close()
            except Exception as err:
                    print "error, this link will be skipped!"
                    continue
            i = i+1
            self.write_log(new_path+r'/'," the num of picture is:"+str(i))
    
    

if __name__ == '__main__':
    #crawl the crowd.
    #the picture's xpath
    xpath_pic_baidu_crowd  = '//div[@class="img-wrapper"]/img'
    xpath_pic_bing_crowd   = '//img[@class="mainImage"]'
    xpath_pic_haosou_crowd = '//img[@class="lb_mainimg"]'
    xpath_pic_soso_crowd   =  "//div[@class='img-box']/img" 
    #the next xpath
    xpath_next_baidu_crowd  = "//span[@class='img-next']/span[@class='img-switch-btn']"
    xpath_next_bing_crowd   = "//div[@id='iol_imp']/div[@id='iol_navr']"
    xpath_next_haosou_crowd = "//a[@id='lbNext']/span"
    xpath_next_soso_crowd   =  "//div[@id='main']/a[@id='btnPgRgt']"
    #the init path
    url_baidu = 'http://image.baidu.com/search/detail?ct=503316480&z=0&tn=baiduimagedetail&ipn=d&word=%E6%8B%A5%E6%8C%A4&step_word=&pn=0&spn=0&di=102119431040&pi=&rn=1&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=25039&cl=2&lm=-1&st=-1&cs=3218680428%2C596206273&os=2672960856%2C1828828546&adpicid=0&ln=1000&fr=%2C&fmq=1433828108535_R&ic=0&s=undefined&se=&sme=0&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&objurl=http%3A%2F%2Fi11.topit.me%2Fo%2F201007%2F18%2F12794430396410.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bp5rtp_z%26e3B4jAzdH3Ftpj4AzdH3Fcmam8n' 
    url_bing  = 'http://cn.bing.com/images/search?q=crowd&view=detailv2&&qft=+filterui%3aphoto-photo&id=B7922F9177ABE1201A28BAA6D3779D8610BEA8DC&selectedIndex=0&ccid=1a4Rp3%2bN&simid=608011118798048245&thid=JN.RW5tk%2fs0hR%2fz4yXJZp1DGg&ajaxhist=0'
    url_haosou = 'http://image.haosou.com/v?q=%E6%8B%A5%E6%8C%A4&src=srp&fromurl=http%3A%2F%2Fnews.sina.com.cn%2Fc%2Fp%2F2009-02-15%2F134617219043.shtml#q=%E6%8B%A5%E6%8C%A4&src=srp&fromurl=http%3A%2F%2Fnews.sina.com.cn%2Fc%2Fp%2F2009-02-15%2F134617219043.shtml&lightboxindex=0&id=c597d21787aa5d42275fddddd5c406eb&multiple=0&itemindex=0&dataindex=0'
    url_soso = 'http://pic.sogou.com/d?query=%D3%B5%BC%B7%C8%CB%C8%BA&mood=0&picformat=0&mode=1&di=0&did=1#did0'
    #the number of picture will be crawled.
    n = 3
    #baidu
    tem = Crawl( "baidu" , n , url_baidu , xpath_pic_baidu_crowd , xpath_next_baidu_crowd)
    tem.get_url()
    tem.crawl()
    #haosou
    tem = Crawl( "haosou", n , url_haosou , xpath_pic_haosou_crowd , xpath_next_haosou_crowd)
    tem.get_url()
    tem.crawl()
    #soso
    tem = Crawl( "soso"  , n , url_soso , xpath_pic_soso_crowd , xpath_next_soso_crowd)
    tem.get_url()
    tem.crawl()   
    #bing
    tem = Crawl( "bing"  , n , url_bing , xpath_pic_bing_crowd , xpath_next_bing_crowd)
    tem.get_url()
    tem.crawl()
