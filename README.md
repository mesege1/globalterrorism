# Exploring the Next Caliphate: A Prediction from the Global Terrorism Database
![START_GTD-Heatmap_2020](https://github.com/mesege1/globalterrorism/assets/135185712/eacb5468-9ef4-44f4-9ae1-ac7803c6571b)
# Table of Contents
1. Overview
2. Questions
3. About the data
4. Visualization
5. Statistical Test and Analysis
6. Prediction
7. Conclusion
8. Future data chanllenge
9. Proposed solution: Change conditions to influence future generations
## Overview
### What is Global War on Terror (GWOT)?
The War on Terror, or Global War on Terrorism (GWOT), was a global counterterrorism military campaign initiated by the United States after the September 11 attacks, with no official endpoint declared.

Since the beginning of the GWOT campaign, the United States has designated 50 new terrorist organizations which operate in different parts of the world. Despite persistent time and efforts to counter it, terrorism continuously reproduced itself regionally and globally because external forces cannot eradicate the ideology and root causes. Extremist groups have been conducting terrorist activities generation after generation because of what they believe and value. Over 20 years, multiple governments and intergovernmental organizations attempted to combat the global VEO problems. However, such efforts exacerbated the resistance movements and spread worldwide with different sects. Even though the U.S. withdrew from Afghanistan in 2021 and reduced boots on the ground from Iraq, the terrorism hasn't ended. And we don't know where would be the next Caliphate. 
## Questions
The social, economic, and cultural conditions are essential to the individuals belonging to society and form perceptions and moral compasses. Therefore, it is safe to evaluate that the lack of education, especially in unstable countries, does not improve the quality of life, creating vulnerabilities among the younger population. Meanwhile, Extremist groups have been conducting terrorist activities generation after generation because they teach, motivate, and inspire the next generation and continue to propagate what they believe. 

Therefore, we pose the following questions. 
- Does the education level affect participation in violent extremism activities? 
- Does the income level affect participation in violent extremism activities?
### We are trying to answer these questions statistically.
* Null Hypothesis (H0): Lack of education in developing countries has no significant relationship with participation in violent extremist activities.
* Alternative Hypothesis (H1): Lack of education in developing countries significantly relates to participation in violent extremist activities.
## About the data
- The primary dataset for this project is from the START Global Terrorism Database (https://www.start.umd.edu/research-projects/global-terrorism-database-gtd). The Global Terrorism Database (GTD) documents more than 200,000 international and domestic terrorist attacks worldwide since 1970. For this project, I used data from 2001 to 2017 to focus on Global War on Terrorism Campaign era more contemporarily. 
- The second dataset is from the World in Our Data, Section 3, "Years of Schooling" (https://ourworldindata.org/global-education#school-enrollment-and-attendance).
- The third dataset is from the World Bank, and it focuses on the GDP per capita and population by year (https://data.worldbank.org/indicator/NY.GDP.MKTP.CD).
- Once we selected columns of interest, we merged three datasets in one. We added new columns, such as 'incident per capita,' based on the original dataset. 
## Visualization
### Map of the terrorism incidents throughout the world separated by regions (2001 - 2017)
![terror_incidents_since_2001](https://github.com/mesege1/globalterrorism/assets/135185712/b7169931-78b1-4aa9-a9f6-96304f83da3c)
### Top 15 countries with the most terrorism incidents (2001 - 2017)
![top15_countries](https://github.com/mesege1/globalterrorism/assets/135185712/0521f184-b5df-42cd-baee-39f5a4b5b7a6)
- Overall, Global War on Terror designated countries, including Iraq and Afghanistan, have high incident numbers. 
### Total number of terrorism incidents by year (2001 - 2017)
![total_incident_by_year](https://github.com/mesege1/globalterrorism/assets/135185712/3628f59b-850a-4428-ac60-f29dc8642e9a)
- In 2014, the peak of the ISIS expansion in the Middle East and worldwide may contribute to increased incidents. 
### Heatmap of the education level by region
![heatmap_by_education_level](https://github.com/mesege1/globalterrorism/assets/135185712/5b5c0b4f-160e-43cc-a32f-a02952a53a54)
- Historically Central America, South Asia, and Sub-Saharan Africa had a low average education level.
### Heatmap of the GDP per capita by region
![heatmap_by_gdp](https://github.com/mesege1/globalterrorism/assets/135185712/d6fe2de1-b6a3-4381-a4ae-555fbfedbb43)
- Central America, Central Asia, South Asia, Southeast Asia, And Sub-Saharan Africa have generally low GDP per capita throughout the timeframe. 
## Statistical Test and Analysis
### The objectives:
The hypothesis determines whether the model is statistically significant and whether at least one independent variable significantly impacts the dependent variable.
### Step 1. Correlation check
![heatmap_three](https://github.com/mesege1/globalterrorism/assets/135185712/117b49dc-8492-42c4-9f95-43d8e0414c24)
- Positive correlation between 'education_level' and 'GDP per capita' (correlation coefficient: 0.693)
- Negative correlation between 'education_level' and 'incident_count' (correlation coefficient: -0.138)
- The correlation between 'GDP per capita' and 'incident_count' is weak (correlation coefficient: -0.119)
- Explanation: The education level and GDP per capita correlate. However, judging by the number, it appears both have a 'weak' correlation, which requires further investigation. However, the Education level and GDP has comparably stronger relationships.
### Step 2. Hypothesis testing (T-test)
#### What is the t-test? 
- It determines the sample data and its ability to provide valuable insights about the population.
- If the p-value is more significant than 0.05, it fails to reject the null hypothesis. In other words, there is insufficient evidence to conclude that the sample mean significantly differs from the hypothesized population mean.
### Education Level T-test
#### Two sample t-test between Southasia and Eastern Europe on Education level
![ttest_edu_sa_ea](https://github.com/mesege1/globalterrorism/assets/135185712/3ae7de6c-38c7-45a6-accd-ea507508a9b4)
- Result: Reject Null Hypothesis
#### Two sample t-test between Caribeean and South Asia on Education level
![ttest_edu_cari_sa](https://github.com/mesege1/globalterrorism/assets/135185712/571462a0-62df-4e3d-bce3-5159182c51aa)
- Result: Reject Null Hypothesis
### GDP per capita T-test
#### Two sample t-test between Western Europe and South America on GDP per capita
![ttest_gdp_we_sa](https://github.com/mesege1/globalterrorism/assets/135185712/a026685c-408c-42b4-bf2b-d12b37e4fe2a)
- Result: Reject Null Hypothesis
#### Two sample t-test between South Asia and North America on GDP per capita
![ttest_gdp_sa_na](https://github.com/mesege1/globalterrorism/assets/135185712/06868d43-4d60-4520-953d-57aaa4d5527b)
- Result: Reject Null Hypothesis
### T-test between high incident and low incident groups on Education level
![ttest_edu_high_low](https://github.com/mesege1/globalterrorism/assets/135185712/d7e058cf-3746-441f-a5b6-ea52fd0dda41)
- Result: Reject Null Hypothesis

![boxplot_education](https://github.com/mesege1/globalterrorism/assets/135185712/17a72d13-6d5f-4f90-af7e-3ee276d44da1)
- Observation: Low incident group has a higher median level (median incident: 23)
### T-test between high incident and low incident groups on GDP per capita
![ttest_gdp_high_low](https://github.com/mesege1/globalterrorism/assets/135185712/bc0d6e11-16a1-40b4-b3df-e244dc5010fe)
- Result: Reject Null Hypothesis

![boxplot_gdp_high_low](https://github.com/mesege1/globalterrorism/assets/135185712/eda9ab58-79bd-41a8-8ae0-6621ccd20311)
- Observation: The low incident group has a slightly higher median than the high incident group. The difference between the top quartile is more than $20,000.
### T-test summary
- According to multiple hypothesis tests, the p-value is smaller than 0.05, which indicates the test rejects the null hypothesis. In other words, lack of education in developing countries significantly relates to participation in violent extremist activities.
### Step 3. Linear regression model
- Based on this t-test result, we built two linear regression models (Education and GDP per capita).
##### Linear regression line on Education level
![linear_regression_with_scatter_plot](https://github.com/mesege1/globalterrorism/assets/135185712/bc41b827-8299-41de-b0b5-dc65873cfa73)
- When the regression line is low, the line has a low Y-intercept, and the slope is relatively shallow. In practical terms, this means that for a given increase in the independent variable (X), the dependent variable (Y) increases only slightly. In other words, the variables have a positive correlation, but the relationship is not very strong.
##### Linear regression line on GDP per capita
![linear_regression_gdp_incident](https://github.com/mesege1/globalterrorism/assets/135185712/3fe3d0bf-c010-4af5-ba42-662cece483b9)
- The same goes for the GDP per capita and incident count relationship. It has a positive but weak relationship, which indicates less predictive power. The same goes for the GDP per capita and incident count relationship. It has a positive but weak relationship, which indicates less predictive power. With more features, it would build a better model. However, this project only deals with education level and GDP per capita. 
# Prediction
### Top 5 countries per region
![top5_per_region](https://github.com/mesege1/globalterrorism/assets/135185712/c913d1f9-676e-48b3-9830-367d6c17e3bb)
- With the given regression model, we applied it to the Global Terrorism dataset. The graphs show the top 5 countries within the regions with low GDP and education levels.
### Countries with the highest predicted terrorism incident count in each region
![prediction](https://github.com/mesege1/globalterrorism/assets/135185712/0d6d3cb0-743a-4a0d-8aff-1fb8246077a7)
### Top 10 countries with the highest prediction (regardless of region)
![top 10 prediction](https://github.com/mesege1/globalterrorism/assets/135185712/656423b8-6756-4d05-95d7-4a9eaede5117)
#### Cross validation (K-fold)
- K-fold cross-validation is a valuable tool to assess the generalization performance of a model and gain confidence in its ability to perform well on new, unseen data.

![kfold_results](https://github.com/mesege1/globalterrorism/assets/135185712/0f3c1a94-013a-482e-9c8a-409efa709928)
#### Residual Analysis
- Residual analysis helps identify outliers in the data. Outliers are data points that significantly deviate from the general trend. High residual values can indicate the presence of outliers, which may be influential in affecting the model's performance and predictions.
![residual_analysis](https://github.com/mesege1/globalterrorism/assets/135185712/8f42f32d-11cb-4e8d-9da3-ec81f5c8bf2b)
- The residual analysis shows this dataset has higher residual values with many outliers. It may affect the model's performance and predictions.
## Conclusion
There are multi-facets of social factors that contribute to violent extremism. This project reviewed terrorism activities during the GWOT era and found correlations between education level, GDP per capita, and terrorism incidents. Although we found a weak relationship between features (education level & GDP) and the target (incident count), we identified the patterns of two social factors and applied the model to future prediction.
## Future data chanllenge 
- The current data exploration revealed the possibility of more significant social factors contributing to violent extremism. Without changes, the status quo repeats. Therefore, the focus must emphasize discovering whether unequal social status and lack of opportunities cause vulnerable children to join VEOs and, if so, how to mitigate them from being influenced by extremist groups. In addition, further analyses must explore how to implement and improve the education system in unstable countries while preserving their cultural values and traditions.
- Future data exploration example; 1) "Not in Education, Employment, or Training" (NEET), 2) child labor index, or 3) any other children's risk index. Once we find the correlation, we can implement the support plan.
## Proposed solutions: Change conditions for long-term effect
![image](https://github.com/mesege1/globalterrorism/assets/135185712/271a7c23-7d1d-4bfe-9e8e-9371603e86af)
(Children in Syrian Al-hol refugee camp, source: https://www.rudaw.net/english/opinion/12092022)

### 1) Embed the Quality Education in the Military Cooperation
- Multiple United States military service members are currently deployed to numerous countries to support counterterrorism operations. Many developing countries are combating contemporary VEO issues, such as Iraq, Libya, Somalia, Niger, and the Philippines, which have established cooperative military relationships with the United States and received structured training and logistical support. Providing them with a quality education would increase the level of individual education and extend the capacities and capabilities of the host nation, which satisfies the U.S. objectives. Most importantly, it reduces VEO influences in the regions by changing conditions and providing opportunities and motivations to serve the armed forces against terrorism. It also positively changes the public perception and increases support for the host nation's armed forces.
### 2) Increase Awareness of the Effective Utilization of Technology
- Providing education, especially for a specific group, is only a partial solution to a complex problem. Developing and unstable countries face more challenges regarding job opportunities due to a lack of resources. Utilizing technology could tighten the opportunity gaps in child education and job availability between developed and unstable countries and solve the global extremist problem, which the many IGOs, such as the U.N., emphasize as an objective for sustainable development.
### 3) Develop Infrastructure for Fair Information Accessibility
- The right to education is a fundamental human right assured by multiple international organizations and treaties. Article 26 of the Universal Declaration of Human Rights states, "Everyone has the right to education. Education shall be free, at least in the elementary and fundamental stages". However, according to UNESCO Institute for Statistics (UIS), about 258 million children are out of school, comprising one-sixth of this age group in 2018. Developing IT infrastructure and improving access to information would preserve children's education rights and substitute the shortage of physical schools and education institutes. In addition, social connectivity through the IT system enables charities and intergovernmental organizations to access people in need via network and to provide quality education without physical presence. 
