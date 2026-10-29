
# ============================================================
# ChurnSense - Customer Behaviour Insights
# ============================================================

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "customer_data.csv"


def load_dataset():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    try:
        df = pd.read_csv(DATA_FILE, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(DATA_FILE, encoding="latin-1")

    df.columns = df.columns.str.strip()
    return df


def main():
    print("=" * 60)
    print("       CHURNSENSE CUSTOMER BEHAVIOUR INSIGHTS")
    print("=" * 60)

    df = load_dataset()

    if "Churn" not in df.columns:
        print("Columns found:", df.columns.tolist())
        raise ValueError(
            "The dataset does not contain a Churn column."
        )

    df["Churn"] = df["Churn"].astype(str).str.strip()
    churn_flag = df["Churn"].str.lower().eq("yes")

    print("\n1. CUSTOMER SUMMARY")
    print("-" * 40)
    print(f"Total records: {len(df)}")
    print(f"Customers who left: {int(churn_flag.sum())}")

    # Churn by contract
    print("\n2. CHURN RATE BY CONTRACT")
    print("-" * 40)

    if "Contract" in df.columns:
        contract_data = df.assign(ChurnFlag=churn_flag)
        contract_rates = (
            contract_data.groupby("Contract")["ChurnFlag"]
            .mean()
            .mul(100)
            .round(2)
        )
        print(contract_rates.to_string() + " %")
    else:
        print("Contract column unavailable.")

    # Churn by tenure
    print("\n3. AVERAGE TENURE")
    print("-" * 40)

    if "tenure" in df.columns:
        df["tenure"] = pd.to_numeric(
            df["tenure"], errors="coerce"
        )
        print(
            df.groupby("Churn")["tenure"]
            .mean()
            .round(2)
            .to_string()
        )
    else:
        print("Tenure column unavailable.")

    # Churn by monthly charges
    print("\n4. AVERAGE MONTHLY CHARGES")
    print("-" * 40)

    if "MonthlyCharges" in df.columns:
        df["MonthlyCharges"] = pd.to_numeric(
            df["MonthlyCharges"], errors="coerce"
        )
        print(
            df.groupby("Churn")["MonthlyCharges"]
            .mean()
            .round(2)
            .to_string()
        )
    else:
        print("MonthlyCharges column unavailable.")

    # Other useful categories
    for column in ("InternetService", "PaymentMethod"):
        if column in df.columns:
            print(f"\n5. CHURN BY {column.upper()}")
            print("-" * 40)

            grouped = df.assign(ChurnFlag=churn_flag)
            rates = (
                grouped.groupby(column)["ChurnFlag"]
                .mean()
                .mul(100)
                .round(2)
            )
            print(rates.to_string() + " %")

    print("\nINSIGHTS ANALYSIS COMPLETED")


if __name__ == "__main__":
    main()
