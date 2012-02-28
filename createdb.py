#!/usr/bin/env python
import sqlite3
dbname = "portal.sqlite"
createq = """CREATE TABLE Questions (qid INTEGER PRIMARY KEY AUTOINCREMENT,
             question TEXT, answer TEXT)"""
createu = """CREATE TABLE Users (phone VARCHAR(64) NOT NULL PRIMARY KEY, 
             qid INTEGER, created FLOAT, finished FLOAT,
             FOREIGN KEY(qid) REFERENCES Questions(qid))"""
conn = sqlite3.connect(dbname)
conn.execute(createq)
conn.execute(createu)
conn.commit()

questions = "questions.data"
qfd = open(questions, "r")
for line in qfd:
   try:
      question, answer = eval(line)
      conn.execute("INSERT INTO Questions(question, answer) VALUES(?, ?)", (question, answer))
   except Exception, e: print e
conn.execute("INSERT INTO Questions(qid, question, answer) VALUES(0, '', ?)", ("start begin lets go play",))
conn.commit()
qfd.close()
