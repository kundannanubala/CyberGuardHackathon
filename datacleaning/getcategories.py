import pandas as pd

def get_categories():
    # Load the CSV file
    data = pd.read_csv('../train.csv')

    # Define the function to extract unique categories and handle NaN values in sub-categories
    def get_unique_categories(data):
        # Replace NaN values in 'sub_category' with an empty string or other value
        data['sub_category'] = data['sub_category'].fillna('')
        # Group by category and get unique sub-categories for each category
        categories = data.groupby('category')['sub_category'].unique()
        return categories.apply(list)  # Convert numpy arrays to lists

    # Call the function on the dataset
    categories_with_subcategories = get_unique_categories(data)

    # Save the result to a text file
    output_file = 'categories_and_subcategories.txt'

    with open(output_file, 'w') as f:
        f.write(f"\nNumber of categories: {len(categories_with_subcategories)}\n")
        
        # Iterate over each category and its sub-categories
        for category, subcategories in categories_with_subcategories.items():
            f.write(f"Category: {category}\n")
            f.write("Sub-categories:\n")
            # Handle case where there are no sub-categories (i.e., empty string)
            if len(subcategories) == 0 or (len(subcategories) == 1 and subcategories[0] == ''):
                f.write("  - No sub-categories (count: 0)\n")
            else:
                for sub_category in subcategories:
                    f.write(f"  - {sub_category}\n")
        f.write("\n")
    
        # Write number of sub-categories for each category
        f.write("-------------------------------------\nNumber of Sub-Categories for Each Category:\n\n")
        for category, subcategories in categories_with_subcategories.items():
            # Count as 0 if the sub-category is empty
            if len(subcategories) == 0 or (len(subcategories) == 1 and subcategories[0] == ''):
                count = 0
            else:
                count = len(subcategories)
            f.write(f"Category: {category}\n")
            f.write(f"Number of Sub-categories: {count}\n\n")

        print(output_file)  # Return the path to the saved file

def test_get_categories():
        # Load the CSV file
    data = pd.read_csv('../test.csv')

    # Define the function to extract unique categories and handle NaN values in sub-categories
    def get_unique_categories(data):
        # Replace NaN values in 'sub_category' with an empty string or other value
        data['sub_category'] = data['sub_category'].fillna('')
        # Group by category and get unique sub-categories for each category
        categories = data.groupby('category')['sub_category'].unique()
        return categories.apply(list)  # Convert numpy arrays to lists

    # Call the function on the dataset
    categories_with_subcategories = get_unique_categories(data)

    # Save the result to a text file
    output_file = 'test_categories_and_subcategories.txt'

    with open(output_file, 'w') as f:
        f.write(f"\nNumber of categories: {len(categories_with_subcategories)}\n")
        
        # Iterate over each category and its sub-categories
        for category, subcategories in categories_with_subcategories.items():
            f.write(f"Category: {category}\n")
            f.write("Sub-categories:\n")
            # Handle case where there are no sub-categories (i.e., empty string)
            if len(subcategories) == 0 or (len(subcategories) == 1 and subcategories[0] == ''):
                f.write("  - No sub-categories (count: 0)\n")
            else:
                for sub_category in subcategories:
                    f.write(f"  - {sub_category}\n")
        f.write("\n")
    
        # Write number of sub-categories for each category
        f.write("-------------------------------------\nNumber of Sub-Categories for Each Category:\n\n")
        for category, subcategories in categories_with_subcategories.items():
            # Count as 0 if the sub-category is empty
            if len(subcategories) == 0 or (len(subcategories) == 1 and subcategories[0] == ''):
                count = 0
            else:
                count = len(subcategories)
            f.write(f"Category: {category}\n")
            f.write(f"Number of Sub-categories: {count}\n\n")

    print(output_file)  # Return the path to the saved file
# get_categories()
test_get_categories()
