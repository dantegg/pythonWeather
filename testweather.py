#coding:utf-8
import string
import re
import urllib2

class getWeather():
    def __init__(self):
        self.urlpath = 'http://www.weather.com.cn/weather1d/101020100.shtml'
        #self.urlpath = 'http://sh.weather.com.cn'

    def get_page(self):
        request = urllib2.Request(self.urlpath)
        response = urllib2.urlopen(request).read().decode("utf-8")
        #print response
        #print "============"
        return response
    def find_temp(self,web):
        print 'start find temperature'
        #current_temperature = re.findall(r'<dl><dd>(.*?)</dd></dl>', web, re.S)
        current_temperature = re.findall(r'<div.*?class="tem">(.*?)</div>', web, re.S)
        #current_temperature = re.findall(r'<div.*?class="tem"><span>(.*?)</span></div>', web, re.S)

        return current_temperature
    def get_temp(self):
        finaltemp =[]
        while True:
            web = self.get_page()
            webdom = self.find_temp(web)
            if len(webdom):
                finaltemp = webdom
                break
        #print finaltemp
        return finaltemp

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
    getpage = weather_spider.get_temp()
    print "get page success"
    for x in getpage:
        print x.encode('utf-8')



if __name__ == '__main__':
    main()
