import pandas as pd

def train_class_imbalance():
    # Load the newly provided CSV file to inspect its contents
    cleaned_data_path = 'cleaned_no_duplicates_train.csv'
    cleaned_data = pd.read_csv(cleaned_data_path)

    # Define a function to check for class imbalance in the 'category' column
    def check_class_imbalance(data):
        # Get the count of each category
        category_counts = data['category'].value_counts()
        # Calculate the percentage of each category
        category_percentage = (category_counts / category_counts.sum()) * 100
        # Combine the counts and percentages in a DataFrame
        imbalance_df = pd.DataFrame({'Count': category_counts, 'Percentage': category_percentage})
        return imbalance_df

    # Check for class imbalance in the 'category' column
    class_imbalance = check_class_imbalance(cleaned_data)

    # Save the class imbalance information to a CSV file
    class_imbalance.to_csv('no_dup_class_imbalance_overview.csv', index=True)  # Save to CSV

    # Display the class imbalance information (removed ace_tools)
    print(class_imbalance)  # Print to console

def test_class_imbalance():
    
    # Load the newly provided CSV file to inspect its contents
    cleaned_data_path = '../test.csv'
    cleaned_data = pd.read_csv(cleaned_data_path)

    # Define a function to check for class imbalance in the 'category' column
    def check_class_imbalance(data):
        # Get the count of each category
        category_counts = data['category'].value_counts()
        # Calculate the percentage of each category
        category_percentage = (category_counts / category_counts.sum()) * 100
        # Combine the counts and percentages in a DataFrame
        imbalance_df = pd.DataFrame({'Count': category_counts, 'Percentage': category_percentage})
        return imbalance_df

    # Check for class imbalance in the 'category' column
    class_imbalance = check_class_imbalance(cleaned_data)

    # Save the class imbalance information to a CSV file
    class_imbalance.to_csv('test_class_imbalance_overview.csv', index=True)  # Save to CSV

    # Display the class imbalance information (removed ace_tools)
    print(class_imbalance)  # Print to console

# train_class_imbalance()
test_class_imbalance()
