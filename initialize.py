import sqlite3
import os
import sys

curdir = os.path.dirname(sys.argv[0])
os.chdir(curdir)

DB_PATH = 'weipai.db'

UIDS_CREATE_SQL = """
CREATE TABLE IF NOT EXISTS [uids] (
  [id] VARCHAR NOT NULL, 
  [initialized] BOOLEAN NOT NULL DEFAULT 0, 
  [captured_videos_count] NUMBER DEFAULT 0, 
  CONSTRAINT [sqlite_autoindex_uids_1] PRIMARY KEY ([id]));
"""

USER_CREATE_SQL = """
CREATE TABLE IF NOT EXISTS [user] (
  [id] VARCHAR NOT NULL, 
  [name] VARCHAR NOT NULL, 
  [face] TEXT, 
  [face_thumbnail] TEXT, 
  [sex] VARCHAR, 
  [follows] NUMBER, 
  [fans] NUMBER, 
  [videos] NUMBER, 
  CONSTRAINT [] PRIMARY KEY ([id]));
"""

VIDEO_CREATE_SQL = """
CREATE TABLE IF NOT EXISTS [video] (
  [id] VARCHAR NOT NULL, 
  [user_id] VARCHAR NOT NULL, 
  [snaps] TEXT, 
  [snaps_3in1] TEXT, 
  [date] VARCHAR, 
  [length] VARCHAR, 
  [like] NUMBER, 
  [view] NUMBER, 
  [comment] NUMBER, 
  [desc] TEXT, 
  [time] VARCHAR, 
  [datetime] DATETIME, 
  [flv_url] TEXT, 
  [mov_url] TEXT, 
  CONSTRAINT [] PRIMARY KEY ([id]));
"""

conn = sqlite3.connect(DB_PATH)
csr = conn.cursor()
csr.execute(UIDS_CREATE_SQL)
csr.execute(USER_CREATE_SQL)
csr.execute(VIDEO_CREATE_SQL)

csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('512194ec7d34941827001340')") # 黄可
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('526258e2c58a878d061e30cf')") # 丝绸裹着性感
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('505d163d7f34941c2f000070')") # 苏夏妞妞
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('527900e97f34948267b8a8b0')") # 唐馨baby
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('5092ac517f34949978000090')") # 桓淼淼baby
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('5286dbf59f6c006c2528d4ba')") # Forbiddenlove_夏洛
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('52b330e5803494662e20aac8')") # 小狐狸茜茜
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('521ccf909f6c00b959d64135')") # 给你看
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('520f44b88034940f047dcfc3')") # 硪爱祢
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('5193daa55e8e87a42c0000bd')") # 自己拍的哦
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('523be1627d3494d547858c8d')") # 2013100727
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51f2391a803494aa4167ba5a')") # 多多汁
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51cf79008134946b41000008')") # 2847203497
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51ad9c4f5e8e875a62000000')") # DJ-CC
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('521064a07d3494b6304bcf94')") # 张雨萌


conn.commit()

print('initialize success!')

