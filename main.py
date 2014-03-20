import weipai_api
import sqlite3
import sys
import os
import dbhelper
import math

curdir = os.path.dirname(sys.argv[0])
os.chdir(curdir)

DB_PATH = 'weipai.db'

def initialize(user_id):
	user = weipai_api.get_user_info(user_id)
	dbhelper.save_user(user)
	if 'videos' in user and len(user['videos']) > 0:
		videos = user['videos']
		dbhelper.save_videos(user_id, videos)
	video_count = user['videos_count']
	dbhelper.commit()
	print('video count: ' + str(video_count))
	if video_count and video_count > 15:
		print('total page: ' + str(math.ceil(video_count / 15)))
		for i in range(math.ceil(video_count / 15)):
			page = i + 1
			print('page: ' + str(page))
			videos = weipai_api.get_more_videos(user_id, page)
			print('more videos: ' + str(len(videos)))
			if len(videos) > 0:
				dbhelper.save_videos(user_id, videos)
	dbhelper.commit()
	captured_videos_count = dbhelper.get_videos_count(user_id)
	dbhelper.update_uids_info(user_id, True, captured_videos_count)
	dbhelper.commit()
	
def capture(user_id):
	print('capture: ' + user_id)

def main():
	dbhelper.open(DB_PATH)
	data = dbhelper.get_uids()
	for row in data:
		user_id = row[0]
		initialized = row[1]
		if not initialized:
			initialize(user_id)
		else:
			capture(user_id)
	dbhelper.close()
	print('done!')

if __name__ == '__main__':
	main()