import pandas as pd

# df = pd.read_csv(filepath_or_buffer = 'data\FoodPrice_in_Turkey.csv', sep = ',')
# print(df.head())

# df = pd.read_excel('data\house_price_dống-da.xlsx')
# print(df.head())

# df = pd.read_json('data\FoodPrice_in_Turkey.json')
# print(df.head())

# df=pd.read_hdf('FoodPrice.h5', 'table')
# print(df.head())

url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_North_America'
df = pd.read_html(url)
print(df[0].head())