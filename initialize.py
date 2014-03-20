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

csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('526844127f34944c1bd4c00e')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51bdc3a65a8e872864000006')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51b24e275d8e8777250000a2')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51a58de95d8e873f56000029')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('5175f8d97f3494930a000060')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51231a2e813494975a000522')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51af43b45c8e87ca74000004')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('520923099f6c008c69000221')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('5205dd278034949c1e857948')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51c54683813494282f000001')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('5189e84a5e8e873d6c000039')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('519f7f465e8e870f30000002')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('506945307d34941b78000166')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('518b84148034942944000003')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('5191c27e5d8e87d73e000044')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('5191118b5a8e874f1d00002c')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51d632ce8034943f27712e20')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51dfec52813494503c00005d')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('508e10fa8134940919000169')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51d97f797d3494974300007d')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51d84f157f34947020000041')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51af43b45c8e87ca74000004')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51bd67df8134947345000000')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51bab489803494d7320000cf')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51bff270813494362c000000')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51e0bb288134941c1a000045')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('51e391417d34944239000001')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('50f85394813494582c0000ed')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('510800377d34943c56000122')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('519b977f5e8e871739000002')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('52ce7575803494d6433e4222')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('5185f1cb7d3494a81b000038')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('5288a0777f3494394832787b')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('52d0082277d3cca54d8b45dc')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('52bf5c81c58a87517aa08b01')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('52cf6fa979d3cc2a068b45b2')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('52c96d9b79d3ccc9308b46b4')")
csr.execute("INSERT OR IGNORE INTO [uids] ([id]) VALUES ('52d1a84c8134948602be22ce')")


conn.commit()

print('initialize success!')

