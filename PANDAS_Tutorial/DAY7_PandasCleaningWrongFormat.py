
# Pandas - Cleaning Data of wrong Format


# Data of Wrong Format - Cells with data of wrong format can make it difficult, or even impossible to analyze data.

# To fix it, you have to options: remove the rows, or convert all cells in the columns into the same format.


# Example: Convert to date - Pandas has a to_dateime() method for this.

import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.dropna(subset=['Date'], inplace = True)

print(df.to_string())



# Cleaning Wrong Data - Wrong data does not have to be emtpy cells or wrong format
# it can just be wrong, like if someone registered "199" instead of "1.99"


# Replacing Values - One way to fix wrong values is to replace them with something else.

# Set "Duration"  = 45 in row 7
import pandas as pd
df = pd.read_csv('data.csv')

df.loc[7,'Duration'] = 45

print(df.to_string())





#