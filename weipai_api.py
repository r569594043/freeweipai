import urllib.request
import os
import time
from bs4 import BeautifulSoup as bs
import re
import base64
import json

# user_ids = ['512194ec7d34941827001340', '526258e2c58a878d061e30cf']
user_ids = ['512194ec7d34941827001340']

USER_URL = 'http://www.weipai.cn/user/{user_id}'

VIDEOS_URL = 'http://www.weipai.cn/videos/{user_id}'

VIDEO_URL = 'http://www.weipai.cn/video/{video_id}'

VIDEO_INFO_URL = 'http://www.weipai.cn/video/play/id/{video_id}/type/theater/source/web?_={timestamp}'

MORE_VIDEOS = 'http://www.weipai.cn/user/moreOwnVideos/uid/{user_id}?page={page}'

REG = re.compile(r"s=(.*?)',")
REG1 = re.compile(r"p=(.*?)&")

headers = {
	'Host': 'www.weipai.cn',
	# 'Referer': 'http://www.weipai.cn/user/526258e2c58a878d061e30cf',
	# 'Referer': 'http://www.weipai.cn/videos/512194ec7d34941827001340',
	'Referer': 'http://www.weipai.cn/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36',
	# 'Cookie': 'weipai_token=mkom5ducaibsqdrs687qcu5tf4'
	# 'Cookie': 'weipai_token=0cp1ddfbei8k2l8ev2cf35olb7'
	'Cookie': 'weipai_token=0cp1ddfbei8k2l8ev2cf35olb7'
}


def analysis_video_list_info(bs_doc):
	video_list_doc = bs_doc.select('#container_div #full_column_div .wf_container .video')
	videos = []
	if len(video_list_doc) > 0:
		for video_info_doc in video_list_doc:
			id = video_info_doc.get('id')
			day = video_info_doc.select('.wrap .time .day')[0].text
			date = video_info_doc.select('.wrap .time .date')[0].contents[2]
			snaps = video_info_doc.select('.wrap .snaps .imgs img')[0].get('src')
			length = video_info_doc.select('.wrap .snaps .imgs .length')[0].text
			video_link = video_info_doc.select('.wrap .snaps .video_link')[0].get('href')
			like = video_info_doc.select('.wrap .details .details-like')[0].text
			view = video_info_doc.select('.wrap .details .details-view')[0].text
			comment = video_info_doc.select('.wrap .details .details-comment')[0].text
			desc = None
			desc_doc = video_info_doc.select('.wrap .desc')
			if len(desc_doc) > 0:
				desc = desc_doc[0].text
			date = date + '-' + day
			like = int(like)
			view = int(view)
			comment = int(comment)
			videos.append({
				'id': id,
				'date': date,
				'snaps': snaps,
				'length': length,
				# 'video_link': video_link,
				'like_count': like,
				'view_count': view,
				'comment_count': comment,
				'desc': desc
			})
	return videos
	
def get_user_info(id):
	user_info = {}
	req = urllib.request.Request(USER_URL.format(user_id = id), headers = headers)
	resp = urllib.request.urlopen(req)
	html_doc = resp.read().decode()
	bs_doc = bs(html_doc)
	user_info_box = bs_doc.select('#container_div #full_column_div .wf_container .info')
	if len(user_info_box) > 0:
		user_info_box = user_info_box[0]
		face = None
		face_doc = user_info_box.select('.wrap .imgs .face img')
		if len(face_doc) > 0:
			face = face_doc[0].get('src')
		name = user_info_box.select('.wrap .user .name')[0].text
		sex = 'female' if 'female' in user_info_box.select('.sex')[0].get('class') else 'male'
		follows = user_info_box.select('.wrap .follows span')[0].text
		fans = user_info_box.select('.wrap .fans span')[0].text
		videos = user_info_box.select('.wrap .videos span')[0].text
		follows = int(follows)
		fans = int(fans)
		videos = int(videos)
		# face_thumbnail = face.replace('/180/', '/50/')
		user_info = {
			'face': face,
			'name': name,
			'sex': sex,
			'follows_count': follows,
			'fans_count': fans,
			'videos_count': videos,
			'id': id,
			# 'face_thumbnail': face_thumbnail,
			'videos': analysis_video_list_info(bs_doc)
		}
	return user_info

def get_videos_info(id):
	user_info = {}
	req = urllib.request.Request(VIDEOS_URL.format(user_id = id), headers = headers)
	resp = urllib.request.urlopen(req)
	html_doc = resp.read().decode()
	bs_doc = bs(html_doc)
	user_info_box = bs_doc.select('#container_div #full_column_div .wf_container .info')
	if len(user_info_box) > 0:
		user_info_box = user_info_box[0]
		face = None
		face_doc = user_info_box.select('.wrap .imgs .face img')
		if len(face_doc) > 0:
			face = face_doc[0].get('src')
		name = user_info_box.select('.wrap .user .name')[0].text
		sex = 'female' if 'female' in user_info_box.select('.sex')[0].get('class') else 'male'
		follows = user_info_box.select('.wrap .follows span')[0].text
		fans = user_info_box.select('.wrap .fans span')[0].text
		videos = user_info_box.select('.wrap .videos span')[0].text
		follows = int(follows)
		fans = int(fans)
		videos = int(videos)
		# face_thumbnail = face.replace('/180/', '/50/')
		user_info = {
			'face': face,
			'name': name,
			'sex': sex,
			'follows_count': follows,
			'fans_count': fans,
			'videos_count': videos,
			'id': id,
			# 'face_thumbnail': face_thumbnail,
			'videos': analysis_video_list_info(bs_doc)
		}
	return user_info

def get_video_info(id):
	user_info = {}
	video_info = {}
	req = urllib.request.Request(VIDEO_URL.format(video_id = id), headers = headers)
	resp = urllib.request.urlopen(req)
	html_doc = resp.read().decode()
	bs_doc = bs(html_doc)
	user_info_box = bs_doc.select('.theater .theater-wrapper .left_div .info')
	if len(user_info_box) > 0:
		user_info_box = user_info_box[0]
		face = None
		face_doc = user_info_box.select('.wrap .imgs .face img')
		if len(face_doc) > 0:
			face = face_doc[0].get('src')
		name = user_info_box.select('.wrap .user .name')[0].text
		sex = 'female' if 'female' in user_info_box.select('.sex')[0].get('class') else 'male'
		follows = user_info_box.select('.wrap .follows span')[0].text
		fans = user_info_box.select('.wrap .fans span')[0].text
		videos = user_info_box.select('.wrap .videos span')[0].text
		follows = int(follows)
		fans = int(fans)
		videos = int(videos)
		# face_thumbnail = face.replace('/180/', '/50/')
		user_info = {
			'face': face,
			'name': name,
			'sex': sex,
			'follows_count': follows,
			'fans_count': fans,
			'videos_count': videos
			# 'id': id,
			# 'face_thumbnail': face_thumbnail
		}
	video_info_box = bs_doc.select('.theater .theater-stage .theater-wrapper #videos_div')
	if len(video_info_box) > 0:
		video_info_box = video_info_box[0]
		snaps = video_info_box.select('.video .video_player .snaps img')[0].get('src')
		day = video_info_box.select('.video .time .day')[0].text
		date = video_info_box.select('.video .time .date')[0].contents[2]
		length = video_info_box.select('.video .video_player .snaps .length')[0].text
		video_title = video_info_box.select('.video_info .video_title')[0].text
		video_detail = video_info_box.select('.video_info .video_details .video_detail')[0].text
		view = video_info_box.select('.video_info .video_details .details-view')[0].text
		like = video_info_box.select('.video_info .video_details .details-like')[0].text
		comment = video_info_box.select('.video .video_buttons .comment span')[0].text.replace('评论(', '').replace(')', '')
		date = date + '-' + day
		view = int(view)
		like = int(like)
		comment = int(comment)
		video_time = video_detail.split(' ')[1]
		video_info = {
			'id': id,
			'snaps': snaps,
			'date': date,
			'length': length,
			'like_count': like,
			'view_count': view,
			'comment_count': comment,
			'desc': video_title,
			'user': user_info,
			'time': video_time
		}
	return video_info
	
def get_video_url(id):
	video_url = None
	req = urllib.request.Request(VIDEO_INFO_URL.format(video_id = id, timestamp = int(time.time()*1000)), headers = headers)
	resp = urllib.request.urlopen(req)
	video_info = resp.read().decode()
	m = REG.search(video_info)
	if m:
		video_url_encrypted = m.group(1)
		video_params = base64.b64decode(video_url_encrypted).decode()
		m1 = REG1.search(video_params)
		if m1:
			video_url = m1.group(1)
			return video_url
	return video_url

def get_more_videos(id, page):
	videos = []
	req = urllib.request.Request(MORE_VIDEOS.format(user_id = id, page = page), headers = headers)
	resp = urllib.request.urlopen(req)
	html_doc = resp.read().decode()
	bs_doc = bs(html_doc)
	videos_doc = bs_doc.contents
	if len(bs_doc.contents) == 1 and bs_doc.contents[0].name == 'html':
		videos_doc = bs_doc.contents[0].select('.video')
	if len(videos_doc) > 0:
		for video_doc in videos_doc:
			id = video_doc.get('id')
			day = video_doc.select('.wrap .time .day')[0].text
			date = video_doc.select('.wrap .time .date')[0].contents[2]
			snaps = video_doc.select('.wrap .snaps .imgs img')[0].get('src')
			length = video_doc.select('.wrap .snaps .imgs .length')[0].text
			like = video_doc.select('.wrap .details .details-like')[0].text
			view = video_doc.select('.wrap .details .details-view')[0].text
			comment = video_doc.select('.wrap .details .details-comment')[0].text
			desc = None
			desc_doc = video_doc.select('.wrap .desc')
			if len(desc_doc) > 0:
				desc = desc_doc[0].text
			video_link = video_doc.select('.wrap .video_link')[0].get('href')
			date = date + '-' + day
			like = int(like)
			view = int(view)
			comment = int(comment)
			videos.append({
				'id': id,
				'snaps': snaps,
				'date': date,
				'length': length,
				'like_count': like,
				'view_count': view,
				'comment_count': comment,
				'desc': desc
			})
	return videos
			

def main():
	#print(get_video_url('5322d4beebeddbdd3d8b45a3'))
	#for id in user_ids:
	#	print(get_videos_info(id)['videos'][0])
	#	print(get_user_info(id)['videos'][0])
	print(get_more_videos('512194ec7d34941827001340', 1), open('c:/more_videos.txt', 'w'))
	print('done!')
	
	
if __name__ == '__main__':
	main()