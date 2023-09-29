import pandas as pd

  
# initialize list of lists
data1 = [[1, "Joe"], [2, 'Henry'], [3, 'Sam'],[4, 'Max']]
data2 = [[1, 2], [3, 1]]

# Create the pandas DataFrame
df1 = pd.DataFrame(data, columns=['id', 'Name'])
  
# print dataframe.
df