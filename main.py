import pandas as pd
import pydotplus
from IPython.display import Image
from sklearn import metrics
from sklearn.externals.six import StringIO
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz

# nazwy wszystkich kolumn z CSV
column_names = ['Elevation', 'Aspect', 'Slope', 'Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology',
                'Horizontal_Distance_To_Roadways', 'Hillshade_9am', 'Hillshade_Noon', 'Hillshade_3pm',
                'Horizontal_Distance_To_Fire_Points', 'Wilderness_Area1', 'Wilderness_Area2', 'Wilderness_Area3',
                'Wilderness_Area4', 'Soil_Type1', 'Soil_Type2', 'Soil_Type3', 'Soil_Type4', 'Soil_Type5', 'Soil_Type6',
                'Soil_Type7', 'Soil_Type8', 'Soil_Type9', 'Soil_Type10', 'Soil_Type11', 'Soil_Type12', 'Soil_Type13',
                'Soil_Type14', 'Soil_Type15', 'Soil_Type16', 'Soil_Type17', 'Soil_Type18', 'Soil_Type19', 'Soil_Type20',
                'Soil_Type21', 'Soil_Type22', 'Soil_Type23', 'Soil_Type24', 'Soil_Type25', 'Soil_Type26', 'Soil_Type27',
                'Soil_Type28', 'Soil_Type29', 'Soil_Type30', 'Soil_Type31', 'Soil_Type32', 'Soil_Type33', 'Soil_Type34',
                'Soil_Type35', 'Soil_Type36', 'Soil_Type37', 'Soil_Type38', 'Soil_Type39', 'Soil_Type40', 'Cover_Type']

# wczytujemy dataset
dataset = pd.read_csv("covtype.csv", header=None, names=column_names)

# wydzielamy zmienne załeżne
feature_cols = column_names[:-1]
X = dataset[feature_cols]
y = dataset.Cover_Type

# dzielimy dataset na zbiory do uczenia się i testów
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# trenujemy model
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("Dokładność: {}".format(metrics.accuracy_score(y_test, y_pred)))

dot_data = StringIO()

# generacja i eksport grafiki drzewka
# głębokość ustawiamy na 5 bo przy wartości powyzęj generuje się godzinami
export_graphviz(clf, max_depth=5, out_file=dot_data, filled=True, rounded=True, special_characters=True,
                feature_names=feature_cols)
print('Graphviz wygenerowany')
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('trees.png')
Image(graph.create_png())
print('End of script.')
