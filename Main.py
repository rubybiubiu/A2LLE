from getaddressfromE import getAddresslist
from A2L import BaiDuMapAPI
from InputLoction2Excel import inputloation2excel
#x ，经度，纬度   z为status的值，0表示成功返回结果，其他值，表示失败
#当客户输入不友好的地理位置，或者非法的地址。要把结果反馈给客户，以便更改。
filename=input('请输入文件地址：')
addresslist=getAddresslist.getaddresslist(filename)
addrlst=[]
for adlst in addresslist:
    adlst.extend(BaiDuMapAPI.address2LngLat(adlst[0]))
    addrlst.append(adlst)
inputloation2excel.inputloction2excel(filename,addrlst)
#识别excel表头
#处理完成后，自动打开结果文件