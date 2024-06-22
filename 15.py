from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np

iris = load_iris()
X = iris.data  # Features (sepal length, sepal width, petal length, petal width)
y = iris.target  # Target (species)


clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

print("Enter the details of the new flower:")
sepal_length = float(input("Sepal Length (cm): "))
sepal_width = float(input("Sepal Width (cm): "))
petal_length = float(input("Petal Length (cm): "))
petal_width = float(input("Petal Width (cm): "))

new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
predicted_species = clf.predict(new_flower)

species_name = iris.target_names[predicted_species][0]
print(f"The predicted species of the new flower is: {species_name}")
