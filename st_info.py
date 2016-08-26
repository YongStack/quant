#encoding=utf-8
"""
Author: Denis Liu
Date: Thu 25 Aug 2016 05:03:08 PM CST
Function: 
"""

import json
import tushare as ts
import st_globals


dump_file = "/tmp/.stock"

class StockInfo():
	def __init__(self):
		pass

	def _get_stock_info(self):
		s_info = []
		info = ts.get_stock_basics()

		for index,row in info.iterrows():
			s_detail  = {}
			s_detail['id'] = index
			s_detail['name'] = row['name']
			s_detail['pe'] = row['pe']
			s_detail['pb'] = row['pb']
			s_detail['outstanding'] = row['outstanding']
			s_detail['totals'] = row['totals']
			s_detail['totalAssets'] = row['totalAssets']

			s_info.append(s_detail)

		return s_info 

	def dump_stock_info(self):
		s_info = self._get_stock_info()

		if len(s_info) > 0: 
			with open(dump_file, 'w') as f:
				f.write(json.dumps(s_info))

		return

	def load_stock_info(self):
		f = open(dump_file, 'r')

		s_info =json.load(f)

		f.close

		return s_info

if __name__=="__main__":
	#StockInfo().dump_stock_info()
	info = StockInfo().load_stock_info()
	print len(info), info[0]['id'], info[0]['name']
