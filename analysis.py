
# ============================================================
# ChurnSense - Customer Churn Analysis
# ============================================================

from pathlib import Path
import pandas as pd

# Project folder and dataset path
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "customer_data.csv"



def load_dataset():
    """Load the customer dataset safely."""

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}\n"
            "Place customer_data.csv in the ChurnSense folder."
        )

    for encoding in ("utf-8", "latin-1"):
        try:
            df = pd.read_csv(
                DATA_FILE,
                encoding=encoding,
                sep=",",
                engine="python",
                on_bad_lines="error"
            )

            print("\nDataset loaded successfully!")
            return df

        except UnicodeDecodeError:
            continue

    raise ValueError("Unable to read the CSV encoding.")



def main():
    print("=" * 60)
    print("          CHURNSENSE CUSTOMER CHURN ANALYSIS")
    print("=" * 60)

    # Load dataset
    df = load_dataset()

    # Clean column names
    df.columns = df.columns.str.strip()

    # Check whether the dataset is empty
    if df.empty:
        raise ValueError(
            "The CSV file contains no customer records."
        )

    # Check required column
    if "Churn" not in df.columns:
        print("\nColumns found in the CSV:")
        print(df.columns.tolist())

        raise ValueError(
            "\nThe required 'Churn' column was not found. "
            "Please check the downloaded dataset."
        )

    # Clean churn values
    df["Churn"] = df["Churn"].astype("string").str.strip()

    # --------------------------------------------------------
    # 1. DATASET OVERVIEW
    # --------------------------------------------------------
    print("\n1. DATASET OVERVIEW")
    print("-" * 40)

    print(f"Total customer records: {len(df)}")
    print(f"Total columns: {len(df.columns)}")

    # --------------------------------------------------------
    # 2. CUSTOMER CHURN COUNTS
    # --------------------------------------------------------
    print("\n2. CUSTOMER CHURN COUNTS")
    print("-" * 40)

    print(df["Churn"].value_counts(dropna=False).to_string())

    # --------------------------------------------------------
    # 3. CHURN RATE
    # --------------------------------------------------------
    churn_values = df["Churn"].str.lower()

    churn_flag = churn_values.eq("yes")
    retained_flag = churn_values.eq("no")

    total = len(df)
    churned = int(churn_flag.sum())
    retained = int(retained_flag.sum())

    print("\n3. CHURN RATE")
    print("-" * 40)

    print(f"Customers who left: {churned}")

    if total > 0:
        churn_rate = churned / total * 100
        print(f"Churn rate: {churn_rate:.2f}%")
    else:
        print("Churn rate cannot be calculated.")

    # --------------------------------------------------------
    # 4. RETENTION RATE
    # --------------------------------------------------------
    print("\n4. RETENTION RATE")
    print("-" * 40)

    print(f"Customers who stayed: {retained}")

    if total > 0:
        retention_rate = retained / total * 100
        print(f"Retention rate: {retention_rate:.2f}%")
    else:
        print("Retention rate cannot be calculated.")

    # --------------------------------------------------------
    # 5. MISSING VALUES
    # --------------------------------------------------------
    print("\n5. MISSING VALUES")
    print("-" * 40)

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        print("No missing values detected.")
    else:
        print("Columns with missing values:")
        print(missing.to_string())

    # --------------------------------------------------------
    # 6. NUMERICAL DATA SUMMARY
    # --------------------------------------------------------
    print("\n6. NUMERICAL DATA SUMMARY")
    print("-" * 40)

    numerical_summary = df.describe(include="number")

    if numerical_summary.empty:
        print("No numerical columns found.")
    else:
        print(numerical_summary.round(2).to_string())

    # --------------------------------------------------------
    # 7. INITIAL OBSERVATION
    # --------------------------------------------------------
    print("\n7. INITIAL OBSERVATION")
    print("-" * 40)

    print(
        "Use further analysis and graphs to investigate "
        "which customer groups have higher churn rates."
    )

    print(
        "These results describe the dataset; they do not prove "
        "why individual customers leave."
    )

    # --------------------------------------------------------
    # COMPLETION
    # --------------------------------------------------------
    print("\nAnalysis completed successfully!")
    print("=" * 60)


# Run the program
if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"\nERROR: {error}")
