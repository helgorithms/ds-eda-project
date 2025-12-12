# -- import pd
import pandas as pd

# -- data cleaning function
def clean_data(df):
    """ Set default decimals to 2 """
    pd.options.display.float_format = '{:.2f}'.format           
    
    """ Set datetime type """
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')  
    
    """ Convert yr_renovated dtype to int """
    df['yr_renovated'] = (                                      
    pd.to_numeric(df['yr_renovated'], errors='coerce')          # convert invalid → NaN
      .fillna(0)                                                # replace NaN / inf
      .astype(int)                                              # convert to int
    )  
    
    """ Convert waterfront dtype to int """
    df['waterfront'] = (
    pd.to_numeric(df['waterfront'], errors='coerce')            # convert invalid → NaN
      .fillna(0)                                                # replace NaN / inf
      .astype(int)                                              # convert to int
    )
    
    """ Convert dtype to int """
    df['bedrooms'] = df['bedrooms'].astype(int)                 # -- convert to int

    """ Use this variable to refer to cleaned data frame """
    return df 