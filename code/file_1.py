with open("C:\\Internship\\task1\data\Titanic-Dataset.csv","r") as file:
    a=file.readlines()
print("first 5 lines")
for i in range(0,6):
    print(a[i].strip())

#2.file operation
with open("C:\Internship\\task1\data\Titanic-Dataset.csv","r") as o_file:
    lis=o_file.readlines()

with open("C:\Internship\\task1\output\survivor.csv","w") as n_file :
    n_file.write(lis[0])

    for line in lis[1:]:
        if line.split(",")[1]=="1":
            n_file.write(line)
print("sucess")

#3. file operation
import csv
import json
data=[]
with open("C:\Internship\\task1\data\Titanic-Dataset.csv","r") as n_file:
    read=csv.DictReader(n_file)
    for i in read:
        data.append(i)
with open("C:\Internship\\task1\output\data.json","w",encoding="utf-8") as json_file:
    json.dump(data,json_file,indent=4)

#4. numpy programs
import numpy as np
import pandas as pd
df=pd.read_csv("C:\Internship\\task1\data\Titanic-Dataset.csv")
age_1=df["Age"]
age_arr=age_1.to_numpy()
age_mean=int(np.nanmean(age_arr))
age_arr[np.isnan(age_arr)]=age_mean
print(age_arr)
mean=np.mean(df["Age"])
print("mean:",mean)
median=np.median(df["Age"])
print("median:",median)
std_dev=np.std(df["Age"])
print("std_dev:",std_dev)

# 5. numpy
import numpy as np
import pandas as pd
df=pd.read_csv("C:\Internship\\task1\data\Titanic-Dataset.csv")
age=df["Age"].to_numpy()
age_mean=int(np.nanmean(age))
age[np.isnan(age)]=age_mean
print(age)
child=age<18
child_count=np.sum(child)
print("Childer:",child_count)
adult=(age>=18) & (age<60)
adult_count=np.sum(adult)
print("Adult:",adult_count)
senior=age>=60
senior_count=np.sum(senior)
print("seniors:",senior_count)

# 6. numpy
import pandas as pd
import numpy as np
data=pd.read_csv("C:\Internship\\task1\data\Titanic-Dataset.csv")
fare_arr=data["Fare"].to_numpy()
min_fare=np.min(fare_arr)
max_fare=np.max(fare_arr)
normal_fare=(fare_arr-min_fare)/(max_fare-min_fare)
print("First 10 normalized fare values:",normal_fare[:10])

#7.pandas
import pandas as pd
df=pd.read_csv("C:\Internship\\task1\data\Titanic-Dataset.csv")
print("Shape of dataset:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())

# 8.pandas
import pandas as pd
df=pd.read_csv("C:\Internship\\task1\data\Titanic-Dataset.csv")
a=df.groupby("Pclass")[["Survived","Age","Fare"]].mean()
print(a)

#9.pandas

import pandas as pd
df = pd.read_csv("C:\Internship\\task1\data\Titanic-Dataset.csv")
df["FamilySize"]=df["SibSp"]+df["Parch"]
res=df.groupby("FamilySize")["Survived"].mean()
res=res.sort_values(ascending=False)
print(res)

#10.pandas

import pandas as pd
df = pd.read_csv("C:\Internship\\task1\data\Titanic-Dataset.csv")
filter_df=df[
    (df["Sex"]=="female")&
    (df["Age"]>=18)&
    (df["Age"]<=35)&
    (df["Pclass"]==1)]
print(filter_df)
filter_df.to_csv("C:\Internship\\task1\output\Firstclass_women.csv",index=False)
print("CSV file created")