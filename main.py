import streamlit as st
import pandas as pd
import numpy as np
if 'clicked' not in st.session_state:
    st.session_state['clicked'] = False

b1 = st.button("About us")
if b1:
    st.session_state['clicked'] = True
    st.text("This Is a app developed by the YF company team.")
    st.text("You can calculate daily-life things on this app, like total groceries price,"
            "clothes price, toys, etc.")
    st.text("You can do any calculation. like google calculator, it calculates but this provides"
            "good interface, good experience and more.")
    st.text("if you are using this app, please support us by sharing this to others.")
st.title("Yamaan Faraz YF™ Official Calculator.")
i1 = st.number_input(placeholder="Enter a number here.", label="Enter number.")
i2 = st.number_input(placeholder="Enter second number.", label="Enter second number.")

df = pd.read_csv("buttons.csv")
num_buttons = len(df.columns[1:])
cols = st.columns(num_buttons)

operation = None

for i, symbol in enumerate(df.columns[1:]):
    with cols[i]:
        if st.button(symbol):
            operation = symbol
if operation:
    if operation == "+":
        st.session_state['clicked'] = True
        st.write(f"{np.add(i1, i2)}")
    elif operation == "-":
        st.session_state['clicked'] = True
        st.write(f"{np.subtract(i1, i2)}")
    elif operation == "/":
        st.session_state['clicked'] = True
        if i2 != 0:
            st.write(f"{i1 / i2}")
        else:
            st.error("Cannot divide by zero!")

    elif operation == "//":
        st.session_state['clicked'] = True
        if i2 != 0:
            st.write(f"{i1 // i2}")
        else:
            st.error("Cannot divide by zero!")

    elif operation == "%":
        st.session_state['clicked'] = True
        if i2 != 0:
            st.write(f"{i1 % i2}")
        else:
            st.error("Cannot divide by zero!")

    elif operation == "*":
        st.session_state['clicked'] = True
        st.write(f"{i1 * i2}")
    elif operation == ">":
        st.session_state['clicked'] = True
        if i1 > i2:
            st.write("Right")
        else:
            st.write("Wrong")
    elif operation == "<":
        st.session_state['clicked'] = True
        if i1 < i2:
            st.write("Right")
        else:
            st.write("Wrong")
    elif operation == "=":
        st.session_state['clicked'] = True
        if i1 == i2:
            st.write("Right")
        else:
            st.write("Wrong")
    elif operation == "**":
        st.session_state['clicked'] = True
        st.write(f"{i1 ** i2}")