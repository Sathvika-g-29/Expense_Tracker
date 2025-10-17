import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
FILE_NAME = "expenses.csv"
def add_expense():
    amount=float(input("Enter the amount: "))
    category=input("Enter category[food,travel,shopping,etc]")
    date=datetime.now().strftime("%Y -%m-%d %H:%M:%S")
    with open(FILE_NAME,"a")as file:
        file.write(f"{date},{amount},{category}\n")
        print("Expense added successfully!")
def view_expenses():
    try:
        df=pd.read_csv(FILE_NAME,names=["Date","Amount","Category"])
        print("***All Expenses***")
        print(df)
    except FileNotFoundError:
        print("No expenses recorded yet.")
def analyze_expenses():
    try:
        df=pd.read_csv(FILE_NAME,names=["Date","Amount","Category"])
        print("***Expense Summary***")
        print(df.groupby("Category")["Amount"].sum())
        df.groupby("Category")["Amount"].sum().plot(kind="pie",autopct="%1.1f")
        plt.title("Expenses by Category")
        plt.show()
    except  FileNotFoundError:
        print("No expense are recorded yet.")
def main():
    while True:
        print("****EXPENSE TRACKER****")
        print("1. ADD expense")
        print("2. VIEW expense")
        print("3. ANALYZE expense")
        print("4. EXIT")
        c=input("Enter choice")
        if c=="1":
            add_expense()
        elif c=="2":
            view_expenses()
        elif c=="3":
            analyze_expenses()
        elif c=="4":
            break
        else:
            print("Invalid choice! Try again.")
if __name__=="__main__":
    main()