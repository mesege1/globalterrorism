import pandas as pd
import numpy as np

def create_final_data():
    # Load data from File 1
    terror = pd.read_csv('data/globalterrorismdb_0718dist.csv', encoding='ISO-8859-1', dtype="object")
    new_terror = terror[['iyear', 'country_txt', 'region_txt', 'latitude', 'longitude', 'attacktype1_txt', 'gname']].copy()
    new_terror['year'] = pd.to_numeric(new_terror['iyear'])
    new_terror.drop(columns='iyear', inplace=True)
    new_terror_after_2000 = new_terror[new_terror['year'] >= 2001].copy()
    new_column_order = ['year', 'country_txt', 'region_txt', 'latitude', 'longitude', 'attacktype1_txt', 'gname']
    new_terror_after_2000 = new_terror_after_2000.reindex(columns=new_column_order)
    incidents_year_and_country = new_terror_after_2000.groupby(['year', 'country_txt', 'region_txt']).size().reset_index(name='incident_count')
    total_incidents_by_country = incidents_year_and_country.groupby(['country_txt', 'region_txt'])['incident_count'].sum().reset_index(name='total_incidents')
    total_incidents_by_country = total_incidents_by_country.sort_values(by='total_incidents', ascending=False)

    # Load data from File 2
    gdp_capita = pd.read_csv('data/per_capita.csv')
    gdp_filtered = gdp_capita[(gdp_capita['Year'] >= 2001) & (gdp_capita['Year'] <= 2017)]
    gdp_filtered.drop(gdp_filtered.columns[[1, 3, 5, 7]], axis=1, inplace=True)
    gdp = gdp_filtered.dropna()

    # Merge data from File 1 and File 2
    incident_gdp = pd.merge(incidents_year_and_country, gdp, left_on=['country_txt', 'year'], right_on=['Entity', 'Year'])
    incident_gdp.drop(columns=['Entity', 'Year'], inplace=True)
    incident_gdp.rename(columns={'Population (historical estimates)': 'population'}, inplace=True)
    incident_gdp['incident_per_capita'] = incident_gdp['incident_count'] / incident_gdp['population']

    # Load data from File 3
    education = pd.read_csv('data/mean-years-of-schooling-long-run.csv')
    education_after_2000 = education[(education['Year'] >= 2001) & (education['Year'] <= 2017)]
    education_after_2000.rename(columns={'Average Total Years of Schooling for Adult Population (Lee-Lee (2016), Barro-Lee (2018) and UNDP (2018))': 'education_level'}, inplace=True)
    education_after_2000 = education_after_2000.drop(columns='Code')

    # Merge previously merged data with data from File 3
    incident_gdp_edu = pd.merge(incident_gdp, education_after_2000, left_on=['year', 'country_txt'], right_on=['Year', 'Entity'], how='left')
    average_education_level = incident_gdp_edu['education_level'].mean()
    incident_gdp_edu['education_level'].fillna(average_education_level, inplace=True)
    incident_gdp_edu = incident_gdp_edu.drop(columns=['Entity', 'Year'])

    # Rename the final dataframe
    final_data = incident_gdp_edu

    # Save the final dataframe to a CSV file
    final_data.to_csv('final_data.csv', index=False)




if __name__ == "__main__":
    create_final_data()
    
    

final_data = pd.read_csv('final_data.csv')
