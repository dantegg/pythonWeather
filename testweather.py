#coding:utf-8
import string
import re
import urllib2
from bs4 import BeautifulSoup
import six
import html5lib
from selenium import webdriver


class getWeather():
    def __init__(self):
        self.urlpath = 'http://www.weather.com.cn/weather1d/101020100.shtml'
        #self.urlpath = 'http://sh.weather.com.cn'

    def get_page(self):
        #request = urllib2.Request(self.urlpath)
        #html_doc = request.read()
        page = urllib2.urlopen(self.urlpath)
        html_doc = page.read()
        driver = webdriver.PhantomJS(executable_path='../phantomjs-2.1.1-macosx/bin/phantomjs')
        driver.get(self.urlpath)
        #print html_doc
        #print driver.page_source
        html_doc = driver.page_source
        driver.quit()
        print '====================='
        #response = urllib2.urlopen(request).read().decode("utf-8")
        #print response
        #print "============"
        response = BeautifulSoup(html_doc,"html5lib")
        print 'get response'
        return response
    def find_temp(self,web):
        print 'start find temperature'
        #current_temperature = re.findall(r'<dl><dd>(.*?)</dd></dl>', web, re.S)
        #current_temperature = re.findall(r'<div.*?class="tem">(.*?)</div>', web, re.S)
        #current_temperature = re.findall(r'<div.*?class="tem"><span>(.*?)</span></div>', web, re.S)
        #web.div['class']='sk'
        spanlist = []
        for i in web.find_all('div',class_='tem'):
            for x in i.find_all('span'):
                spanlist.append(x.string)
            #print span

        return spanlist
    # def get_temp(self):
    #     finaltemp =[]
    #     while True:
    #         web = self.get_page()
    #         webdom = self.find_temp(web)
    #         if len(webdom):
    #             finaltemp = webdom
    #             break
    #     #print finaltemp
    #     return finaltemp

def main():
    print """
        ###############################
            爬取本市天气
            Author: dantegg_zhang
            Version: 0.0.1
            Date: 2016-10-12
        ###############################
    """
    weather_spider = getWeather()
    getpage = weather_spider.get_page()
    getdom = weather_spider.find_temp(getpage)
    print 'the temperature now is /现在的温度是 %s '%(getdom[0].encode('utf-8'))
    #print getdom[0]
    # getpage = weather_spider.get_temp()
    # print "get page success"
    # for x in getpage:
    #     print x.encode('utf-8')



if __name__ == '__main__':
    main()
