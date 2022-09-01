import sqlite3
from tokenize import Name

# program to create celeb database
conn = sqlite3.connect('celeb.db')
c = conn.cursor()

print('Celeb database created suscefully')

# # create a table called Celebrity
# c.execute("""CREATE TABLE Celebrity(
#                           Name TEXT,
#                           Genre TEXT,
#                           Num_albums INTEGER,
#                           Age INTEGER,
#                           Awards INTEGER,
#                           Years_in_industry INTEGER
# )""")

print('Celebrity table created succesfully')

# Add values in the table
Celebrity_list = [("TuBaba", "Afrobeats", "8", "46", "52", "28"),
               ("AdekunkeGold", "Afrobeats", "4", "35", "5", "12"),
               ("Asa", "Pop", "4", "39", "2", "18"),
               ("Ayrastarr", "Afropop", "3", "20", "1", "4"),
               ("BankyW", "R&B", "4", "41","8", "20"),
               ("Burnaboy", "Afrobeats", "6", "31", "38", "12"),
               ("Chidinma", "Gospel", "2", "31", "2", "11"),
               ("Davido", "Afropop", "6", "29", "32", "13"),
               ("Falz", "Hippop", "5", "31", "8", "13"),
               ("FemiKuti", "Jazz", "10", "60", "2", "44"),
               ("FireboyDML", "Afrobeats", "3", "26", "8", "10"),
               ("Flavour", "Highlife", "7", "38", "13", "17"),
               ("Iceprince", "Hippop", "4", "37", "17", "18"),
               ("Joeboy", "Contemporary", "3", "25", "2", "5"),
               ("JohnnyDrille", "Folk", "1", "32", "1", "10"),
               ("KizzDaniel", "Afrobeats", "4", "31", "7", "8"),
               ("Laycon", "Rap", "2", "28", "4", "6"),
               ("Mayorkun", "Afrobeats", "2", "28", "9", "6"),
               ("MercyChinwo", "Gospel", "2", "31", "5", "10"),
               ("Niniola", "Afrohouse", "4", "6", "8", "10"),
               ("Olamide", "Hiphop", "10", "33", "22", "22"),
               ("Timaya", "Dancehall", "8", "41", "13", "17")
]

# Add the multiple rows into the database
c.executemany('INSERT INTO Celebrity VALUES(?,?,?,?,?,?)', Celebrity_list)

c.execute('SELECT * FROM Celebrity')

rows = c.fetchall()
# print(rows)

#  formating the table
print("Name" + "\t\t\tGenre" + "\t\tNum_albums" + "\t\tAge" + "\t\tAwards" + "\t\tYears_in_industry \n"f"{'.' * 120}")

for rows in rows:
    Name, Genre, Num_albums, Age, Awards, Years_in_industry = rows
    print(f"{Name:16}\t{Genre:8}\t{Num_albums:8}\t{Age:8}\t{Awards:8}\t\t{Years_in_industry}")


#Most Decorated Celebrity
def most_decorated_celebrity():
        query= """SELECT Name, Genre, Awards FROM celebrity
        WHERE Awards = (SELECT MAX(Awards) FROM celebrity)
        """
        print(f"This is the celebrity with the most Awards") 
        c.execute(query)
        rows = c.fetchall()
        print("Name" + "\t\tGenre" + "\t\tAwards\n"f"{'.' * 40}")
        
        for rows in rows:
            Name, Genre, Awards = rows
            print(f"{Name:8}\t{Genre:8}\t{Awards:8}")
most_decorated_celebrity()


# program to determine the oldest celebrity
def oldest_celebrity():
        query= """
        SELECT Name, Age
        FROM celebrity
        WHERE age = (SELECT MAX(age)
                   FROM celebrity)
        """
        
        c.execute(query)
        rows = c.fetchall()
        print(f"This is the oldest celebrity in the industry")
        
        print("Name" + "\t\tAge\n"f"{'.' * 28}")
        
        for rows in rows:
            Name, Age = rows
            print(f"{Name:8}\t{Age:8}")
        # print(rows)
        
oldest_celebrity()

# program to determine the oldest in the industry
def longest_years_in_industry():
        query= """
        SELECT Name. Genre, Num_albums, Years_in_industry
        FROM celebrity
        WHERE Years_in_industry = (SELECT MAX(Years_in_industry)
                   FROM celebrity)
        """
        print(f"This Celebrity has been in the industry for years with hit Albums and still setting waves")
        c.execute(query)
        rows = c.fetchall()
        print(rows)
        
# program to determine the celebrity with the least number of albums
def least_num_albums():
        query= """
        SELECT Name, Genre, Num_albums
        FROM celebrity
        WHERE Num_albums = (SELECT MIN(Num_albums)
                   FROM celebrity)
        """
        print(f"The Celebrity with the least number of released albums")
        c.execute(query)
        rows = c.fetchall()
        
        print("Name" + "\t\tGenre" + "\t\tNum_albums\n"f"{'.' * 40}")
        
        for rows in rows:
            Name, Genre, Num_albums = rows
            print(f"{Name:8}\t{Genre:8}\t{Num_albums:8}")

least_num_albums()

# program to determine the most common genre of songs
def popular_genre():
    query= """
         SELECT genre, count(genre) as value_occurence from celebrity group by genre order by value_occurence desc limit 1
        """
    print(f"The most played genre of songs")
    c.execute(query)
    rows = c.fetchall()
    print(rows) 
    
popular_genre()
    
    # print("Genre \n"f"{'.' * 10}")
        
    # for rows in rows:
    #     Genre= rows
    #     print("{Genre:8}}")
    
conn.commit()

conn.close()
