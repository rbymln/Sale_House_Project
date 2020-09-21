import pandas as pd
import numpy as np

#visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#statistic
from scipy import stats

#encoder

import warnings 
warnings.filterwarnings("ignore")

def ambilcsv():
    return pd.read_csv("../../Data/Raw/kc_house_data.csv",usecols=['date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated'])
