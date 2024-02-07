import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv(r'C:\Users\SAHYADRI\Downloads\data.csv')
dur=pd.DataFrame(dataset,columns=["Duration"])
pls=pd.DataFrame(dataset,columns=["Pulse"])
mpls=pd.DataFrame(dataset,columns=["Maxpulse"])
cal=pd.DataFrame(dataset,columns=["Calories"])
figure,axis=plt.subplots(1,2)
axis[0].plot(df.corr())
axis[0].set_title("Correlation Graph")
axis[1].plot(dataset)
axis[1].set_title("Full Graph")
plt.legend(["Duration","Pulse","Max Pulse","Calories"])
print(df.to_string()) 
