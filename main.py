import streamlit as st
import pandas as pd

# 1. Setup
if 'calc_input' not in st.session_state:
    st.session_state['calc_input'] = ""

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# 2. About Us
if st.button("About us"):
    st.text("Developed by the YF company team. Support us by sharing!")

st.title("Yamaan Faraz YF™ Official Calculator.")

# 3. The Input Box
eq = st.text_input("Equation:", value=st.session_state['calc_input'])

# 4. Buttons from CSV
df = pd.read_csv("buttons.csv")
symbols = df.columns[1:] # +, -, //, /, %, *, =, >, <, **
cols = st.columns(len(symbols))

clicked = None
for i, symbol in enumerate(symbols):
    with cols[i]:
        if st.button(symbol):
            clicked = symbol

# 5. Logic for EVERY Button (If/Else)
if clicked == "=":
    try:
        # 1. Check double-character operators FIRST
        if "**" in eq:
            parts = [float(x) for x in eq.split("**")]
            res = parts[0]
            for x in parts[1:]: res **= x
            st.write(f"Result: {res}")

        elif "//" in eq:
            parts = [float(x) for x in eq.split("//")]
            res = parts[0]
            for x in parts[1:]: res //= x
            st.write(f"Result: {res}")

        # 2. Check single-character operators
        elif "+" in eq:
            parts = [float(x) for x in eq.split("+")]
            st.write(f"Result: {sum(parts)}")

        elif "-" in eq:
            parts = [float(x) for x in eq.split("-")]
            res = parts[0] - sum(parts[1:])
            st.write(f"Result: {res}")

        elif "*" in eq:
            parts = [float(x) for x in eq.split("*")]
            res = 1
            for x in parts: res *= x
            st.write(f"Result: {res}")

        elif "/" in eq:
            parts = [float(x) for x in eq.split("/")]
            res = parts[0]
            for x in parts[1:]: res /= x
            st.write(f"Result: {res}")
        elif "%" in eq:
            parts = [float(x) for x in eq.split("%")]
            res = parts[0]
            for x in parts[1:]: res %= x
            st.write(f"Result: {res}")
        elif ">" in eq:
            parts = eq.split(">")
            st.write("Right" if float(parts[0]) > float(parts[1]) else "Wrong")

        elif "<" in eq:
            parts = eq.split("<")
            st.write("Right" if float(parts[0]) < float(parts[1]) else "Wrong")

    except Exception as e:
        st.error("Check your numbers")

    # --- Button "Clicked" Logic for every operation ---
    if clicked == "+":
        st.session_state['calc_input'] = eq + "+"
        st.rerun()
    elif clicked == "-":
        st.session_state['calc_input'] = eq + "-"
        st.rerun()
    elif clicked == "*":
        st.session_state['calc_input'] = eq + "*"
        st.rerun()
    elif clicked == "/":
        st.session_state['calc_input'] = eq + "/"
        st.rerun()
    elif clicked == "//":
        st.session_state['calc_input'] = eq + "//"
        st.rerun()
    elif clicked == "%":
        st.session_state['calc_input'] = eq + "%"
        st.rerun()
    elif clicked == "**":
        st.session_state['calc_input'] = eq + "**"
        st.rerun()
    elif clicked == ">":
        st.session_state['calc_input'] = eq + ">"
        st.rerun()
    elif clicked == "<":
        st.session_state['calc_input'] = eq + "<"
        st.rerun()
