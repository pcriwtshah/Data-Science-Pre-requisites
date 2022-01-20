import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
#%matplotlib inline --> A magic command used in iPython, and Jupyter Notebook/Lab to allow plots to be displayed without calling the .show() function.
import seaborn as sns
print("Setup Complete")

# Path of the file to read
#fifa_filepath = "fifa.csv"
with open('fifa.csv', 'r') as f:
    fifa_file = f.read()
    print(fifa_file)

'''
# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_file, index_col="Date", parse_dates=True)
print(pd.array(fifa_data))
'''