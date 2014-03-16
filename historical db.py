#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  historical db.py
#  
#  Copyright 2014 Shridhar Mishra <shridhar@shridhar>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from matplotlib.finance import quotes_historical_yahoo
import sqlite3
import datetime
import os
 
date1 = datetime.datetime(2014,1,1)
date2 = datetime.datetime.now()
#path = os.path.expanduser('~') + '/Dev/Data/AssetPrices/'
#path = os.getcwd() + '/Dev/Data/AssetPrices/'
#db = path + 'assetprices.db'
db = 'assetprices.db'
 
stocks = {'data':[('GOOG', 'stock'), ('AAPL','stock')],
 'headers':('ticker', 'tag')}
etfs = {'data':[('DBP', 'etf'), ('TIP','etf'),('DLS','etf'),('BND','etf'),
 ('EWC','etf'),('VBR','etf'),('RWX','etf'),('SPY','etf')],
 'headers':('ticker','tag')}
 
#Create a function to create a csv file for a given ticker.
 
def package_data(db=None, ticker=None, start=None, end=None):
 '''
 package_data() almost the same as write2csv() without the CSV section.
 It uses quotes_historical_yahoo() to create a data set for a given stock's
 price history. Date_string, Year, month, and day fields are included for
 added flexibility. Returns a dictionary of tuples.
 '''
 con = sqlite3.connect(db)
 c = con.cursor()
 sql = "select asset_id from assets where ticker='%s'" % ticker #change this!
 c.execute(sql)
 id_list = c.fetchall()
 if len(id_list)==1:
	f_key = id_list[0][0]
 else:
	print 'Error: asset has %s IDs' % str(len(key_list))
 
 raw_quotes = quotes_historical_yahoo(ticker, start, end) #list of tuples
 data = []
 for quote in raw_quotes:
	date_raw = datetime.datetime.fromordinal(int(quote[0]))
	year, month, day = date_raw.year, date_raw.month, date_raw.day
	date_string = str(year)+'-'+str(month)+'-'+str(day)
	record = (f_key, quote[0], date_string, year, month, day,
	quote[1], quote[2], quote[3], quote[4], quote[5])
	data.append(record)    
 
 headers = ('asset_id',
 'gregorian_day',
 'date_string',
 'year',
 'month',
 'day',
 'open',
 'close',
 'high',
 'low',
 'volume')
 return {'data':data, 'headers':headers}
 
def write2sqlite(db=None, table_name=None, data_dict=None):
 '''
 write2sqlite() takes a given dictionary of tuples and writes them to a
 designated sqlite database table.
 '''
 header_string = ', '.join([header for header in data_dict['headers']])
 marks = len(data_dict['headers'])*'?,'
 marks_string = marks[:-1]
 con = sqlite3.connect(db)
 c = con.cursor()
 c.executemany('insert into ' + table_name + ' (' + header_string + ') '
 'values (' + marks_string +')', data_dict['data'])
 con.commit()
 # don't forget to add 'date modified' field at some pt
 c.close()
 return
 
#Need to create a database to work with.
 
def build_database(db=None, assets=None, start=None, end=None):
 '''
 build_database() creates an sqlite database populated by stocks defined in
 the code below. Change date1 to adjust how much price history you want.
 '''
 con = sqlite3.connect(db)
 c = con.cursor()
 c.execute('''CREATE TABLE assets
 (asset_id integer not null primary key,
 ticker text,
 tag text)
 ''')
 
 c.execute('''CREATE TABLE prices
 (price_id integer not null primary key,
 asset_id integer not null,
 gregorian_day integer,
 date_string date,
 year integer,
 month integer,
 day integer,
 open real,
 close real,
 high real,
 low real,
 volume integer,
 FOREIGN KEY (asset_id) REFERENCES assets(asset_id))
 ''')
 con.commit()
 c.close()
 
 #add stocks to asset table
 write2sqlite(db=db, table_name='assets', data_dict=assets)
 
 #package price data and write to price table
 for asset in assets['data']:
	prices = package_data(db=db, ticker=asset[0], start=start, end=end)
	write2sqlite(db=db, table_name='prices', data_dict=prices)
	return
 
def remove_existing_db(path=None):
 if os.path.exists(path) == True:
	os.remove(path)
	print 'old db removed'
 else:
	pass
 
remove_existing_db(path=db)
build_database(db=db, assets=stocks, start=date1, end=date2)


def main():
	
	return 0

if __name__ == '__main__':
	main()

