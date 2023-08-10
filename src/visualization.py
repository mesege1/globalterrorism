from merged_file import final_data
import pandas as pd
import matplotlib.pyplot as plt

def plot_lowest_avg_gdp(final_data, num_countries=15):
    """
    Plot countries with the lowest GDP per capita
    """
    
    average_gdp_countries = final_data.groupby('country_txt')['GDP per capita'].mean().reset_index()
    lowest_gdp_countries = average_gdp_countries.sort_values(by='GDP per capita', ascending=True).head(num_countries)
    
    plt.figure(figsize=(10, 6))
    plt.barh(lowest_gdp_countries['country_txt'], lowest_gdp_countries['GDP per capita'],
             color='red', alpha=0.8)
    plt.xlabel('Average GDP per capita')
    plt.title(f'{num_countries} Countries with the Lowest Average GDP per capita (2001 - 2017)', fontsize=15, fontweight='bold')
    plt.yticks(range(len(lowest_gdp_countries['country_txt'])), lowest_gdp_countries['country_txt'])
    plt.tight_layout()
    plt.show()
    
def plot_lowest_education(final_data):
    """
    Plot countries with the lowest GDP per capita
    """
    
    # Calculate average education level by country
    average_education_countries = final_data.groupby('country_txt')['education_level'].mean().reset_index()
    # Sort and select the lowest education level countries
    lowest_education_countries = average_education_countries.sort_values(by='education_level', ascending=True).head(15)

    # Plot the bar chart for lowest education level countries
    plt.figure(figsize=(10, 6)) 
    plt.barh(lowest_education_countries['country_txt'], lowest_education_countries['education_level'], 
             color='purple', alpha=0.8)
    plt.xlabel('Average Education Level')
    plt.title('15 Countries with the Lowest Average Education Level (2001 - 2017)', fontsize=15, fontweight='bold')
    plt.yticks(range(len(lowest_education_countries['country_txt'])), lowest_education_countries['country_txt'])
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load the final_data DataFrame here
    #plot_lowest_avg_gdp(final_data)
    plot_lowest_education(final_data)
    
