import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def create_model(data):
    x = data.drop(['diagnosis'], axis=1)
    y = data['diagnosis']

    #escalar os dados
    scaler = StandardScaler()
    x = scaler.fit_transform(x)

    #dividir os dados
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=31)

    #treinar model
    model = LogisticRegression()
    model.fit(x_train, y_train)

    return model, scaler


def get_clean_data():
    data = pd.read_csv("data\data-wisconsin.csv")

    data = data.drop(['Unnamed: 32', 'id'], axis=1)

    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

    return data


def main():
    data = get_clean_data()

    model, scaler = create_model(data)
    
if __name__ == '__main__':
    main()