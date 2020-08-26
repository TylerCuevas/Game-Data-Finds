import pandas
df= pandas.read_csv("multiTimeline.csv")
print(df)


#Creating a column 
search_intel = df.Intel_Core
Week = df.Week

#Printing column
print(search_intel)
print(Week)

#The challenge
search_intel_number = search_intel[0]
print(search_intel_number)

