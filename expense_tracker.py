import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class ExpenseTracker:

    def __init__(self):
        try:
            self.df = pd.read_csv("expenses.csv")
            print("Data Loaded Successfully")
            self.df.dropna(inplace=True)
        except:
            print("New dataset created")
            self.df = pd.DataFrame(
                columns=["Date", "Amount", "Category", "Description"]
            )

    def add_expense(self):

        date = input("Enter Date (YYYY-MM-DD): ")
        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")
        description = input("Enter Description: ")

        if amount <= 0:
            print("Invalid amount")
            return

        new_data = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description,
        }

        self.df = pd.concat(
            [self.df, pd.DataFrame([new_data])], ignore_index=True
        )

        self.df.to_csv("expenses.csv", index=False)
        print("Expense Added")

    def get_summary(self):

        total = np.sum(self.df["Amount"])
        avg = np.mean(self.df["Amount"])

        print("Total Expense:", total)
        print("Average Expense:", avg)

    def filter_expenses(self):

        cat = input("Enter category to filter: ")
        filtered = self.df[self.df["Category"] == cat]

        print(filtered)

    def generate_report(self):

        print("\nShape")
        print(self.df.shape)

        print("\nNull Values")
        print(self.df.isnull().sum())

        print("\nDescribe")
        print(self.df.describe())

        print("\nCategory Wise Total")
        print(self.df.groupby("Category")["Amount"].sum())

        self.df["Date"] = pd.to_datetime(self.df["Date"])

        print("\nMonthly Spending")
        print(self.df.groupby(self.df["Date"].dt.month)["Amount"].sum())

    def visualize(self):

        sns.barplot(x="Category", y="Amount", data=self.df)
        plt.title("Total Expense by Category")
        plt.show()

        plt.plot(self.df["Amount"])
        plt.title("Spending Trend")
        plt.show()

        self.df.groupby("Category")["Amount"].sum().plot(
            kind="pie", autopct="%1.1f%%"
        )
        plt.title("Category Distribution")
        plt.show()

        plt.hist(self.df["Amount"])
        plt.title("Expense Histogram")
        plt.show()


tracker = ExpenseTracker()

while True:

    print("\n--- Smart Expense Tracker ---")
    print("1. Add Expense")
    print("2. Summary")
    print("3. Filter")
    print("4. Report")
    print("5. Visualization")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        tracker.add_expense()

    elif choice == "2":
        tracker.get_summary()

    elif choice == "3":
        tracker.filter_expenses()

    elif choice == "4":
        tracker.generate_report()

    elif choice == "5":
        tracker.visualize()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
