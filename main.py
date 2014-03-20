import weipai_api
import sqlite3
import sys
import os

curdir = os.path.dirname(sys.argv[0])
os.chdir(curdir)

DB_PATH = 'weipai.db'

def initialize(user_id):
	print('initialize: ' + user_id)

def capture(user_id):
	print('capture: ' + user_id)

def main():
	sql = 'SELECT [id],[initialized] FROM uids;'
	conn = sqlite3.connect(DB_PATH)
	csr = conn.cursor()
	csr.execute(sql)
	data = csr.fetchall()
	for row in data:
		user_id = row[0]
		initialized = row[1]
		if not initialized:
			initialize(user_id)
		else:
			capture(user_id)

if __name__ == '__main__':
	main()