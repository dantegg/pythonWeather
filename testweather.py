#coding:utf-8
import string
import re
import urllib2
from bs4 import BeautifulSoup
import six
import html5lib
from selenium import webdriver
import datetime


class getWeather():
    def __init__(self):
        self.urlpath = 'http://www.weather.com.cn/weather1d/101020100.shtml'
        #self.urlpath = 'http://sh.weather.com.cn'

    def get_page(self):
        #request = urllib2.Request(self.urlpath)
        #html_doc = request.read()
        page = urllib2.urlopen(self.urlpath)
        html_doc = page.read()
        driver = webdriver.PhantomJS(executable_path='../phantomjs/bin/phantomjs')
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
    def find_time(self,web):
        print 'start find time'
        timelist = []
        for i in web.find_all('p',class_='time'):
            for x in i.find_all('span'):
                timelist.append(x.string)
        return timelist
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
            Version: 0.0.2
            Date: 2016-10-13
        ###############################
    """
    weather_spider = getWeather()
    getpage = weather_spider.get_page()
    getdom = weather_spider.find_temp(getpage)
    gettime = weather_spider.find_time(getpage)
    now = datetime.datetime.now()
    timeStyle = now.strftime("%Y-%m-%d %H:%M:%S")
    print 'current system time is(当前系统时间是):%s'%timeStyle
    print 'the time is(温度采集时间是):%s'%(gettime[0].encode('utf-8'))
    print 'the temperature is /采集温度是 %s '%(getdom[0].encode('utf-8'))
    #print getdom[0]
    # getpage = weather_spider.get_temp()
    # print "get page success"
    # for x in getpage:
    #     print x.encode('utf-8')



if __name__ == '__main__':
    main()
