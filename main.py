import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="yourSQLpwd",
    database="FIFA_WC"
)

cursor = conn.cursor()

def get_products():
    cursor.execute("SELECT ID, Quantity, Price FROM Sales")
    products = cursor.fetchall()
    df = pd.DataFrame(products, columns=["Prod_ID", "Quantity","Price"])  
    df["Revenue"]  = df["Quantity"] * df["Price"]
    return df

def add_products():
    try: 
        prod_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        
        if quantity <= 0 and price < 0:
            print("Invalid Quantity or Price! Please Try Again!")
            return
        
        cursor.execute("Select * from Sales where ID = %s", (prod_id,))
        if cursor.fetchone():
            print("Product ID already exists! Please Try again!")
            return
        
        maine = "Insert into Sales (ID, Quantity, Price) values (%s, %s, %s)"
        cursor.execute(maine, (prod_id, quantity, price))
        conn.commit()
        print("Product Added!")
    
    except Exception as e:
        print("Error: ", e)    

def show_products():
    df = get_products()
    print("Products: \n", df)
    
def total_revenue():
    df = get_products()
    print("Products: \n", df["Revenue"].sum())
    
def top_product():
    df = get_products()
    top = df.loc[df["Price"].idxmax()]
    print("Top Product: ", top)
    
def show_chart():
    df = get_products()
    plt.bar(df["Prod_ID"], df["Revenue"])
    plt.title("Revenue in terms of Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.show()

def predict_sales():
    df = get_products()
    X = df[["Quantity"]]
    y = df["Revenue"]
    
    model = LinearRegression()
    model.fit(X, y)
    qty = int(input("Enter quantity to predict sales: "))
    predict = model.predict([[qty]])
    
    print(f"Predict Sales: {qty}: {predict[0]}")
    
while True: 
    print("\n SMART SALES MANAGEMENT SYSTEM ")
    print("1. Show All Products")
    print("2. Total Revenue")
    print("3. Top Selling Product")
    print("4. Show Sales Chart")
    print("5. Predict Sales")
    print("6. Add Products")
    print("7. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_products()

    elif choice == 2:
        total_revenue()

    elif choice == 3:
        top_product()

    elif choice == 4:
        show_chart()

    elif choice == 5:
        predict_sales()
        
    elif choice == 6:
        add_products()
    
    elif choice == 7:
        print("Exited")
        break
    
    else:
        print("Please Try Again!")

conn.close()
    

#cursor.execute("SELECT Prod_ID, Product FROM Product")
#name = cursor.fetchall()

#starwars = print(name)
#print(starwars)

