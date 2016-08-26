#encoding=utf-8
"""
Author: Denis Liu <yongstack@163.com>
Date: Fri 26 Aug 2016 07:41:23 AM CST
Function: 
"""

import sys
from st_info import StockInfo
from st_filter import StockFilter


def dump_head_stock(info):
	print "Total counts: %d" % len(info)
	for i in range(0, 10):
		if len(info) != 0 and i < len(info):
			print "\t", info[i]['id'], info[i]['name']


def do_choose_target_stock():
	all_stock = StockInfo().load_stock_info()

	f_stock = StockFilter().filter_stock_by_assets(all_stock, 0, 1200000)

	f_stock = StockFilter().filter_stock_by_ampl(f_stock, 0.11)

	dump_head_stock(f_stock)



if __name__=="__main__":
	do_choose_target_stock()
