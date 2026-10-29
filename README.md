# ChurnSense: Customer Churn & Behaviour Analytics

## Project Overview

ChurnSense is a Python-based data analytics mini-project that studies customer churn behaviour using a customer dataset.

The project examines customer retention, contract types, customer tenure, and monthly charges to identify patterns associated with customers leaving a service. It also provides an interactive web dashboard for exploring customer data and visualizations.

## Objectives

- Load and inspect customer data.
- Calculate customer churn and retention rates.
- Analyze customer behaviour and contract patterns.
- Visualize findings using charts.
- Provide an interactive dashboard for data exploration.
- Establish a foundation for future machine learning models.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Scikit-learn (for potential future machine learning extensions)

## Project Files

- `main.py` — Main project menu and launcher.
- `analysis.py` — Dataset inspection and churn analysis.
- `customer_insights.py` — Customer behaviour analysis.
- `visualization.py` — Customer churn chart generation.
- `dashboard.py` — Interactive Streamlit dashboard.
- `run_dashboard.py` — Launcher for starting the dashboard.
- `customer_data.csv` — Customer dataset.
- `requirements.txt` — Required Python libraries.
- `plots/` — Generated chart images.
- `.gitignore` — Excludes selected unnecessary or local files.

## Visualizations

The project generates the following charts:

1. **Churn Distribution:** Compares customers who left with those who stayed.
2. **Monthly Charges Histogram:** Shows the distribution of monthly customer charges.
3. **Tenure vs. Monthly Charges Scatter Plot:** Explores the relationship between customer tenure and monthly charges.

## How to Run

### Prerequisites

- Python installed on your computer.
- VS Code or another Python-compatible editor.
- An internet connection for installing dependencies, if they are not already installed.

### Step 1: Install Dependencies

Open a terminal in the project folder and run:

`python -m pip install -r requirements.txt`

### Step 2: Run the Analysis Menu

Run:

`python main.py`

Choose an option from the menu to perform analysis, view customer insights, or generate visualizations.

### Step 3: Run the Interactive Dashboard

To start the web dashboard, run:

`python -m streamlit run dashboard.py`

Alternatively, open `run_dashboard.py` in VS Code and click **Run Python File**.

The dashboard normally opens in your browser at `http://localhost:8501`.

## Dataset

The project uses the IBM Telco Customer Churn sample dataset.

Before redistributing the dataset publicly, verify its original source, applicable license, and redistribution permissions.

## Future Scope

- Train classification models such as Logistic Regression, Decision Tree, and Random Forest.
- Compare models using appropriate evaluation metrics.
- Identify customers who may be at risk of leaving.
- Add interactive filters and more advanced visualizations.
- Develop predictive insights to support customer retention strategies.

## Disclaimer

This is an educational project. Patterns identified in the dataset do not establish causation or guarantee future churn. Any predictive results would depend on data quality, model performance, and appropriate evaluation.
