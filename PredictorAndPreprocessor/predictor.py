#------------------------------------------------------------Weather API to File Code Below ------------------------------------------------------#
import requests
import pandas as pd

#api_key = '2c32a4be8e2b46939394d55c72a1f816'
#latitude = '33.738045'
#longitude = '73.084488'

# Endpoint for API
endpoint = 'https://api.weatherbit.io/v2.0/forecast/hourly?lat=33.6844&lon=73.0479&key=2c32a4be8e2b46939394d55c72a1f816&hours=24'

try:
    # Making the API request
    response = requests.get(endpoint)

    # if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Create a DataFrame from the API data
        df = pd.DataFrame(data['data'])

        # Extracting the necessary columns
        df = df[['timestamp_local', 'temp', 'rh', 'wind_spd', 'weather', 'dewpt']]

        # Extracting 'description' from the 'weather' column
        df['weather_description'] = df['weather'].apply(lambda x: x['description'])

        # Drop the original 'weather' column
        df = df.drop(columns=['weather'])

        # Rename columns
        df.columns = ['Time', 'Temperature', 'Humidity', 'WindSpeed', 'WeatherObserved', 'DewpointTemp']

        # Swap last to columns to arrange data as in ML traing dataset
        df['Time'], df ['Temperature'], df['Humidity'], df['WindSpeed'], df['DewpointTemp'], df['WeatherObserved'] = df['Time'], df ['Temperature'], df['Humidity'], df['WindSpeed'],  df['WeatherObserved'], df['DewpointTemp']

        # Adjusting weather observed 
        df['WeatherObserved'] = 0

        # Save the DataFrame to an XLSX file
        filename = 'weather_data_dayahead.xlsx'
        df.to_excel(filename, index=False)

        #print(f"Data saved to {filename}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

except Exception as e:
    print(f"An error occurred: {str(e)}")




# Load the Excel file containing the timestamp column
df = pd.read_excel('weather_data_dayahead.xlsx', engine='openpyxl')

# Assuming the timestamp column is named 'Timestamp', you can replace it with your actual column name
timestamp_column = 'Time'

# Convert the column to datetime format
df[timestamp_column] = pd.to_datetime(df[timestamp_column])

# Save the updated DataFrame with time components to a new Excel file
df.to_excel('weather_data_dayahead.xlsx', index=False, engine='openpyxl')





# Load the Excel file containing the timestamp column
df = pd.read_excel('weather_data_dayahead.xlsx', engine='openpyxl')

# Assuming the timestamp column is named 'Timestamp', you can replace it with your actual column name
timestamp_column = 'Time'

# Extract and create separate columns for time components
df['Year'] = df[timestamp_column].dt.year
df['Month'] = df[timestamp_column].dt.month
df['Day'] = df[timestamp_column].dt.day
df['Hour'] = df[timestamp_column].dt.hour
df['Minute'] = df[timestamp_column].dt.minute
df['Second'] = df[timestamp_column].dt.second


# Define a list of columns to remove
columns_to_remove = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second']  # Add the column names you want to remove


# Reorder the columns with the new time components at the beginning
new_order = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second'] + [col for col in df.columns if col != timestamp_column and col not in columns_to_remove]
df = df[new_order]

# Save the updated DataFrame with time components to a new Excel file
df.to_excel('weather_data_dayahead.xlsx', index=False, engine='openpyxl')









#------------------------------------------------------------ML Predictor Code Below------------------------------------------------------#








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


# Loading the end Excel file
predicted_df = pd.read_excel('TotalLoadperHour.xlsx', engine='openpyxl')

predicted_labels_list = []

for i in range(24):

    # Load the new data from another Excel file
    new_data_df = pd.read_excel('weather_data_dayahead.xlsx', engine='openpyxl')

    #Pick the i'th row, from row no 1 to 24 for complete day 
    selected_row = new_data_df.iloc[i:i+1]

    # Conversion into ndarray from df
    selected_row = selected_row.values

    #Converting from floating no to Integer, truncate the floating points 
    selected_row = selected_row.astype(int)

    new_data = selected_row

    new_data = scaler.transform(new_data) # Normalize the new data using the loaded or fitted scaler
    new_data = new_data.reshape(new_data.shape[0], 1, new_data.shape[1]) # Reshape the new data for LSTM input

    predictions = model.predict(new_data) #Making predictions on the new data using the model 

    threshold = 0.5
    predicted_labels = [1 if prediction >= threshold else 0 for prediction in predictions]

    # Append the predicted labels to the list
    predicted_labels_list.append(predicted_labels[0])


# Write to the appropriate column with the predicted labels 
predicted_df['RandomPrediction'] = predicted_labels_list

# Save the updated DataFrame back to the same Excel file
predicted_df.to_excel('TotalLoadperHour.xlsx', index=False, engine='openpyxl')