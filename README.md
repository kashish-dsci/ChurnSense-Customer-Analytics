
# ChurnSense: Customer Churn & Behaviour Analytics

## Project Overview

ChurnSense is a Python-based data analytics mini project
that studies customer churn behaviour using a customer dataset.

The project examines customer retention, contract types,
tenure, and monthly charges to identify patterns associated
with customers leaving a service.

## Objectives

- Load and inspect customer data.
- Calculate customer churn and retention rates.
- Analyze customer behaviour and contract patterns.
- Visualize findings using charts.
- Develop a foundation for future machine learning models.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Project Files

- `main.py` - Main project menu and launcher.
- `analysis.py` - Dataset inspection and churn analysis.
- `customer_insights.py` - Customer behaviour analysis.
- `visualization.py` - Customer churn charts.
- `customer_data.csv` - Customer dataset.
- `requirements.txt` - Required Python libraries.
- `plots/` - Generated chart images.

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Open a terminal in the project folder.
4. Install the required libraries:

   `python -m pip install -r requirements.txt`

5. Run the project:

   `python main.py`

6. Choose an option from the menu.

## Dataset

The project uses the IBM Telco Customer Churn sample dataset.
Check the original dataset source and its license before
redistributing the CSV in a public repository.

## Future Scope

- Train classification models such as Logistic Regression,
  Decision Tree, and Random Forest.
- Compare models using appropriate evaluation metrics.
- Identify customers who may be at risk of leaving.
- Explore a dashboard for presenting results.

## Disclaimer

This is an educational project. Patterns identified in the
dataset do not establish causation or guarantee future churn.
