import sqlite3
# connect to a database
conn = sqlite3.connect('stationary.db')

#create a cusor
c = conn.cursor()

print('Cursor created')

#create a table called inventory
# c.execute('''CREATE TABLE inventory(
#                     Tags INTEGER,
#                     Items TEXT,
#                     Cost_price INTERGER,
#                     Quantity INTEGER
                    
#           )''')

# Add rows to input into the table created
shop_list = [(1, "Books", 1000, 50),
                (2, "Pencils", 500, 100),
                (3, "Eraser", 300, 50),
                (4, "Staplers", 1200, 40),
                (5, "PenCups", 700, 60),
                (6, "Glue", 1500, 700),
                (7, "Scissors", 2000, 20),
                (8, "Calculator", 1500, 20),
                (9, "Notepads", 2500, 500),
                (10, "Highlighter", 3000, 50),
                (11, "Markers", 500, 170),
                (12, "Envelopes", 700, 250)
]

# Add the rows into the shop_list
c.executemany('INSERT INTO inventory VALUES(?,?,?,?)', shop_list)

c.execute('SELECT * FROM inventory')

rows = c.fetchall()

# formating the table
# print("\ttags" + "\t\titems" + "\t\t\tcost_price" + "\t\tquantity \n"f"{'.' * 100}")

# for row in rows:
#      tags, items, cost_price, quantity = row
#      print(f"{tags:16}\t{items:16}\t{cost_price:8}\t\t{quantity:8}")



# program to determine the amount the shop owner invested
# by suming the cost_price of all items
def total_investment():
    c.execute("""SELECT SUM(cost_price) 
              FROM inventory;
              """)
    rows = c.fetchall()
    for rows in rows:
        cost_price = rows
        print(f"The total amount the shop owner invested is {cost_price}")
        
total_investment()

# program to calculate the average quantity of items in stock
def avg_quantities_in_stock():
    c.execute("""SELECT ROUND(AVG(Quantity))
              FROM inventory;
              """)
    rows = c.fetchall()
    for rows in rows:
        quantity = rows
        print(f"The Average quantites of items still in stock  is {quantity}")
  
avg_quantities_in_stock()

# program to determine the item with the least quantity in stock
def least_quantity_in_stock():
    c.execute("""SELECT Items, Quantity
                   FROM inventory
        WHERE Quantity = (SELECT MIN(Quantity)
                   FROM inventory)
    """)
    rows = c.fetchall()
    print(f"The least quantity of item still available is:")
  
    print("Items" + "\t\tQuantity\n"f"{'.' * 28}")
        
    for rows in rows:
            Items, Quantity = rows
            print(f"{Items:8}\t{Quantity:8}")

least_quantity_in_stock()

# program to determine items with most quantity in stock
def most_quantity_in_stock():
    c.execute("""SELECT Items, Quantity
                   FROM inventory
        WHERE Quantity = (SELECT MAX(Quantity)
                   FROM inventory)
    """)
    rows = c.fetchall()
    print(f"The most quantity of item still available is:")
  
    print("Items" + "\t\tQuantity\n"f"{'.' * 28}")
        
    for rows in rows:
            Items, Quantity = rows
            print(f"{Items:8}\t{Quantity:8}")

most_quantity_in_stock()

