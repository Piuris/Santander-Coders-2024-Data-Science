import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv('usa.csv')
print(df.head())
x = df[['AVG. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
        'Area Population']]
y = df['price']
x_treino, x_teste, y_treino, y_teste = train_test_split()
modelo = LinearRegression()
modelo.fit(x_treino, y_treino)
y_previsto = modelo.predict(x_teste)
print(y_previsto)
