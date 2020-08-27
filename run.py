import pandas
import matplotlib.pyplot as plt

df= pandas.read_csv("multiTimeline.csv")
print(df)


#Creating a column 
search_intel = df.Nvidia
Week = df.Week

#Printing column
print(search_intel)
print(Week)

#For plotting data
plt.plot(Week,search_intel)

plt.xlabel("Week")
plt.ylabel("Amount of people searching")
plt.title("Nvidia searches over time")

plt.show()





