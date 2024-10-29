import streamlit as st
import joblib 
import pandas as pd
import plotly.graph_objects as go

def get_clean_data():
    data = pd.read_csv("../data/data-wisconsin.csv")

    data = data.drop(['Unnamed: 32', 'id'], axis=1)

    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

    return data

def add_sidebar():
    st.sidebar.header("Medições de núcleos celulares")
    data = get_clean_data()

    slider_labels = [
        ("Raio (média)", "radius_mean"),
        ("Textura (média)", "texture_mean"),
        ("Perímetro (média)", "perimeter_mean"),
        ("Área (média)", "area_mean"),
        ("Suavidade (média)", "smoothness_mean"),
        ("Compacidade (média)", "compactness_mean"),
        ("Concavidade (média)", "concavity_mean"),
        ("Pontos côncavos (média)", "concave points_mean"),
        ("Simetria (média)", "symmetry_mean"),
        ("Dimensão fractal (média)", "fractal_dimension_mean"),
        ("Raio (ep)", "radius_se"),
        ("Textura (ep)", "texture_se"),
        ("Perímetro (ep)", "perimeter_se"),
        ("Área (ep)", "area_se"),
        ("Suavidade (ep)", "smoothness_se"),
        ("Compacidade (ep)", "compactness_se"),
        ("Concavidade (ep)", "concavity_se"),
        ("Pontos côncavos (ep)", "concave points_se"),
        ("Simetria (ep)", "symmetry_se"),
        ("Dimensão fractal (ep)", "fractal_dimension_se"),
        ("Raio (pior)", "radius_worst"),
        ("Textura (pior)", "texture_worst"),
        ("Perímetro (pior)", "perimeter_worst"),
        ("Área (pior)", "area_worst"),
        ("Suavidade (pior)", "smoothness_worst"),
        ("Compacidade (pior)", "compactness_worst"),
        ("Concavidade (pior)", "concavity_worst"),
        ("Pontos côncavos (pior)", "concave points_worst"),
        ("Simetria (pior)", "symmetry_worst"),
        ("Dimensão fractal (pior)", "fractal_dimension_worst"),
    ]

    input_dict = {}

    for label, key in slider_labels:
        input_dict[key] = st.sidebar.slider(
            label=label,
            min_value=float(0.0),
            max_value=float(data[key].max()),
            value=float(data[key].mean())
        )
    
    return input_dict

def get_scaled_values(input_dict):
    data = get_clean_data()

    x = data.drop(['diagnosis'], axis=1)

    scaled_dict = {}

    for key, value in input_dict.items():
        max_value = x[key].max()
        min_value = x[key].min()
        scaled_value = ((value - min_value) / (max_value - min_value))
        scaled_dict[key] = scaled_value

    return scaled_dict

def get_radar_chart(input_data):

    input_data = get_scaled_values(input_data)
    categories = ['Raio', 'Textura', 'Perímetro', 'Área', 'Suavidade', 'Compacidade', 'Concavidade', 'Pontos Côncavos', 'Simetria', 'Dimensão Fractal']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_mean'], input_data['texture_mean'], input_data['perimeter_mean'],
            input_data['area_mean'], input_data['smoothness_mean'], input_data['compactness_mean'],
            input_data['concavity_mean'], input_data['concave points_mean'], input_data['symmetry_mean'],
            input_data['fractal_dimension_mean']
        ],
        theta=categories,
        fill='toself',
        name='Média'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_se'], input_data['texture_se'], input_data['perimeter_se'], input_data['area_se'],
            input_data['smoothness_se'], input_data['compactness_se'], input_data['concavity_se'],
            input_data['concave points_se'], input_data['symmetry_se'],input_data['fractal_dimension_se']
        ],
        theta=categories,
        fill='toself',
        name='Erro Padrão'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_se'], input_data['texture_se'], input_data['perimeter_se'], input_data['area_se'], input_data['smoothness_se'], input_data['compactness_se'], input_data['concavity_se'], input_data['concave points_se'], input_data['symmetry_se'],input_data['fractal_dimension_se']
        ],
        theta=categories,
        fill='toself',
        name='Erro Padrão'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_worst'], input_data['texture_worst'], input_data['perimeter_worst'],
            input_data['area_worst'], input_data['smoothness_worst'], input_data['compactness_worst'],
            input_data['concavity_worst'], input_data['concave points_worst'], input_data['symmetry_worst'],
            input_data['fractal_dimension_worst']
        ],
        theta=categories,
        fill='toself',
        name='Pior Valor'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 1]
        )),
    showlegend=True
    )

    return fig

def main():
    st.set_page_config(
        page_title="Prima",
        page_icon=":tulip:",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.write("Bem vindo(a) ao Prima App")

    input_data = add_sidebar()

    with st.container():
        st.title("Prima - Previsor de Risco e Identificador Mamográfico")
        st.write("O PRIMA é um aplicativo demonstrativo que, ao se conectar ao seu laboratório de citologia, auxilia no diagnóstico de câncer de mama a partir de amostras de tecido. Este aplicativo emprega um modelo de aprendizado de máquina para prever se uma massa mamária é benigna ou maligna, com base nas medições fornecidas pelo seu laboratório. Além disso, você pode ajustar as medições manualmente utilizando os controles deslizantes disponíveis na barra lateral.")

    col1, col2 = st.columns([4,1])

    with col1:
        radar_chart = get_radar_chart(input_data)
        st.plotly_chart(radar_chart)

    with col2:
        st.write("coluna 2")


if __name__ == '__main__':
    main()