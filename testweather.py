#coding:utf-8
import string
import re
import urllib2

class getWeather():
    def __init__(self):
        #self.urlpath = 'http://www.weather.com.cn/weather40d/101020100.shtml'
        self.urlpath = 'http://sh.weather.com.cn'

    def get_page(self):
        request = urllib2.Request(self.urlpath)
        response = urllib2.urlopen(request).read().decode("utf-8")
        return response
    def find_temp(self,web):
        print 'start find temperature'
        current_temperature = re.findall(r'<dl><dd>(.*?)</dd></dl>', web, re.S)
        #current_temperature = re.findall(r'<div.*?class="tem">(.*?)</div>', web, re.S)
        print "========="
        print type(current_temperature)
        print "========="
        print current_temperature[0].encode('utf-8')

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
    print "get page success"
    weather_spider.find_temp(getpage)



if __name__ == '__main__':
    main()
