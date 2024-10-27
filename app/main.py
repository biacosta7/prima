import streamlit as st
import joblib 
import pandas as pd

def get_clean_data():
    data = pd.read_csv("../data/data-wisconsin.csv")

    data = data.drop(['Unnamed: 32', 'id'], axis=1)

    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

    return data

def add_sidebar():
    st.sidebar.header("Medições de núcleos celulares")
    data = get_clean_data()

    slider_labels = [
        ("Radius (mean)", "radius_mean"),
        ("Texture (mean)", "texture_mean"),
        ("Perimeter (mean)", "perimeter_mean"),
        ("Area (mean)", "area_mean"),
        ("Smoothness (mean)", "smoothness_mean"),
        ("Compactness (mean)", "compactness_mean"),
        ("Concavity (mean)", "concavity_mean"),
        ("Concave points (mean)", "concave points_mean"),
        ("Symmetry (mean)", "symmetry_mean"),
        ("Fractal dimension (mean)", "fractal_dimension_mean"),
        ("Radius (se)", "radius_se"),
        ("Texture (se)", "texture_se"),
        ("Perimeter (se)", "perimeter_se"),
        ("Area (se)", "area_se"),
        ("Smoothness (se)", "smoothness_se"),
        ("Compactness (se)", "compactness_se"),
        ("Concavity (se)", "concavity_se"),
        ("Concave points (se)", "concave points_se"),
        ("Symmetry (se)", "symmetry_se"),
        ("Fractal dimension (se)", "fractal_dimension_se"),
        ("Radius (worst)", "radius_worst"),
        ("Texture (worst)", "texture_worst"),
        ("Perimeter (worst)", "perimeter_worst"),
        ("Area (worst)", "area_worst"),
        ("Smoothness (worst)", "smoothness_worst"),
        ("Compactness (worst)", "compactness_worst"),
        ("Concavity (worst)", "concavity_worst"),
        ("Concave points (worst)", "concave points_worst"),
        ("Symmetry (worst)", "symmetry_worst"),
        ("Fractal dimension (worst)", "fractal_dimension_worst"),
    ]

    for label, key in slider_labels:
        st.sidebar.slider(
            label=label,
            min_value=float(0.0),
            max_value=float(data[key].max()),
            value=float(data[key].mean())
        )


def main():
    st.set_page_config(
        page_title="Prima",
        page_icon=":tulip:",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.write("Bem vindo(a) ao Prima App")

    add_sidebar()

    with st.container():
        st.title("Prima - Previsor de Risco e Identificador Mamográfico")
        st.write("O PRIMA é um aplicativo demonstrativo que, ao se conectar ao seu laboratório de citologia, auxilia no diagnóstico de câncer de mama a partir de amostras de tecido. Este aplicativo emprega um modelo de aprendizado de máquina para prever se uma massa mamária é benigna ou maligna, com base nas medições fornecidas pelo seu laboratório. Além disso, você pode ajustar as medições manualmente utilizando os controles deslizantes disponíveis na barra lateral.")

    col1, col2 = st.columns([4,1])

    with col1:
        st.write("coluna 1")
    with col2:
        st.write("coluna 2")


if __name__ == '__main__':
    main()