import sqlite3
from tokenize import Name

# connect to databse
conn = sqlite3.connect('grades.db')

# create a cursor
c = conn.cursor()

# query values from database
c.execute("""SELECT * FROM waec_scores""")

rows = c.fetchall()

# print(type(rows))

# program to determine student with highest score in maths
def max_math():
    c.execute("""SELECT Name, MAX(Maths) FROM waec_scores""")
    
    rows = c.fetchall()
    for rows in rows:
        Name, Maths = rows
        print(f" The student with the highest score in Maths is {Name} with {Maths} score. \n"f"{'.'*70}")
        # print()
max_math()

# program to determine the student with the lowest score in English
def min_english():
    c.execute("""SELECT Name, MIN(English) FROM waec_scores""")
    
    rows = c.fetchall()
    for rows in rows:
        Name, English = rows
        print(f" The student with the least score in English is {Name} with {English} score. \n"f"{'.'*70}")

min_english()

# program to determine the average student in Maths
def avg_english():
    c.execute("""SELECT Name, AVG(English) FROM waec_scores""")
    
    rows = c.fetchall()
    for rows in rows:
        Name, English = rows
        print(f" The student with the average score in English is {Name} with {English} score \n"f"{'.'*70}")

avg_english()
 
# program to determine the average student in English
def avg_maths():
    c.execute("""SELECT Name, AVG(Maths) FROM waec_scores""")
    
    rows = c.fetchall()
    for rows in rows:
        Name, Maths = rows
        print(f" The student with the average score in Maths is {Name} with {Maths} score \n"f"{'.'*70}")

avg_maths()

# program to determine the best performing student across all subjects
def best_student():
    c.execute("""SELECT Name,
              SUM(Maths+English+Basic_science+Agri_science+Language+Economics+Physics+Chemistry+Literature) AS Total_score
              FROM waec_scores
              GROUP BY Name
              ORDER BY total_score DESC
              LIMIT 1
              """)
    
    rows = c.fetchall()
    for rows in rows:
        Name, Total_score = rows
        print(f" The overall best student is {Name} with {Total_score} score \n"f"{'.'*70}")

best_student()

# program to determine the overall avergae student
def avg_best_student():
    c.execute("""SELECT Name,
              AVG(Maths+English+Basic_science+Agri_science+Language+Economics+Physics+Chemistry+Literature) AS Avg_score
              FROM waec_scores
              GROUP BY Name
              ORDER BY Avg_score DESC
              LIMIT 1               
              """)

    rows = c.fetchall()
    for rows in rows:
        Name, Avg_score = rows
        print(f" The overall average best student is {Name} with {Avg_score} score \n"f"{'.'*70}")

avg_best_student()