import streamlit as st
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="your_pwd",
    database="FIFA_WC"
)

cursor = conn.cursor()

def get_products():
    cursor.execute("SELECT ID, Customer, Product, Quantity, Price FROM Sales")
    data = cursor.fetchall()

    df = pd.DataFrame(data, columns=["ID", "Customer", "Product", "Quantity", "Price"])
    df["Revenue"] = df["Quantity"] * df["Price"]

    return df


def add_product(prod_id, customer, product, quantity, price):

    if quantity <= 0 or price < 0:
        return "Invalid Quantity or Price!"

    cursor.execute("SELECT * FROM Sales WHERE ID=%s", (prod_id,))
    if cursor.fetchone():
        return "Product ID already exists!"

    cursor.execute(
        "INSERT INTO Sales (ID, Customer, Product, Quantity, Price) VALUES (%s, %s, %s, %s, %s)",
        (prod_id, customer, product, quantity, price)
    )

    conn.commit()
    return "Product Added Successfully!"


st.set_page_config(page_title="Sales System", layout="wide")

st.title("📊 Smart Sales Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Show Products", "Add Product", "Total Revenue", "Top Product", "Sales Chart", "Predict Sales"]
)

if menu == "Show Products":
    st.subheader("📋 All Products")
    df = get_products()

    if df.empty:
        st.warning("No data available!")
    else:
        st.dataframe(df, use_container_width=True)


elif menu == "Add Product":
    st.subheader("➕ Add New Product")

    prod_id = st.number_input("Product ID", step=1)
    customer = st.text_input("Customer Name")
    product = st.text_input("Product Name")
    quantity = st.number_input("Quantity", step=1)
    price = st.number_input("Price", step=0.1)

    if st.button("Add Product"):
        result = add_product(prod_id, customer, product, quantity, price)
        st.success(result)


elif menu == "Total Revenue":
    st.subheader("💰 Total Revenue")

    df = get_products()

    if df.empty:
        st.warning("No data available!")
    else:
        total = df["Revenue"].sum()
        st.success(f"Total Revenue: ₹ {total:.2f}")


elif menu == "Top Product":
    st.subheader("🏆 Top Product")

    df = get_products()

    if df.empty:
        st.warning("No data available!")
    else:
        top = df.loc[df["Revenue"].idxmax()]
        st.write(top)


elif menu == "Sales Chart":
    st.subheader("📊 Revenue Chart")

    df = get_products()

    if df.empty:
        st.warning("No data available!")
    else:
        fig, ax = plt.subplots()

        ax.bar(df["ID"], df["Revenue"]) 
        ax.set_xlabel("Product ID")
        ax.set_ylabel("Revenue")

        st.pyplot(fig)

elif menu == "Predict Sales":
    st.subheader("🤖 Personalized Revenue Prediction")

    df = get_products()

    if df.empty:
        st.warning("No data available!")
    else:
       
        df["Customer_Code"] = df["Customer"].astype("category").cat.codes

        X = df[["Customer_Code", "Quantity"]]
        y = df["Revenue"]

        model = LinearRegression()
        model.fit(X, y)

        customer_list = df["Customer"].unique()
        selected_customer = st.selectbox("Select Customer", customer_list)

        qty = st.number_input("Enter Quantity", step=1)

        customer_code = df[df["Customer"] == selected_customer]["Customer_Code"].iloc[0]

        if st.button("Predict"):
            prediction = model.predict([[customer_code, qty]])[0]
            st.success(f"Predicted Revenue for {selected_customer}: ₹ {prediction:.2f}")
