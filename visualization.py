
# ============================================================
# ChurnSense - Customer Data Visualization
# ============================================================

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "customer_data.csv"
PLOT_DIR = BASE_DIR / "plots"


def load_dataset():
    """Load customer data and standardize column names."""

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    try:
        df = pd.read_csv(DATA_FILE, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(DATA_FILE, encoding="latin-1")

    # Remove spaces and standardize column names
    df.columns = df.columns.astype(str).str.strip()

    # Match column names without case differences
    rename_columns = {}

    for column in df.columns:
        cleaned = column.strip().lower().replace(" ", "")
        if cleaned == "churn":
            rename_columns[column] = "Churn"
        elif cleaned == "tenure":
            rename_columns[column] = "tenure"
        elif cleaned in ("monthlycharges", "monthly_charge"):
            rename_columns[column] = "MonthlyCharges"

    df = df.rename(columns=rename_columns)

    print("\nCSV column names:", df.columns.tolist())

    return df


def main():
    print("=" * 60)
    print("       CHURNSENSE CUSTOMER DATA VISUALIZATION")
    print("=" * 60)

    df = load_dataset()

    # Check for required columns
    if "Churn" not in df.columns:
        raise ValueError(
            "The Churn column was not found. "
            "Check the CSV column names printed above."
        )

    if "MonthlyCharges" not in df.columns:
        raise ValueError(
            "The MonthlyCharges column was not found. "
            "Check the CSV column names printed above."
        )

    # Create the output folder
    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    # Prepare numerical columns
    df["MonthlyCharges"] = pd.to_numeric(
        df["MonthlyCharges"], errors="coerce"
    )

    # ========================================================
    # GRAPH 1: Customer Churn Distribution - Bar Chart
    # ========================================================

    churn_counts = df["Churn"].value_counts()

    plt.figure(figsize=(7, 5))
    sns.barplot(
        x=churn_counts.index,
        y=churn_counts.values
    )

    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn Status")
    plt.ylabel("Number of Customers")
    plt.tight_layout()

    plt.savefig(
        PLOT_DIR / "churn_distribution.png",
        dpi=150
    )
    plt.close()

    print("\nGraph 1 created: Customer Churn Distribution")

    # ========================================================
    # GRAPH 2: Monthly Charges - Histogram
    # ========================================================

    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x="MonthlyCharges",
        bins=20,
        kde=True
    )

    plt.title("Distribution of Monthly Charges")
    plt.xlabel("Monthly Charges")
    plt.ylabel("Number of Customers")
    plt.tight_layout()

    plt.savefig(
        PLOT_DIR / "monthly_charges_histogram.png",
        dpi=150
    )
    plt.close()

    print("Graph 2 created: Distribution of Monthly Charges")

    # ========================================================
    # GRAPH 3: Tenure vs Monthly Charges - Scatter Plot
    # ========================================================

    # Find the tenure column regardless of capitalization
    tenure_column = next(
        (
            column for column in df.columns
            if column.strip().lower() == "tenure"
        ),
        None
    )

    if tenure_column is not None:
        df[tenure_column] = pd.to_numeric(
            df[tenure_column], errors="coerce"
        )

        scatter_data = df.dropna(
            subset=[tenure_column, "MonthlyCharges", "Churn"]
        )

        plt.figure(figsize=(8, 5))

        sns.scatterplot(
            data=scatter_data,
            x=tenure_column,
            y="MonthlyCharges",
            hue="Churn",
            alpha=0.6
        )

        plt.title("Customer Tenure vs Monthly Charges")
        plt.xlabel("Customer Tenure (Months)")
        plt.ylabel("Monthly Charges")
        plt.legend(title="Churn Status")
        plt.tight_layout()

        plt.savefig(
            PLOT_DIR / "tenure_vs_monthly_charges.png",
            dpi=150
        )
        plt.close()

        print("Graph 3 created: Customer Tenure vs Monthly Charges")

    else:
        print(
            "\nGraph 3 could not be created because the "
            "'tenure' column was not found."
        )
        print(
            "Check the CSV column names printed above."
        )

    print("\n" + "=" * 60)
    print("VISUALIZATION PROCESS FINISHED")
    print(f"Graphs folder: {PLOT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
