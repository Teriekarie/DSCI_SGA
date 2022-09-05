import pandas as pd
import numpy as np

# program to create a dataset

df = pd.DataFrame({'First Name': ['Aryan', 'Rohan', 'Riya', 'Yash', 'Siddhant', ],
                   'Last Name': ['Singh', 'Agarwal', 'Shah', 'Bhatia', 'Khanna'],
                   'Type': ['Full-time Employee', 'Intern', 'Full-time Employee', 
                            'Part-time Employee', 'Full-time Employee'],
                   'Department': ['Administration', 'Technical', 'Administration', 
                                  'Technical', 'Management'],
                   'YoE': [2, 3, 5, 7, 6],
                   'Salary': [20000, 5000, 10000, 10000, 20000]})

print(df)

# using the pivot_table and determine the data, index, columns, aggfunc and `values` parameters.
# create a basic pivot table in pandas which shows the average salary of each type of employee for each department. 
# As there are no user-defined parameters passed, the remaining arguments have assumed their default values.
output = pd.pivot_table(data=df, 
                        index=['Type'], 
                        columns=['Department'], 
                        values='Salary',
                        aggfunc='mean')

print(output)
