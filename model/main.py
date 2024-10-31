import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

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

    #testar model
    y_prediction = model.predict(x_test)
    print("Accuracy: ", accuracy_score(y_test, y_prediction))
    print("Classification report:\n", classification_report(y_test, y_prediction))

    return model, scaler

def get_clean_data():
    data_path = os.path.join(os.path.dirname(__file__), "../data/data-wisconsin.csv")

    data = pd.read_csv(data_path)

    data = data.drop(['Unnamed: 32', 'id'], axis=1)

    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

    return data

def main():
    data = get_clean_data()

    model, scaler = create_model(data)

    # salvar o modelo e o scaler
    joblib.dump(model, './model.pkl')
    joblib.dump(scaler, './scaler.pkl')

    
if __name__ == '__main__':
    main()