#encoding=utf-8
"""
Author: Denis Liu <yongstack@163.com>
Date: Fri 26 Aug 2016 07:28:32 AM CST
Function: 
"""
import types
import tushare as ts


class StockFilter():
	def __init__(self):
		pass

	def filter_stock_by_assets(self, stock, min = 0, max = 1500000):
		f_info = []

		for item in stock:
			if item['totals'] == 0:
				continue

			out_asset = float(item['outstanding']/item['totals']) * item['totalAssets']

			if out_asset < min or out_asset > max:
				continue

			f_info.append(item)
			
		return f_info

	def filter_stock_by_ampl(self, stock, value = 0.1):
		f_info = []

		for item in stock:
			try:
				df = ts.get_realtime_quotes(str(item['id']))
			except Exception, e:
					print "get quotes of %d failed"  % int(item['id'])
					continue

			if type(df) is types.NoneType:
				continue

			for d, x in df.iterrows():
				if abs((float(x['price']) - float(df['open'])) / float(df['pre_close'])) > abs(value) and abs((float(x['price']) - float(df['open'])) / float(df['pre_close'])) < 0.21:
					f_info.append(item)

		return f_info
