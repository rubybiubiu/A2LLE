from A2L import BaiDuMapAPI
#x ，经度，纬度   z为status的值，0表示成功返回结果，其他值，表示失败
#当客户输入不友好的地理位置，或者非法的地址。要把结果反馈给客户，以便更改。
address=input('请输入地址：')
x,y,z=BaiDuMapAPI.address2LngLat(address)
if z==0:
    print(address,'的经度是：%s，维度是：%s'%(x,y))
else:
    print (z)
