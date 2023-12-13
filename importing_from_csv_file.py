import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv(r'C:\Users\SAHYADRI\Downloads\data.csv')#use the path of the csv file here
dur=pd.DataFrame(dataset,columns=["Duration"])
pls=pd.DataFrame(dataset,columns=["Pulse"])
mpls=pd.DataFrame(dataset,columns=["Maxpulse"])
cal=pd.DataFrame(dataset,columns=["Calories"])
plt.plot(dur)
plt.plot(pls)
plt.plot(mpls)
plt.plot(cal)
plt.xlabel("Max Pulse")
plt.ylabel("Calories")
plt.legend(["Duration","Pulse","Max Pulse","Calories"])
print(df.to_string()) 
