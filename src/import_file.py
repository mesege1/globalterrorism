import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

def main():
    # Load with pandas dataframe
    terror = pd.read_csv('data/globalterrorismdb_0718dist.csv', encoding='ISO-8859-1', dtype="object")
        
    # Select columns for the EDA
    new_terror = terror[['iyear', 'country_txt', 'region_txt', 'latitude', 'longitude', 'attacktype1_txt', 'gname']].copy()

    # Add 'year' column for same values from the 'iyear'
    new_terror['year'] = pd.to_numeric(new_terror['iyear'])

    # Drop iyear column
    new_terror.drop(columns='iyear', inplace=True)

    # Set the dataframe parameter from 2001 to 2017
    new_terror_after_2000 = new_terror[new_terror['year'] >= 2001].copy()

    # Reset the column order for easier navigation
    new_column_order = ['year', 'country_txt', 'region_txt', 'latitude', 'longitude', 'attacktype1_txt', 'gname']
    new_terror_after_2000 = new_terror_after_2000.reindex(columns=new_column_order)
    
    return new_terror_after_2000

if __name__ == "__main__":
    processed_data = main()
    print(processed_data) 
