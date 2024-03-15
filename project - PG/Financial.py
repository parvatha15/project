# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:17:19 2024

@author: lenovo
"""


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import AdaBoostClassifier
import warnings 
warnings.filterwarnings("ignore", category=DeprecationWarning)

print("#--------------------Data Selection---------------#")
print("*******************")
df = pd.read_csv('financialdataset.csv')
df = df.iloc[0:80000]
print()
 

print(df.head(20))
print()



print("#--------------------Find missing values---------------#")
print("*******************")

print(df.isnull().sum())
print()

print("#--------------------Fill 0 from missing Values---------------#")
print("*******************")
df=df.fillna(0)


print(df.isnull().sum())
print()

print("#--------------------Before Label Encoding---------------#")
print("*******************")
print(df.head(20))

print("#--------------------After Label Encoding---------------#")
print("*******************")

le = LabelEncoder()
df.type = le.fit_transform(df.type)
df.nameOrig = le.fit_transform(df.nameOrig)
df.nameDest = le.fit_transform(df.nameDest)

print(df.head(20))
print()

print("#--------------------Data Splitting---------------#")
print("*******************")

x=df.drop('isFraud',axis=1)


#print(x.head(20))
#print()

y= df.isFraud

#print(y.head(20))
#print()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

print("Total no of dataset :", df.shape)
print("Training set Without Target", x_train.shape)
print("Training set only Target", y_train.shape)
print("Testing set Without Target", x_test.shape)
print("Testing set only Target", y_test.shape)
print()

print("#--------------------Random Forest Algorithm---------------#")
print("*******************")


#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)
#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)

confusion_matrix(y_test, y_pred)
accuracy=accuracy_score(y_test, y_pred)
acc1=accuracy*100
print("Matrix: ")
print(confusion_matrix(y_test,y_pred))
print("classfication: ")
print(classification_report(y_test, y_pred))
print("Accuracy: ",acc1)
print()


print("#--------------------Ada Boost---------------#")
print("*******************")

abc=AdaBoostClassifier()
abc.fit(x_train, y_train)
print(abc.score(x_test, y_test))
y_pred = abc.predict(x_test)
accuracy=accuracy_score(y_test, y_pred)
acc3=accuracy*100
print()
print("Matrix: ")
print(confusion_matrix(y_test,y_pred))
print("classfication: ")
print(classification_report(y_test, y_pred))
print("Accuracy: ",acc3)
print()

print("#--------------------Get input Manually---------------#")
print("*******************")

pre_x_test=x_train.head(1)

pre_y_test=y_train.head(1)

print(pre_x_test)
print(pre_y_test)
print()


y_pred = abc.predict([[ 8,3,9201.92,65750,0.0,0.0,20252,0.0,0.0,0]]);


print(y_pred)
print()

if y_pred==0:
    print("Non Fraud")
else:
  print("Fraud")

# print("#--------------------Get input from user---------------#")
# print("*******************")
  
    

# ele1=int(input('Enter the Step: '))
# ele2=int(input('Enter the Type: '))
# ele3=int(input('Enter the Amount: '))
# ele4=int(input('Enter the nameOrig: '))
# ele5=int(input('Enter the oldbalance: '))
# ele6=int(input('Enter the newbalance: '))
# ele7=int(input('Enter the nameDest: '))
# ele8=int(input('Enter the oldbalance: '))
# ele9=int(input('Enter the newbalance: '))
# ele10=int(input('Enter the isFlaggedFraud: '))
  
# lst = [ele1,ele2,ele3,ele4,ele5,ele6,ele7,ele8,ele9,ele10]


# #lst(input(ele1,ele2,ele3,ele4,ele5,ele6,ele7,ele8,ele9,ele10)) # adding the element
      
# #print(lst)
# #df['type'] = pd.to_numeric(df['type'])


# y_pred = abc.predict([lst])

# print(y_pred)

# if y_pred==0:
#     print("This is financial Non Fraud")
# else:
#   print("This is financial Fraud")
#   print()
print("#--------------------Camparison between 2 Algorithm Accuracy---------------#")
print("*******************")
print()
#print(acc1)
#print(acc2)
#print(acc3)

df_plot  = pd.DataFrame([acc1,acc3])
df_plot.index=['Random Forest','Ada Boost']

# Plot
df_plot.plot(kind='bar',stacked=True, title='Accuracy Bar plot');

print()



