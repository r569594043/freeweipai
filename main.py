import weipai_api
import sqlite3
import sys
import os
import dbhelper
import math
import logging, logging.config
import time

curdir = os.path.dirname(sys.argv[0])
os.chdir(curdir)

DB_PATH = 'weipai.db'
LOG_CONFIG = 'weipai.conf'

def capture(user_id):
	logger.debug('get user info: ' + user_id)
	user = weipai_api.get_user_info(user_id)
	dbhelper.save_user(user)
	logger.debug('save user info: ' + user_id)
	if 'videos' in user and len(user['videos']) > 0:
		videos = user['videos']
		dbhelper.save_videos(user_id, videos)
		logger.debug('save user {0} latest videos: {1}'.format(user_id, len(videos)))
	dbhelper.commit()
	return user

def initialize(user_id):
	user = capture(user_id)
	video_count = user['videos_count']
	logger.debug('user {0} total videos count: {1}'.format(user_id, video_count))
	if video_count and video_count > 15:
		logger.debug('user {0} total page: {1}'.format(user_id, math.ceil(video_count / 15)))
		for i in range(1, math.ceil(video_count / 15)):
			page = i + 1
			logger.debug('user {0} more videos page: {1}'.format(user_id, page))
			videos = weipai_api.get_more_videos(user_id, page)
			logger.debug('user {0} more videos count: {1}'.format(user_id, len(videos)))
			if len(videos) > 0:
				dbhelper.save_videos(user_id, videos)
	dbhelper.commit()
	captured_videos_count = dbhelper.get_videos_count(user_id)
	logger.debug('user {0} captured videos count: {1}'.format(user_id, captured_videos_count))
	dbhelper.update_uids_info(user_id, True, captured_videos_count)
	logger.debug('update user {0} infomation'.format(user_id))
	dbhelper.commit()

def init():
	global logger
	logging.config.fileConfig(LOG_CONFIG)
	logger = logging.getLogger("weipai")

def main():
	init()
	while True:
		dbhelper.open(DB_PATH)
		logger.info('start capture...')
		try:
			uids = dbhelper.get_uids()
			logger.debug('get uids: ' + str(len(uids)))
			for row in uids:
				try:
					user_id = row[0]
					initialized = row[1]
					if not initialized:
						logger.debug('start initial: ' + user_id)
						initialize(user_id)
						logger.debug('end initial: ' + user_id)
					else:
						logger.debug('start capture: ' + user_id)
						capture(user_id)
						logger.debug('end capture: ' + user_id)
				except Exception as ex:
					logger.exception('error during get user videos: ' + user_id)
			
		except Exception as ex:
			logger.exception('error during get uids')
		finally:
			dbhelper.close()
			
		logger.info('end capture...')
		logger.debug('sleep 2 minutes...')
		time.sleep(60 * 2)

if __name__ == '__main__':
	main()