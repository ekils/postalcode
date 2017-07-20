#coding=utf-8
import pandas as pd
from . import _chp_csv_path

def ZipCodeTW(city,district):
    city=unicode(city,'utf-8')
    district= unicode(district,'utf-8')
    r= pd.read_excel(_chp_csv_path,sheetname=u'{}'.format(city))
    print r[u'{}'.format(district)][0]
#ZipCodeTW('新北市','新店區')
