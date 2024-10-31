<h1 style="margin: 0; align="center";">
    <img src='https://github.com/user-attachments/assets/c7ddec0d-da95-477f-abe4-35b69e0531e7' alt="Ícone" width="32" height="32"> PRIMA - Preditor de Diagnóstico de Câncer de Mama
</h1>

## 🌐 Visão Geral

O web app **PRIMA (Preditor de Risco e Identificador Mamográfico)** é uma ferramenta impulsionada por Machine Learning, projetada para auxiliar profissionais da saúde no diagnóstico de câncer de mama. Utilizando um conjunto de medições, o aplicativo prevê se uma massa mamária é benigna ou maligna. Ele oferece uma representação visual dos dados de entrada por meio de um gráfico radar e exibe o diagnóstico previsto, além da probabilidade de ser benigno ou maligno. As medições podem ser inseridas manualmente ou o app poderia ser conectado à um laboratório de citologia para obter os dados diretamente de uma máquina. No entanto, a conexão direta com a máquina do laboratório não faz parte do aplicativo em si.

O app foi desenvolvido como um projeto de estudo de machine learning a partir do dataset público [Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data). Observe que este conjunto de dados pode não ser confiável, pois este projeto foi criado apenas para fins de aprendizado pessoal no campo de Machine Learning e não para uso profissional à princípio.

Você pode acessar uma versão ao vivo do aplicativo na plataforma [Streamlit Community Cloud](https://prima-app.streamlit.app).

## 🛠️ Funcionalidades
- 🔬 **Diagnóstico Previsível:** Predição da benignidade ou malignidade de massas mamárias com base em medições.
- 📊 **Visualização dos Dados:** Gráfico radar que representa visualmente as medições e facilita a análise.
- 📈 **Probabilidades:** Exibição da probabilidade de uma massa ser benigna ou maligna.
- 🛠️ **Entrada de Dados Flexível:** Opção de inserir medições manualmente ou integração com laboratório para coleta de dados.

## 💻 Tecnologias Utilizadas
- **Machine Learning:** scikit-learn
- **Manipulação de Dados:** pandas
- **Visualização Gráfica:** Plotly
- **Interface do Usuário:** Streamlit
- **Processamento Numérico:** NumPy
- **Persistência de Modelos:** Joblib

## Instalação
Recomenda-se que você rode o aplicativo dentro de um ambiente virtual para facilitar o gerenciamento das dependências. Abaixo estão as etapas recomendadas para configurar um ambiente com o conda.

Para criar um novo ambiente chamado prima-app, execute:

```bash
conda create -n prima-app python=3.12 
```

Em seguida, ative o ambiente com:

```bash
conda activate prima-app
```

Para instalar os pacotes necessários, execute:

```bash
pip install -r requirements.txt
```
Isso instalará todas as dependências necessárias.

## Uso

Para iniciar o aplicativo, basta executar o seguinte comando:

```bash
streamlit run app/main.py
```
Isso abrirá o aplicativo no seu navegador padrão. A partir daí, você pode carregar uma imagem de células para análise e ajustar várias configurações para personalizar a análise. Quando estiver satisfeito com os resultados, é possível exportar as medições para um arquivo CSV para análises adicionais.

<br>
<br>
<strong>Desenvolvido por: Beatriz Costa</strong><br>
Inspirado por: Alejandro AO

