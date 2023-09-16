## 1. Title and Author

**Project Title:** Customer Churn Prediction

Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang

**Author Name:** Jaspreet Singh Bhatia

**GitHub:** https://github.com/jaspreet007singh

**LinkedIn:** https://www.linkedin.com/in/jsbhatia7/

**PowerPoint presentation file:**

**Link to your YouTube video:** 
    
## 2. Background

**What is the Project about?**

Customer churn, also known as customer attrition or customer turnover, is a critical business metric that refers to the phenomenon where customers or subscribers discontinue their engagement with a company's products or services. It is a pivotal concern for businesses across various industries, as retaining existing customers is often more cost-effective and profitable than acquiring new ones. High churn rates can significantly impact a company's revenue, growth prospects, and overall sustainability. Therefore, understanding the factors that drive customer churn and developing effective strategies to mitigate it are crucial objectives for any data-driven organization.


**Why does it matter?**


In the context of the data science project, the investigation of customer churn typically involves the analysis of historical customer data, encompassing variables such as customer demographics, charges, transaction history, and customer feedback. Data scientists employ a variety of predictive modelling techniques, including machine learning algorithms, to develop accurate churn prediction models. These models not only help in identifying customers at risk of churn but also provide valuable insights into the underlying causes, enabling businesses to take proactive measures to retain valuable customers and optimize their operations for sustained growth and profitability.

**What are your research questions?**


I am going to build a basic model for predicting customer churn using Telco Customer Churn dataset. I am using some classification algorithm to model customers who have left, using Python tools such as pandas for data manipulation and matplotlib for visualizations..

## 3. Data 

**Describe the datasets you are using to answer your research questions:**

**Data sources:** - https://www.kaggle.com/datasets/blastchar/telco-customer-churn?resource=download

**Data size (MB, GB, etc.):** - 955 Kb

**Data shape (# of rows and # columns) :** - (7043, 21) i.e. 7043 rows and 21 columns

**Time period:** - N/A

**What does each row represent?** 

- Each row represents the values of 21 different columns in which 4 are numerical and 16 are categorical (excluding Customer Id).

**Data dictionary:**

- **customerID**
  - Data type: Categorical
  - Definition: Unique customer ID.
  - Potential values: Id numbers like “6840-RESVB”

- **gender**
  - Data type: Categorical
  - Definition: Gender of customers.
  - Potential values: Male or Female

- **SeniorCitizen**
  - Data type: Numerical (Integer)
  - Definition: Shows if the customer is a Senior citizen or not.
  - Potential values: 0 or 1
 
- **Partner**
  - Data type: Categorical
  - Definition: Whether the customer has a partner or not.
  - Potential values: Yes or No

- **Dependents**
  - Data type: Categorical
  - Definition: Whether the customer has dependents or not.
  - Potential values: Yes or No

- **tenure**
  - Data type: Numerical (Integer)
  - Definition: Time duration (months) for which the customer has been with the company.
  - Potential values: 0 to 72

- **PhoneService**
  - Data type: Categorical
  - Definition: If the customer has Phone service or not.
  - Potential values: Yes or No

- **MultipleLines**
  - Data type: Categorical
  - Definition: If the customer has Multiple lines or not.
  - Potential values: Yes,No, No Phone Service

- **InternetService**
  - Data type: Categorical
  - Definition: Type of Internet service owned by customer.
  - Potential values: ‘DSL’, ‘Fiber Optic’ and ‘No’

- **OnlineSecurity**
  - Data type: Categorical
  - Definition: If the customer had Online Security or not.
  - Potential values: Yes, No, No internet service

- **OnlineBackup**
  - Data type: Categorical
  - Definition: If the customer had Online Backup or not.
  - Potential values: Yes, No, No internet service

- **DeviceProtection**
  - Data type: Categorical
  - Definition: If the customer had Device protection or not
  - Potential values: Yes, No, No internet service

- **TechSupport**
  - Data type: Categorical
  - Definition: If the customer had Tech Support or not
  - Potential values: Yes, No, No internet service

- **StreamingTV**
  - Data type: Categorical
  - Definition: If the customer had Streaming TV or not.
  - Potential values: Yes, No, No internet service

- **StreamingMovies**
  - Data type: Categorical
  - Definition: If the customer had Streaming TV or not.
  - Potential values: Yes, No, No internet service

- **Contract**
  - Data type: Categorical
  - Definition: Type of contracts of customers. 
  - Potential values: 'Month-to-month', 'One year’, 'Two year'

- **PaperlessBilling**
  - Data type: Categorical 
  - Definition: If the customer has enabled Paperless Billing or not.
  - Potential values: Yes or No

- **PaymentMethod**
  - Data type: Categorical
  - Definition: Type of Payment Method used by customer.
  - Potential values: 'Bank transfer (automatic)', 'Credit card (automatic)','Electronic check', ‘Mailed check'

- **MonthlyCharges**
  - Data type: Numerical (Float)
  - Definition: Indicates the monthly charges to customers.
  - Potential values: 18.25 to 118.75

- **TotalCharges**
  - Data type:Categorical but will be changing it into Numerical (Float)
  - Definition: Indicates the Total charges to customers.
  - Potential values: Random numeric values

- **Churn**
  - Data type: Categorical
  - Definition: Indicates if the customer churned or not.
  - Potential values: Yes or No

**Which variable/column will be your target/label in your ML model?**
-	Churn

**Which variables/columns may be selected as features/predictors for your ML models?**
 - Tenure
 - MonthlyCharges
 - TotalCharges

