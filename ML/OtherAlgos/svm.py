#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
#from imblearn.under_sampling import RandomUnderSampler


# In[12]:


from imblearn.under_sampling import RandomUnderSampler


# In[13]:


from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score



# In[14]:


# i had outdated pandas so read_excel is not working 
#df = pd.read_excel('final_data.xlsx')

# workaround
df = pd.read_excel('final_data.xlsx',engine='openpyxl') # 


# In[15]:


# checking for nan values
missing_values = df.isna().sum()
print(missing_values)


# In[16]:


# dropping rows with missing values
df.dropna(inplace=True)


# In[17]:


# # Extract timestamp features
df['Year'] = df['Timestamp'].dt.year
df['Month'] = df['Timestamp'].dt.month
df['Day'] = df['Timestamp'].dt.day
df['Hour'] = df['Timestamp'].dt.hour
df['Minute'] = df['Timestamp'].dt.minute
df['Second'] = df['Timestamp'].dt.second

# Define features and target
#features = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second', 'Temperature', 'Humidity', 'WindSpeed', 'WeatherObserved','DewpointTemp']
#features = ['Temperature', 'Humidity', 'WindSpeed', 'WeatherObserved','DewpointTemp']
features = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second', 'Temperature', 'Humidity', 'WindSpeed', 'WeatherObserved','DewpointTemp']


# In[18]:


#features = ['Temperature', 'Humidity', 'WindSpeed', 'WeatherObserved','DewpointTemp']


# In[19]:


X = df[features].values
y = df['Grid'].values


# # Undersampling
# 

# In[20]:


under_sampler = RandomUnderSampler(random_state=42)

X, y = under_sampler.fit_resample(X, y)


# In[21]:



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

count_zeros = np.sum(y == 0)
count_ones = np.sum(y == 1)
print(f"Grid ON count:{count_ones},Grid OFF count{count_zeros}")


# In[ ]:


# Reshape the data to two dimensions
X_train = X_train.reshape(X_train.shape[0], -1)
X_test = X_test.reshape(X_test.shape[0], -1)

# Create an instance of the SVM model
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)

# Train the SVM model
svm_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm_model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Now, you can use 'svm_model' to make predictions on new data