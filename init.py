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
  [actual_videos_count] NUMBER DEFAULT 0, 
  CONSTRAINT [sqlite_autoindex_uids_1] PRIMARY KEY ([id]));
"""

USER_CREATE_SQL = """
CREATE TABLE IF NOT EXISTS [user] (
  [id] VARCHAR NOT NULL, 
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

csr.execute("INSERT INTO [uids] ([id]) VALUES ('512194ec7d34941827001340')")
csr.execute("INSERT INTO [uids] ([id]) VALUES ('526258e2c58a878d061e30cf')")

conn.commit()

print('initialize success!')

