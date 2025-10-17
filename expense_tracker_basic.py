import csv
from datetime import datetime
FILE_NAME="expenses.csv"
def add_expense():
    amount=float(input("Enter the amount: "))
    category=input("Enter category[Food,Travel,Shopping,etc]")
    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME,"a",newline="")as file:
        writer=csv.writer(file)
        writer.writerow([date,amount,category])
        print("Expenses added Successfully!")
def view_expenses():
    try:
        with open(FILE_NAME,"r")as file:
            reader=csv.reader(file)
            print("***EXPENSES***")
            for row in reader:
                print(f"Date: {row[0]},Amount: {row[1]},category: {row[2]}")
    except FileNotFoundError:
        print("No expenses recorded yet.")
def main():
    while True:
        print("***EXPENSES TRACKER***")
        print("1. ADD expenses")
        print("2. VIEW expenses")
        print("3. EXIT")

        c = input("Enter choice")
        if c=="1":
            add_expense()
        elif c=="2":
            view_expenses()
        elif c=="3":
            break
        else:
            print("Invalid Choice! Try again.")
if __name__=="__main__":
    main()