
# ============================================================
# ChurnSense - Interactive Customer Analytics Dashboard
# ============================================================

from pathlib import Path

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="ChurnSense Dashboard",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "customer_data.csv"

# ------------------------------------------------------------
# BLACK AND WHITE DESIGN
# ------------------------------------------------------------

st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffffff;
        color: #111111;
    }

    h1, h2, h3, p, label {
        color: #111111;
    }

    div[data-testid="stMetric"] {
        background: #f5f5f5;
        border: 1px solid #222222;
        padding: 18px;
        border-radius: 8px;
    }

    div[data-testid="stMetricValue"] {
        color: #111111;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# LOAD DATASET
# ------------------------------------------------------------

@st.cache_data
def load_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    try:
        data = pd.read_csv(DATA_FILE, encoding="utf-8")
    except UnicodeDecodeError:
        data = pd.read_csv(DATA_FILE, encoding="latin-1")

    data.columns = data.columns.astype(str).str.strip()

    # Standardize common column-name variations
    rename_columns = {}

    for column in data.columns:
        cleaned = column.strip().lower().replace(" ", "")

        if cleaned == "churn":
            rename_columns[column] = "Churn"
        elif cleaned == "tenure":
            rename_columns[column] = "tenure"
        elif cleaned in ("monthlycharges", "monthly_charge"):
            rename_columns[column] = "MonthlyCharges"
        elif cleaned == "contract":
            rename_columns[column] = "Contract"

    data = data.rename(columns=rename_columns)

    return data


# ------------------------------------------------------------
# MAIN DASHBOARD
# ------------------------------------------------------------

st.title("ChurnSense")
st.subheader("Customer Churn & Behaviour Analytics")

st.write(
    "Explore customer retention, monthly charges, "
    "and customer behaviour using interactive data visualization."
)

st.divider()

try:
    df = load_data()
except Exception as error:
    st.error(f"Unable to load the dataset: {error}")
    st.stop()

required_columns = ["Churn", "MonthlyCharges", "tenure"]
missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    st.error(
        "Required columns were not found: "
        + ", ".join(missing_columns)
    )
    st.write("Available columns:", df.columns.tolist())
    st.stop()

# Clean data for calculations
df["Churn"] = df["Churn"].astype(str).str.strip()
df["MonthlyCharges"] = pd.to_numeric(
    df["MonthlyCharges"], errors="coerce"
)
df["tenure"] = pd.to_numeric(
    df["tenure"], errors="coerce"
)

# Normalize churn labels for calculations
churn_yes = df["Churn"].str.lower().eq("yes")
churn_no = df["Churn"].str.lower().eq("no")

total_customers = len(df)
customers_left = int(churn_yes.sum())
customers_stayed = int(churn_no.sum())

churn_rate = (
    customers_left / total_customers * 100
    if total_customers else 0
)

retention_rate = (
    customers_stayed / total_customers * 100
    if total_customers else 0
)

# ------------------------------------------------------------
# SIDEBAR FILTERS
# ------------------------------------------------------------

st.sidebar.header("Dashboard Filters")

filtered_df = df.copy()

if "Contract" in df.columns:
    contract_options = ["All"] + sorted(
        df["Contract"].dropna().astype(str).unique().tolist()
    )

    selected_contract = st.sidebar.selectbox(
        "Select Contract Type",
        contract_options
    )

    if selected_contract != "All":
        filtered_df = filtered_df[
            filtered_df["Contract"].astype(str) == selected_contract
        ]

churn_options = ["All"] + sorted(
    filtered_df["Churn"].dropna().unique().tolist()
)

selected_churn = st.sidebar.selectbox(
    "Select Churn Status",
    churn_options
)

if selected_churn != "All":
    filtered_df = filtered_df[
        filtered_df["Churn"] == selected_churn
    ]

st.sidebar.caption(
    "Choose filters to explore different customer groups."
)

# ------------------------------------------------------------
# KEY PERFORMANCE INDICATORS
# ------------------------------------------------------------

st.header("Customer Overview")

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric(
    "Total Customers",
    f"{total_customers:,}"
)

metric2.metric(
    "Customers Left",
    f"{customers_left:,}"
)

metric3.metric(
    "Churn Rate",
    f"{churn_rate:.2f}%"
)

metric4.metric(
    "Retention Rate",
    f"{retention_rate:.2f}%"
)

st.caption(
    "Overview metrics describe the full dataset. "
    "Filters below apply to the detailed charts."
)

st.divider()

# ------------------------------------------------------------
# CHART 1: CUSTOMER CHURN DISTRIBUTION
# ------------------------------------------------------------

st.header("1. Customer Churn Distribution")

chart1, chart2 = st.columns(2)

with chart1:
    churn_counts = filtered_df["Churn"].value_counts()

    fig, ax = plt.subplots(figsize=(7, 4))

    sns.barplot(
        x=churn_counts.index,
        y=churn_counts.values,
        color="#555555",
        ax=ax
    )

    ax.set_title("Customers by Churn Status")
    ax.set_xlabel("Churn Status")
    ax.set_ylabel("Number of Customers")

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# ------------------------------------------------------------
# CHART 2: MONTHLY CHARGES HISTOGRAM
# ------------------------------------------------------------

with chart2:
    fig, ax = plt.subplots(figsize=(7, 4))

    sns.histplot(
        data=filtered_df,
        x="MonthlyCharges",
        bins=20,
        kde=True,
        color="#555555",
        ax=ax
    )

    ax.set_title("Distribution of Monthly Charges")
    ax.set_xlabel("Monthly Charges")
    ax.set_ylabel("Number of Customers")

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

st.divider()

# ------------------------------------------------------------
# CHART 3: TENURE VS MONTHLY CHARGES
# ------------------------------------------------------------

st.header("2. Customer Tenure vs Monthly Charges")

scatter_data = filtered_df.dropna(
    subset=["tenure", "MonthlyCharges", "Churn"]
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.scatterplot(
    data=scatter_data,
    x="tenure",
    y="MonthlyCharges",
    hue="Churn",
    alpha=0.6,
    ax=ax
)

ax.set_title("Customer Tenure vs Monthly Charges")
ax.set_xlabel("Customer Tenure (Months)")
ax.set_ylabel("Monthly Charges")
ax.legend(title="Churn Status")

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# ------------------------------------------------------------
# CUSTOMER DATA TABLE
# ------------------------------------------------------------

st.divider()
st.header("Customer Data Explorer")

st.write(
    f"Showing {len(filtered_df):,} of {total_customers:,} customers."
)

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------

st.divider()

st.caption(
    "ChurnSense | Python, Pandas, Matplotlib, Seaborn and Streamlit"
)

st.caption(
    "Educational project: observed patterns do not prove causation."
)
