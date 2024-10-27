import streamlit as st
import joblib 
import pandas as pd

def main():
    st.set_page_config(
        page_title="Prima",
        page_icon=":tulip:",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.write("Bem vindo(a) ao Prima App")

if __name__ == '__main__':
    main()