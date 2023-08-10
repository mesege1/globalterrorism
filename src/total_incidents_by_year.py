import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_total_incidents_by_year_chart():
    """This code creates a bar graph showing the number of incidents by year from 2001 to 2017
    """
    # Load the data
    incidents_year_and_country = pd.read_csv('final_data.csv')
    
    # Group by year and calculate the sum of incident_count
    incidents_by_year = incidents_year_and_country.groupby('year')['incident_count'].sum().reset_index(name='sum')
    incidents_by_year = incidents_by_year.sort_values(by='year', ascending=False)
    incidents_by_year['year'] = incidents_by_year['year'].astype(int)
    
    # Sort the DataFrame by 'year' in descending order
    by_year = incidents_by_year.sort_values(by='year', ascending=False)
    
    # Create the horizontal bar chart
    plt.figure(figsize=(8, 5))
    sns.barplot(x='year', y='sum', data=by_year, palette='viridis_d')
    plt.xlabel('Year')
    plt.ylabel('Incident Count')
    plt.title('Total Number of Terror Incidents by Year (2001 - 2017)', fontsize=16, fontweight='bold')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('total_incidents_by_year.png') 
    plt.show()

if __name__ == "__main__":
    generate_total_incidents_by_year_chart()
