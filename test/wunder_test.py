import urllib.request as urllib2
from http import cookiejar


cookieJar = cookiejar.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))

set_url = "http://www.wunderground.com/cgi-bin/findweather/getForecast?setpref=SHOWMETAR&value=1"
request = urllib2.Request(set_url)
response = opener.open(request)

url = "http://www.wunderground.com/history/airport/KBUF/2011/1/1/DailyHistory.html?theprefset=SHOWMETAR&theprefvalue=1&format=1"
request = urllib2.Request(url)
page = opener.open(request)
# print(page.info())
dailyData = page.read()
print(dailyData)
