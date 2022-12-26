# Data-Science-Salary-Estimate

Data Science Salary Estimate from glassdoor

# Data Cleaning

clean it up so that it was usable for our model. I made the following changes and created the following variables:
- Parsed numeric data out of salary
- Made columns for employer provided salary and hourly wages
- Removed rows without salary
- Parsed rating out of company text
- Made a new column for company state
- Added a column for if the job was at the company’s headquarters
- Transformed founded date into age of company
- Made columns for if different skills were listed in the job description:
  - Python
  - R
  - Excel
  - AWS
  - Spark
  - Column for simplified job title and Seniority
  - Column for description length
  
# EDA

I looked at the distributions of the data and the value counts for the various categorical variables.
 
# Model Building

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried three different models:

- Multiple Linear Regression – Baseline for the model
- Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
- Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.

# Model Performance

The Random Forest model far outperformed the other approaches on the test and validation sets.

- Random Forest : MAE = 11.22
- Linear Regression: MAE = 18.86
- Ridge Regression: MAE = 19.67

# Production

In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.

# Credit

I like to thank Ken Jee for his guidance also I have used this guide for flask api : (https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2)
