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


scaler = MinMaxScaler()
X = scaler.fit_transform(X)

count_zeros = np.sum(y == 0)
count_ones = np.sum(y == 1)
print(f"Grid ON count:{count_ones},Grid OFF count{count_zeros}")


# In[ ]:





# In[ ]:





# In[22]:


X = X.reshape(X.shape[0], 1, X.shape[1])

# Step 3: Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[32]:


model = Sequential()
model.add(LSTM(50, input_shape=(1, 11)))  # Assuming you have 10 features
model.add(Dense(1, activation='sigmoid'))  # Sigmoid activation for binary classification
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[ ]:





# In[33]:


validation_data = (X_test, y_test)

history = model.fit(X_train, y_train, epochs=80, batch_size=32, validation_data=validation_data)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")


# In[34]:


threshold = 0.5 # sigmoid threshold, below 0.5 is 0 else 1
predicted_labels = []
for idx, data_point in enumerate(X):
    prediction = model.predict(data_point.reshape(1, 1, -1))[0][0]

    class_label = 1 if prediction >= threshold else 0
    #print(class_label)
    if class_label != y[idx]:
        print(f"True label:{y[idx]}, Predicted:{class_label}")
    predicted_labels.append(class_label)
    

class_labels = np.array(predicted_labels)

model.save('trained_model.h5')  # Save the trained model to a file
# In[35]:


from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


# In[36]:


len(class_labels)


# In[37]:


cm = confusion_matrix(y, class_labels)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', annot_kws={"size": 16})

plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')

plt.show()





# In[ ]:

from sklearn.metrics import classification_report
 
print(classification_report(y, class_labels))

