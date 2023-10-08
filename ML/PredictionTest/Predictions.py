import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler  
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from imblearn.under_sampling import RandomUnderSampler

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score


model = load_model('trained_model.h5')  # loading the trained model


df = pd.read_excel('final_data.xlsx',engine='openpyxl') # adding the data-set file for reference  
missing_values = df.isna().sum()

df.dropna(inplace=True) # dropping rows with missing values
df['Year'] = df['Timestamp'].dt.year
df['Month'] = df['Timestamp'].dt.month
df['Day'] = df['Timestamp'].dt.day
df['Hour'] = df['Timestamp'].dt.hour
df['Minute'] = df['Timestamp'].dt.minute
df['Second'] = df['Timestamp'].dt.second

features = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second', 'Temperature', 'Humidity', 'WindSpeed', 'WeatherObserved','DewpointTemp']
X = df[features].values
y = df['Grid'].values

under_sampler = RandomUnderSampler(random_state=42)

X, y = under_sampler.fit_resample(X, y)

scaler = MinMaxScaler()
X = scaler.fit_transform(X)
X = X.reshape(X.shape[0], 1, X.shape[1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

new_data = np.array([[2023, 6, 4, 15, 10, 0, 43, 14, 7, 0, 10]])  # Define the values after getting them from the weather API
#For Reference ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second', 'Temperature', 'Humidity', 'WindSpeed', 'WeatherObserved','DewpointTemp']

new_data = scaler.transform(new_data) # Normalize the new data using the loaded or fitted scaler

new_data = new_data.reshape(new_data.shape[0], 1, new_data.shape[1]) # Reshape the new data for LSTM input

predictions = model.predict(new_data) #Making predictions on the new data using the model 

threshold = 0.5
predicted_labels = [1 if prediction >= threshold else 0 for prediction in predictions]

# 'predicted_labels' now contains the predicted class labels for the new data
print("below me")
print(predicted_labels)
print("above me")
