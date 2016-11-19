#coding：utf-8
#author：ruby
#Date:2016-11-19 15:07:05
#Feature：通过百度地图提供的API服务，把地址转化为经纬度
#           （http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding）
#Remark：str urllib.parse.quote  resquests.get
#       output=json/xml 此处用的是json，xml尚未处理 、
#       callback 用于javascript，此处不需要用，不然json.loads无法处理（回调函数）

import json
import requests
import urllib
def address2LngLat(address):
    pp=urllib.parse.quote(address)
    resp=requests.get("http://api.map.baidu.com/geocoder/v2/?address="+str(pp)+"&output=json&ak=oVaH0a1fHXnOS4MopuwmOoog")
#html=urlopen("http://api.map.baidu.com/geocoder/v2/?address=北京市海淀区上地十街10号&output=json&ak=oVaH0a1fHXnOS4MopuwmOoog&callback=showLocation")
    resp1=json.loads(resp.content.decode('utf-8'))
    if resp1.get('status')==0:
        lng=resp1['result']['location'].get('lng')
        lat=resp1['result']['location'].get('lat')
        return lng, lat,0
    else:

        return 0,0,resp1['msg']



