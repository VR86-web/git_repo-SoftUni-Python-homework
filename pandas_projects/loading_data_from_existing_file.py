import pandas as pd
import sqlite3
#adding data from file
data = pd.read_csv("bmi.csv", sep="\t")
#adding database file
connection = sqlite3.connect("gta.db")
# select gta (gta represent the name of the table in gta file)
gta_data = pd.read_sql("select * from gta", connection)
first_five_rows = gta_data.head()
last_2_rows = gta_data.tail(2)
# filtering the column "city" if the value == "Liberty City" then the command return the entire row
filtered_row = gta_data[gta_data["city"] == "Liberty City"]
#replace
replaced_city = gta_data.replace("Liberty City", "New York")
#remove data
#axis=1 represent columns and axis=0 rows
# if we want to remove more columns("release_year") we just have to add the name of the column into ["city", "release_year"]
remove_column = gta_data.drop("city", axis=1)
#remove rows
remove_row = gta_data.iloc[1:4]
#add new rows
row = {"release_year": 2021,
       "release_name": "Natural Vision Evolved",
       "city": "Los Angeles"}
#new_row_data = gta_data.append(row, ignore_index=True)
print(filtered_row)
