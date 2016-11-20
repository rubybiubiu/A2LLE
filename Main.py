from GetAddressFromExcel import DealWtihAddressFromExcel
#x ，经度，纬度   z为status的值，0表示成功返回结果，其他值，表示失败
#当客户输入不友好的地理位置，或者非法的地址。要把结果反馈给客户，以便更改。
filename=input('请输入文件地址：')
DealWtihAddressFromExcel.DealWithExcel(filename)
