#coding=utf-8
import pandas as pd

def ZipCodeTW(city,district):
    city=unicode(city,'utf-8')
    district= unicode(district,'utf-8')
    r= pd.read_excel("zip_code.xlsx",sheetname=u'{}'.format(city))
    print r[u'{}'.format(district)][0]
#ZipCodeTW('新北市','新店區')
