import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.model_selection import train_test_split as TTS

df = pd.read_csv('/Users/brendon/Documents/Kaggle_Data/Bank_Churn/BankChurners.csv')
df = df.drop(columns=['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'])

# converting categorical variables into numerical
df['Gender'] = df.Gender.apply(lambda x: 1 if x == 'F' else 0)
df['Attrition_Flag'] = df.Attrition_Flag.apply(lambda x: 1 if x == 'Attrited Customer' else 0)

edu_vals_cat = df.Education_Level.unique()
edu_vals_num = list(range(7))
edu_vals_zip = list(zip(edu_vals_num, edu_vals_cat))
for i in edu_vals_zip:
    i = list(i)
    df['Education_Level'] = df.Education_Level.apply(lambda x: i[0] if x == i[1] else x)

mar_vals_cat = df.Marital_Status.unique()
mar_vals_num = list(range(len(mar_vals_cat)))
mar_vals_zip = list(zip(mar_vals_num, mar_vals_cat))
for i in mar_vals_zip:
    i = list(i)
    df['Marital_Status'] = df.Marital_Status.apply(lambda x: i[0] if x == i[1] else x)

inc_vals_cat = df.Income_Category.unique()
inc_vals_num = list(range(len(inc_vals_cat)))
inc_vals_zip = list(zip(inc_vals_num, inc_vals_cat))
for i in inc_vals_zip:
    i = list(i)
    df['Income_Category'] = df.Income_Category.apply(lambda x: i[0] if x == i[1] else x)

car_vals_cat = df.Card_Category.unique()
car_vals_num = list(range(len(car_vals_cat)))
car_vals_zip = list(zip(car_vals_num, car_vals_cat))
for i in car_vals_zip:
    i = list(i)
    df['Card_Category'] = df.Card_Category.apply(lambda x: i[0] if x == i[1] else x)

# Test and Training Data
X = df.drop(columns=['Attrition_Flag', 'CLIENTNUM'])
Y = df['Attrition_Flag']

x_train, x_test, y_train, y_test = TTS(X, Y, test_size= 0.2, random_state = 5)

# Random Forest
clf = RFC(n_estimators=20)
clf = clf.fit(x_train, y_train)

RF_Predict = clf.predict(x_test)
RF_test = list(zip(RF_Predict, y_test))

num_correct = 0
for i in RF_test:
    if i[0] == i[1]:
        num_correct += 1

print("Random Forest Accuracy = " + str((num_correct/len(y_test))))