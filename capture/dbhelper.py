import sqlite3, re

conn = None
csr = None

UIDS_SQL = 'SELECT [id],[initialized] FROM uids;'

USER_SQL = """REPLACE INTO [user] ([id], [name], [face], [face_thumbnail], [sex], [follows], [fans], [videos])
VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', {5}, {6}, {7});
"""
#0 [id], 
#1 [name], 
#3 [face], 
#4 [face_thumbnail], 
#5 [sex], 
#6 [follows], 
#7 [fans], 
#8 [videos]
VIDEO_SQL = """REPLACE INTO [video] ([id], [user_id], [snaps], [snaps_3in1], [date], [length], [like], [view], [comment], [desc], [time], [datetime], [flv_url], [mov_url]) 
VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8}, '{9}', '{10}', '{11}', '{12}', '{13}');
"""
#0	[id]
#1  [user_id]
#2  [snaps]
#3  [snaps_3in1]
#4  [date]
#5  [length]
#6  [like]
#7  [view]
#8  [comment]
#9  [desc]
#10 [time]
#11 [datetime]
#12 [flv_url]
#13 [mov_url]

VIDEOS_COUNT_SQL = "SELECT COUNT(*) [count] FROM [video] WHERE [user_id] = '{0}'"

UPDATE_UIDS_INFO_SQL = "UPDATE [uids] SET [initialized] = {1}, [captured_videos_count] = {2} WHERE [id] = '{0}'"

def open(path):
	global conn, csr
	conn = sqlite3.connect(path)
	csr = conn.cursor()

def save_user(user):
	if 'face' in user and user['face']:
		user['face_thumbnail'] = user['face'].replace('/180/', '/50/')
	else:
		user['face'] = ''
		user['face_thumbnail'] = ''
	user_sql = USER_SQL.format(user['id'], user['name'], user['face'], user['face_thumbnail'], user['sex'], user['follows_count'], user['fans_count'], user['videos_count'])
	csr.execute(user_sql)

def save_video(video):
	if 'snaps' in video:
		snaps = video['snaps']
		if snaps.count('.') > 3:
			snaps = snaps.replace('ppp/video/', 'video')
			snaps = re.sub(r'\.s\..*?\.jpg', '.jpg', snaps)
			snaps = snaps.replace('.1.jpg', '.jpg').replace('.2.jpg', '.jpg').replace('.3.jpg', '.jpg')
		video['snaps_3in1'] = snaps.replace('.jpg', '.mov.3in1.jpg')
		video['flv_url'] = snaps.replace('.jpg', '.flv')
		video['mov_url'] = snaps.replace('.jpg', '.mov')
	if 'length' in video:
		video['length'] = video['length'].replace("'", "''")
	video['time'] = ''
	video['datetime'] = ''
	video['desc'] = video['desc'].replace("'", "''") if video['desc'] else ''
	video_sql = VIDEO_SQL.format(video['id'], video['user_id'], video['snaps'], video['snaps_3in1'], video['date'], video['length'], video['like_count'], video['view_count'], video['comment_count'], video['desc'], video['time'], video['datetime'], video['flv_url'], video['mov_url'])
	csr.execute(video_sql)

def save_videos(user_id, videos):
	for video in videos:
		video['user_id'] = user_id
		save_video(video)

def get_videos_count(user_id):
	csr.execute(VIDEOS_COUNT_SQL.format(user_id))
	return csr.fetchone()[0]

def update_uids_info(user_id, initialized, captured_videos_count):
	csr.execute(UPDATE_UIDS_INFO_SQL.format(user_id, int(initialized), captured_videos_count))

def get_uids():
	csr.execute(UIDS_SQL)
	return csr.fetchall()

def commit():
	conn.commit()

def close():
	csr.close()
	conn.close()