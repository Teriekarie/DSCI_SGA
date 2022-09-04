import sqlite3
import csv

# create database connection
conn = sqlite3.connect("grades.db")

print("connection created successfully")

# create cursor
c = conn.cursor()

print("cursor creates successfully")

# create table query
score_sheet = """
CREATE TABLE waec_scores
(Name TEXT,
Maths INTEGER,
English INTEGER,
Basic_science INTEGER,
Agri_science INTEGER,
Language INTEGER,
Economics INTEGER,
Physics INTEGER,
Chemistry INTEGER,
Literature INTEGER)

"""

c.execute(score_sheet)

print("table created")

# load csv file into the table
with open('waec.csv') as data_fh:
    # read the csv file
    waec_scores = csv.reader(data_fh)
    
    # skip header
    next(waec_scores)
    
    print("csv file read without header")
    
    c.executemany(
        """
        INSERT INTO waec_scores
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """,
        waec_scores
    )
    
    print("csv file inserted")
    
#commit changes
conn.commit()

conn.close()

