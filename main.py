
# ============================================================
# ChurnSense: Customer Churn & Behaviour Analytics
# Main Project Launcher
# ============================================================

import os
import sys
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_FILES = {
    "1": ("Customer Data Analysis", "analysis.py"),
    "2": ("Customer Behaviour Insights", "customer_insights.py"),
    "3": ("Customer Data Visualization", "visualization.py"),
}


def display_menu():
    print("\n" + "=" * 60)
    print("       CHURNSENSE CUSTOMER ANALYTICS")
    print("=" * 60)
    print("1. Analyze customer data")
    print("2. View customer behaviour insights")
    print("3. Generate customer churn graphs")
    print("4. Exit")
    print("=" * 60)


def run_project_file(filename):
    file_path = os.path.join(BASE_DIR, filename)

    if not os.path.isfile(file_path):
        print(f"\nError: File not found: {filename}")
        return

    print(f"\nStarting: {filename}")
    print("-" * 60)

    result = subprocess.run(
        [sys.executable, file_path],
        cwd=BASE_DIR
    )

    if result.returncode == 0:
        print("\nTask completed.")
    else:
        print(
            "\nThe program ended with an error. "
            "Check the message above."
        )


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice in PROJECT_FILES:
            _, filename = PROJECT_FILES[choice]
            run_project_file(filename)

        elif choice == "4":
            print("\nThank you for using ChurnSense!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
