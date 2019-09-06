import pymysql, re, datetime
import pandas as pd
import numpy as np

class DBOperate():
	def __init__(self, host='localhost', port=3306, user='root', password='root', database='', charset='utf8'):
		self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset=charset)
		self.cursor = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

	def __enter__(self):
		return self.cursor

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.conn.commit()
		self.cursor.close()


def Extract(host, user, password, database):
	with DBOperate(host=host, user=user, password=password, database=database) as DB:
		sql = "show tables"
		DB.execute(sql)
		result = {}
		tables = DB.fetchall()
		for i in tables:
			tablename = i["Tables_in_"+database]
			desc_sql = "desc %s" % tablename
			DB.execute(desc_sql)
			table_desc = DB.fetchall()
			select_sql = "select * from %s" % tablename
			DB.execute(select_sql)
			table_data = DB.fetchall()
			if table_data == ():
				table_data = {}
			result[tablename] = {"desc":table_desc,"value":table_data}

	return result


def createsql(tablename, desc):
	sql = "create table %s(" % tablename
	for i in range(0,len(desc)):
		field = "%s %s "%(desc[i]["Field"], desc[i]["Type"])
		if desc[i]["Null"]=="No":
			field += "NOT NULL"
		elif desc[i]["Key"]=="PRI":
			field += "primary key "
		elif desc[i]["Default"]:
			field += "DEFAULT %s " % str(desc[i]["Default"])
		if i == len(desc)-1:
			field += desc[i]["Extra"]
		else:
			field += desc[i]["Extra"] + ","
		sql += field
	return sql + ")"


def insertsql(tablename, desc):
	mapping = ",".join(["%s" for i in desc])
	sql = "insert into %s values(%s)" % (tablename, mapping)
	return sql



def LoadData(data, host, user, password, database):
	with DBOperate(host=host, user=user, password=password, database=database) as DB:

		for tablename in data:

			sql = "drop table if exists %s" % tablename
			DB.execute(sql)
			create_sql = createsql(tablename, data[tablename]["desc"])
			DB.execute(create_sql)

			value = data[tablename]["value"]


			if value:
				for item in value:
					for k, v in item.items():
						if type(item[k]) == datetime.datetime:
							item[k] = str(item[k])
				insert_data = tuple([tuple(i.values()) for i in value])
				insert_sql = insertsql(tablename, data[tablename]["desc"])
				print("insert table: %s" % tablename)
				DB.executemany(insert_sql, insert_data)




if __name__ == '__main__':

	# 提取数据与表结构
	remote_host = input("remote host: ")
	remote_user = input("remote user: ")
	remote_password = input("remote password: ")
	remote_database = input("remote database: ")

	row_data = Extract(host=remote_host, user=remote_user, password=remote_password, database=remote_database)
	if row_data:
		print("extract done.")
		local_host = input("local host: ")
		local_user = input("local user: ")
		local_password = input("local password: ")
		local_database = input("local database: ")
		result = LoadData(row_data, host=local_host, user=local_user, password=local_password, database=local_database)
	else:
		print("extract failed.")