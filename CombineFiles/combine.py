import pandas as pd 

# Load the datasets
states = pd.read_excel('states.xlsx')
dataset = pd.read_excel('US Sales Datasets.xlsx')

# Initialize Longitude and Latitude columns with default values (e.g., 0)
dataset['Longitude'] = 0
dataset['Latitude'] = 0

# Add a new 'Number' column to store the sequence of numbers
dataset['Number'] = range(1, len(dataset) + 1)

# Reorder the columns to make 'Number' the first column
columns = ['Number'] + [col for col in dataset.columns if col != 'Number']
dataset = dataset[columns]

# Loop through each state in the dataset
for idx, state in dataset.iterrows():
    # Find the matching state in the 'states' DataFrame
    for i in range(len(states["name"])):
        # idx refers to the current row you are iterating through
        # .at accesses a single value for row/column pair 
        if states['name'][i] == state['State']:  # Match based on the 'State' column
            dataset.at[idx, 'Longitude'] = states['longitude'][i]  # Assign longitude
            dataset.at[idx, 'Latitude'] = states['latitude'][i]    # Assign latitude

# Save the updated dataset to a new Excel file
dataset.to_excel("output.xlsx", index=False)
