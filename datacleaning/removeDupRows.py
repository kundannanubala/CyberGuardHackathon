import pandas as pd

# Define a function to remove duplicate rows based on the content of the entire row
def remove_duplicates(data):
    # Remove duplicate rows
    cleaned_data = data.drop_duplicates()
    return cleaned_data

# Example usage
# data = pd.read_csv('cleaned_wrapped_text_train.csv')  # Load your CSV file
# cleaned_data = remove_duplicates(data)  # Remove duplicates

# # Save the cleaned data to a new CSV file
# output_file = 'cleaned_no_duplicates_train.csv'
# cleaned_data.to_csv(output_file, index=False)
#print(f"Cleaned data without duplicates saved to {output_file}")
test_data = pd.read_csv('../test.csv')  # Load your CSV file
test_cleaned_data = remove_duplicates(test_data)  # Remove duplicates

test_output_file = 'cleaned_no_duplicates_test.csv'
test_cleaned_data.to_csv(test_output_file, index=False)


print(f"Cleaned test data without duplicates saved to {test_output_file}")
