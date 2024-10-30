import pandas as pd
import re

# Load the CSV file
data = pd.read_csv('../train.csv')

# Define the function to remove rows with empty 'crimeaditionalinfo' and handle wrapped text
def clean_wrapped_text(data):
    # Replace NaN values in 'crimeaditionalinfo' with an empty string
    data['crimeaditionalinfo'] = data['crimeaditionalinfo'].fillna('')
    
    # Remove line breaks and replace them with a space
    data['crimeaditionalinfo'] = data['crimeaditionalinfo'].apply(lambda x: re.sub(r'[\r\n]+', ' ', x))
    
    # Remove any special or hidden characters
    data['crimeaditionalinfo'] = data['crimeaditionalinfo'].apply(lambda x: re.sub(r'[^\x20-\x7E]', '', x))
    
    # Remove rows where 'crimeaditionalinfo' is still empty after cleaning
    cleaned_data = data[data['crimeaditionalinfo'].str.strip() != '']
    return cleaned_data

# Clean the data
cleaned_data = clean_wrapped_text(data)

# Save the cleaned data to a new CSV file
output_file = 'cleaned_wrapped_text_train.csv'
cleaned_data.to_csv(output_file, index=False)

print(f"Cleaned data saved to {output_file}")
