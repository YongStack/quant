#encoding=utf-8
"""
Author: Denis Liu <liu.yong@datatom.com>
Date: Thu 25 Aug 2016 05:03:08 PM CST
Function: 
"""

import st_globals
import tushare as ts

class StockInfo():
	def __init__(self):
		pass

	def get_stock_info(self):
		info = ts.get_stock_basics()

		for index,row in info.iterrows():
			break

		return info


if __name__=="__main__":
	StockInfo().get_stock_info()
