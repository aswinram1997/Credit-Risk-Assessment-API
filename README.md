# Credit-Risk-Asessment-API

![kenny-eliason-8fDhgAN5zG0-unsplash](https://github.com/aswinram1997/Insightful_Clusters_App/assets/102771069/06c171a5-0f57-4b2d-9cca-37ed235251fd)


## Project Overview
The project aims to develop a credit risk assessment ML model using a[Kaggle Dataset](<https://www.kaggle.com/datasets/laotse/credit-risk-dataset>) that predicts the likelihood of loan default based on various applicant features. The model is exposed as a containerized API, allowing internal bank applications and systems to request credit risk assessments for loan applicants. The model's predictions will assist in making efficient and well-informed lending decisions minimizing financial losses and strengthen the bank's overall financial stability.

## Dataset Overview
The [Kaggle Dataset](<https://www.kaggle.com/datasets/laotse/credit-risk-dataset>) used for the project has 32581 records and includes several features that capture relevant information about loan applicants. These features are as follows:

- person_age: Age of the loan applicant.
- person_income: Annual income of the loan applicant.
- person_home_ownership: Home ownership status of the loan applicant.
- person_emp_length: Employment length of the loan applicant in years.
- loan_intent: Purpose or intent of the loan.
- loan_grade: Grade assigned to the loan based on creditworthiness.
- loan_amnt: Loan amount requested by the applicant.
- loan_int_rate: Interest rate associated with the loan.
- loan_status: Loan status, where 0 represents non-default and 1 represents default.
- loan_percent_income: The percentage of income that the loan amount represents.
- cb_person_default_on_file: Historical default status of the loan applicant.
- cb_preson_cred_hist_length: Length of the loan applicant's credit history.

## Methodology
The project follows a typical machine learning workflow consisting of exploratory data analysis (EDA), data splitting, preprocessing, modeling, and evaluation. Additionally, a comparison of tree-based algorithms, including Random Forest, XGBoost, LightGBM, and a Deep Neural Network (DNN), was performed to determine the winning model. The chosen model was then utilized to build a FAST API endpoint. Finally, the API endpoint was containerized using Docker for scalability. The resulting containerized API provides an accessible and scalable solution for credit risk assessment, contributing to efficient loan processing, accurate risk evaluation, and enhanced decision-making within the bank.

#### Exploratory Data Analysis (EDA):
EDA was conducted on the dataset to gain insights into the distributions, relationships, and characteristics of the features. This involved performing statistical analysis, visualizations, and identifying any data quality issues or patterns that could impact the modeling process.

#### Data Splitting:
The dataset was divided into training and testing sets to assess the model's performance on unseen data accurately. The training set was used for model training and parameter tuning, while the testing set was utilized for evaluating the model's performance.

#### Data Preprocessing:
Data preprocessing steps were applied to ensure the dataset's quality and compatibility with the chosen algorithms. This involved handling missing values, handling imbalanced dataset, encoding categorical features, scaling numerical features.

#### Modeling and Evaluation:
The dataset was used to train and evaluate different machine learning models. A comparison was made between tree-based algorithms (such as Random Forest, XGBoost, and LightGBM) and a Deep Neural Network (DNN). Each model was trained using the training dataset, and their performance was evaluated using the AUC-ROC score. The objective was to identify the best-performing model considering both predictive power and generalizability. The results of modeling and evaluation indicate that DNN outperformed the tree based models as reflected by ROC-AUC scores. This signifies that the ANN model not only exhibits impressive accuracy but also effectively captures the intrinsic patterns and relationships within the dataset. Therefore, the ANN model is selected as the preferred choice for loan default prediction, given its superior performance.

#### FAST API Endpoint:
The winning model, chosen for its exceptional performance, was integrated into a FAST API endpoint. This endpoint enables seamless integration into internal bank applications, allowing users to request credit risk assessments for loan applicants. This integration enhances efficiency and ensures informed lending decisions.

#### Docker Containerization:
To ensure scalability and ease of deployment, the API endpoint was containerized using Docker. Containerization encapsulated the API, its dependencies, and the ML model within a portable environment. This approach facilitated easy deployment and scaling across different environments, reducing potential compatibility issues.


## Running the API Locally
To run the credit risk assessment API locally, you can follow these steps:

1. Clone the project repository: `git clone https://github.com/aswinram1997/Credit-Risk-Assessment_API.git`

2. Install Docker and ensure it is running properly on your machine.

3. Navigate to the project directory.

4. Build the Docker image using the Dockerfile: `docker build -t credit-risk-api .`

5. Run the Docker container based on the created image: `docker run -p 8000:8000 credit-risk-api`

6. Once the Docker container is running, you can send POST requests to http://localhost:8000/predict for credit risk assessments.


### Example Request
```
{
"person_age": 25,
"person_income": 50000.0,
"person_emp_length": 5,
"loan_amnt": 10000.0,
"loan_int_rate": 7.5,
"loan_percent_income": 20.0,
"cb_person_cred_hist_length": 3,
"person_home_ownership": "RENT",
"loan_intent": "EDUCATION",
"loan_grade": "A",
"cb_person_default_on_file": "N"
}
```
### Request Body Details
- `person_age`: integer (range: 20 - 144 years)
- `person_income`: float (range: $4,000 - $6,000,000)
- `person_emp_length`: integer (range: 0 - 123 months)
- `loan_amnt`: float (range: $500 - $35,000)
- `loan_int_rate`: float (range: 5.42% - 23.22%)
- `loan_percent_income`: float (range: 0% - 83%)
- `cb_person_cred_hist_length`: integer (range: 2 - 30 years)
- `person_home_ownership`: string (values: RENT, OWN, MORTGAGE, OTHER)
- `loan_intent`: string (values: PERSONAL, EDUCATION, MEDICAL, VENTURE, HOME IMPROVEMENT, DEBT CONSOLIDATION)
- `loan_grade`: string (values: D, B, C, A, E, F, G)
- `cb_person_default_on_file`: string (values: Yes, No)

## Conclusion
The developed credit risk assessment ML model, trained on the provided dataset, offers an efficient and accurate method for predicting loan default risk. By leveraging various applicant features, the model assists internal bank users in making informed lending decisions. The model's integration as an API enhances its accessibility, allowing for seamless integration with existing bank systems and workflows. This project's outcomes contribute to improved credit risk management, and streamlined loan processing, ultimately reducing the risk of defaults and promoting sound lending practices.
