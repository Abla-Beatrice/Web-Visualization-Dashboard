import pandas as pd

# Read the csv file in
cities_df = pd.read_csv('Resources/cities.csv')

# Save to file
cities_df.to_html('data.html', index=False)

# Assign to string
table = cities_df.to_html()
print(table)