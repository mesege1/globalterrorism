import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import plotly.offline as py
import plotly.express as px
import plotly.graph_objs as go
import plotly.tools as tls
plt.style.use('fivethirtyeight')
import scipy.stats as stats
import statsmodels.api as sm
from scipy.stats import pearsonr, ttest_ind, ttest_1samp, norm, mannwhitneyu, t
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve, KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, precision_recall_curve, auc, classification_report
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
from sklearn.tree import DecisionTreeRegressor
import folium
import folium.plugins
import warnings 
warnings.filterwarnings('ignore')
py.init_notebook_mode(connected=True)
sns.set(style='whitegrid')

final_data = pd.read_csv('C:/Users/vans8/dai5/projects/globalterrorism/final_data.csv')

def generate_total_incidents_by_year_chart(data):
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

def plot_incidents_by_country(data):
    # Group by country and sum the incident counts
    incidents_by_country = data.groupby('country_txt')['incident_count'].sum().reset_index()
    
    # Sort by incident count in descending order
    incidents_by_country = incidents_by_country.sort_values(by='incident_count', ascending=False)
    
    # Plot the bar graph
    plt.figure(figsize=(12, 6))
    plt.bar(incidents_by_country['country_txt'].head(15), incidents_by_country['incident_count'].head(15), color='blue')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Country')
    plt.ylabel('Total Incident Count')
    plt.title('Total Incidents by Country')
    plt.tight_layout()
    plt.show()

def plot_heatmap(data):
    # Pivot table to create heatmap data
    heatmap_data = data.pivot_table(index='region_txt', columns='year', values='incident_count', aggfunc='sum')
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='YlOrRd', annot=True, fmt='g', linewidths=0.5, cbar_kws={'label': 'Incident Count'})
    plt.xlabel('Year')
    plt.ylabel('Region')
    plt.xticks(rotation=45, ha='center')
    plt.title('Heatmap: Terrorism Incidents by Region and Year (2001 - 2017)', pad=10)
    plt.tight_layout()
    plt.show()

def plot_lowest_average_gdp(data):
    average_gdp_countries = data.groupby('country_txt')['GDP per capita'].mean().reset_index()
    lowest_gdp_countries = average_gdp_countries.sort_values(by='GDP per capita', ascending=True).head(15)
    
    plt.figure(figsize=(10, 6)) 
    plt.barh(lowest_gdp_countries['country_txt'], lowest_gdp_countries['GDP per capita'], 
             color='red', alpha=0.8)
    plt.xlabel('Average GDP per capita')
    plt.title('15 Countries with the Lowest Average GDP per capita (2001 - 2017)', fontsize=15, fontweight='bold')
    plt.yticks(range(len(lowest_gdp_countries['country_txt'])), lowest_gdp_countries['country_txt'])
    plt.tight_layout()
    plt.show()
    
def plot_lowest_average_education(data):
    average_education_countries = data.groupby('country_txt')['education_level'].mean().reset_index()
    lowest_education_countries = average_education_countries.sort_values(by='education_level', ascending=True).head(15)
    
    plt.figure(figsize=(10, 6)) 
    plt.barh(lowest_education_countries['country_txt'], lowest_education_countries['education_level'], 
             color='purple', alpha=0.8)
    plt.xlabel('Average Education Level')
    plt.title('15 Countries with the Lowest Average Education Level (2001 - 2017)', fontsize=15, fontweight='bold')
    plt.yticks(range(len(lowest_education_countries['country_txt'])), lowest_education_countries['country_txt'])
    plt.tight_layout()
    plt.show()
    
def plot_education_heatmap(data):
    heatmap_data = data.pivot_table(index='region_txt', columns='year', values='education_level', aggfunc='mean')

    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='YlOrRd_r', annot=True, fmt='.1f', linewidths=0.5, cbar_kws={'label': 'Average Education Level'}, vmin=data['education_level'].min(), vmax=data['education_level'].max())
    plt.xlabel('Year')
    plt.ylabel('Region')
    plt.xticks(rotation=45, ha='center')
    plt.title('Heatmap: Average education level by region (2001 - 2017)', pad=12, fontsize=15, fontweight='bold')
    plt.show()

def plot_distribution(data, column_name, color):
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=20, edgecolor='black')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {column_name}')
    plt.grid(True)
    plt.show()
    
def plot_pairplot(data, variables):
    sns.set(style='whitegrid')
    sns.pairplot(data[variables], diag_kind='kde', plot_kws={'alpha': 0.7, 's': 70})
    plt.suptitle(', '.join(variables), fontsize=14, fontweight='bold', y=1.02)
    plt.show()
    
def plot_scatterplot(data, x_column, y_column, hue_column, title):
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x=x_column, y=y_column, hue=hue_column, palette='tab20', data=data)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title, fontsize=20, fontweight='bold')
    plt.grid(True)
    plt.legend(title=hue_column, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()
    
def plot_correlation_heatmap(data, columns):
    correlation_matrix = data[columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.xticks(ticks=range(len(columns)), labels=columns, rotation=45, ha='right')
    plt.yticks(ticks=range(len(columns)), labels=columns, ha='right')
    plt.show()

def perform_multiple_linear_regression(data):
    # Define independent & dependent variables
    X = final_data[['education_level', 'GDP per capita']]
    y = final_data['incident_count']

    # Add a constant column to X
    X = sm.add_constant(X)

    # Fit the multiple linear regression model
    model = sm.OLS(y, X).fit()

    # Print the summary
    print(model.summary())

def plot_regression_simplified(data, x_column, y_column):
    sns.set(style='whitegrid')
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data[x_column], y=data[y_column], color='blue', alpha=0.7)
    sns.regplot(x=data[x_column], y=data[y_column], scatter=False, color='red')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def perform_ttest_and_visualize(data1, data2, alpha=0.025, num_bootstrap_samples=1000):
    # Bootstrap samples function
    def bootstrap_samples(x, num_bootstrap_samples):
        bootstrap_samples = []
        for _ in range(num_bootstrap_samples):
            bootstrap_samples.append(np.mean(np.random.choice(x.squeeze(), size=len(x), replace=True)))
        return bootstrap_samples
    
    # Apply bootstrap samples function
    data1_bootstrap = bootstrap_samples(data1, num_bootstrap_samples)
    data2_bootstrap = bootstrap_samples(data2, num_bootstrap_samples)
    
    # Create distributions using bootstrap samples
    data1_distribution = norm(loc=np.mean(data1_bootstrap), scale=np.std(data1_bootstrap, ddof=1))
    data2_distribution = norm(loc=np.mean(data2_bootstrap), scale=np.std(data2_bootstrap, ddof=1))
    
    # Calculate critical values
    critical_value_data1 = data1_distribution.ppf(alpha)
    critical_value_data2 = data1_distribution.ppf(1 - alpha)
    
    # Perform t-test
    t_stat, p_value_ttest = ttest_ind(data1, data2)
    
    # KDE plots
    plt.figure(figsize=(8,6))
    sns.set(style='whitegrid')
    sns.kdeplot(data1_bootstrap, label='Sample 1')
    sns.kdeplot(data2_bootstrap, label='Sample 2')
    plt.axvline(critical_value_data1, color='red', linestyle='dashed', linewidth=2, label=f'Lower Critical Value: {critical_value_data1:.3f}')
    plt.axvline(critical_value_data2, color='red', linestyle='dashed', linewidth=2, label=f'Upper Critical Value: {critical_value_data2:.3f}')
    plt.xlabel('Data')
    plt.ylabel('Density')
    plt.title('Two samples T-test: Bootstrap and Critical Values', fontsize = 15, fontweight='bold')
    plt.legend(title=f"P-Value: {p_value_ttest:.3f}", loc='upper left')
    
    if p_value_ttest < alpha:
        plt.annotate('"Reject Null Hypothesis"', xy=(0.05, 0.55), xycoords='axes fraction', fontsize=14, color='red')
    else:
        plt.annotate('"Fail to Reject Null Hypothesis"', xy=(0.05, 0.55), xycoords='axes fraction', fontsize=14, color='green')
    plt.show()

def plot_qq_plot(data, title):
    sm.qqplot(data, line='s')
    plt.title(f'QQ Plot: {title}')
    plt.show()
 
def create_new_final_dataframe(dataframe):
    # Group by 'country_txt' and 'region_txt', and aggregate data
    aggregated_data = dataframe.groupby(['country_txt', 'region_txt']).agg({
        'incident_count': 'sum',
        'GDP per capita': 'mean',
        'education_level': 'mean'
    }).reset_index()
    
    # Add a constant column
    aggregated_data['constant'] = 1
    
    return aggregated_data

def calculate_highest_incidents_by_region(dataframe):
    X = dataframe[['GDP per capita', 'education_level', 'constant']]
    y = dataframe['incident_count']
    # Fit the linear regression model
    model = sm.OLS(y, X).fit()
    # Get the predicted incident count from the model
    dataframe['predicted_incident_count'] = model.predict(X)
    # Group the data by 'region_txt' and find the country with the highest predicted incident count in each region
    highest_incidents_by_region = dataframe.groupby('region_txt').apply(lambda group: group.loc[group['predicted_incident_count'].idxmax()])
    # Create a new variable with calculated prediction data
    result_regression = highest_incidents_by_region[['region_txt', 'country_txt', 'predicted_incident_count']]
    return result_regression

def create_bar_chart(dataframe):
    plt.figure(figsize=(10, 6))
    bar_width = 0.4
    highest_incidents_by_region_sorted = dataframe.sort_values(by='predicted_incident_count', ascending=True)
    index = np.arange(len(highest_incidents_by_region_sorted))

    # Create the bar chart
    bars = plt.barh(index, highest_incidents_by_region_sorted['predicted_incident_count'], 
                    height=bar_width, color='blue')

    plt.xlabel('Incident Count')
    plt.ylabel('Top Country per Region')
    plt.title('Countries with the highest predicted terrorism incident count in each region', fontsize=14, fontweight='bold')
    plt.yticks(index, highest_incidents_by_region_sorted['country_txt'])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Variables required for the following functions.
    gdp_cleaned = final_data['education_level']    
    variables_to_plot = ['GDP per capita', 'education_level', 'incident_count']   
    sub_sahara_education_data = final_data[final_data['region_txt'] == 'Sub-Saharan Africa']['education_level']
    north_america_education_data = final_data[final_data['region_txt'] == 'North America']['education_level']
    education_level = final_data['education_level']
    
    # Functions start below. 
    
    #generate_total_incidents_by_year_chart(final_data)
    #plot_incidents_by_country(final_data)
    #plot_heatmap(final_data)
    #plot_lowest_average_gdp(final_data)
    #plot_lowest_average_education(final_data)
    #plot_education_heatmap(final_data)
    #plot_distribution(gdp_cleaned, 'education_level', 'red')
    #plot_pairplot(final_data, variables_to_plot)
    #plot_scatterplot(final_data, 'education_level', 'incident_count', 'region_txt', 'Scatter Plot: Education Level vs. Incident Count by Region')
    #plot_correlation_heatmap(final_data, variables_to_plot)
    #perform_multiple_linear_regression(final_data)
    #plot_regression_simplified(final_data, 'education_level', 'incident_count')
    perform_ttest_and_visualize(sub_sahara_education_data, north_america_education_data)
    #plot_qq_plot(education_level, 'Education Level')
    new_final = create_new_final_dataframe(final_data)
    print(new_final)
    result = calculate_highest_incidents_by_region(new_final)
    print(result)
    create_bar_chart(result)