"""Exercício 15 — Pipeline de Machine Learning (exemplo)

Organize as etapas de um projeto de Machine Learning: carregar dados, separar treino e teste, treinar, realizar previsões e avaliar o modelo.

Pseudocódigo:

    INÍCIO
        dataset ← CARREGAR_DADOS()
        dados_treino, dados_teste ← SEPARAR_DADOS(dataset)
        modelo ← TREINAR_MODELO(dados_treino)
        previsoes ← REALIZAR_PREVISOES(modelo, dados_teste)
        resultado ← AVALIAR_MODELO(previsoes, dados_teste)
        MOSTRAR resultado
    FIM
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

dataset_X, dataset_y = load_iris(return_X_y=True)

dados_treino_X, dados_teste_X, dados_treino_y, dados_teste_y = train_test_split(
    dataset_X, dataset_y, test_size=0.2, random_state=42
)

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(dados_treino_X, dados_treino_y)

previsoes = modelo.predict(dados_teste_X)

resultado = accuracy_score(dados_teste_y, previsoes)
print("Acurácia do modelo: " + str(round(resultado, 2)))
