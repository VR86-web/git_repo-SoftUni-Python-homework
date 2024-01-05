import pandas as pd
#adding a list with names
column = ["Maria", "Batman", "Spongebob"]

#changing the 0 with "name" and adding 2 more columns
titled_columns = {"name": column,
                 "height": [1.67, 1.9, 0.25],
                 "weight": [54, 100, 1]}

#puting them into a frame
data = pd.DataFrame(titled_columns)

#selecting the column with name "weight" and index 1
select_column = data["weight"][1]

#selecting a row (iloc represent row) and putting the index in [] and after the key "weight"
select_row = data.iloc[1]["weight"]

#manipulate dataframe values
#bmi = body mass index
bmi = []
# formula = weight/(height**2)
for i in range(len(data)):
    bmi_score = data["weight"][i]/(data["height"][i]**2)
    bmi.append(bmi_score)

data["bmi"] = bmi

#safe dataframe to a file csv
# separated by "t" (tab)
# if we like to change the file to "txt" just change "bmi.csv" with "bmi.txt". Doesnt mather that we selected data.to_csv
data.to_csv("bmi.txt", sep="\t")
print(data)