import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

df = pd.read_csv('breast-cancer.csv')
print(df.head())
x = df.drop(columns=['id', 'diagnosis'], axis=1)
y = df['diagnosis']
modelo = LogisticRegression(max_iter=10000)
modelo = LogisticRegression()
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)
modelo.fit(x_treino, y_treino)
y_previsto = modelo.predict(x_teste)
cm = confusion_matrix(y_previsto, y_teste)
plot_confusion_matrix(cm)
