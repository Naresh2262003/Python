import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['target'] = iris.target
data['species'] = data['target'].apply(lambda x: iris.target_names[x])

# Part (a): Bar chart for frequency of each class label
class_counts = data['species'].value_counts()
plt.figure(figsize=(8, 5))
class_counts.plot(kind='bar', color=['skyblue', 'orange', 'green'])
plt.title('Frequency of Each Class Label', fontsize=14)
plt.xlabel('Class Label', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(rotation=0)
plt.legend(['Frequency'])
plt.show()

# Part (b): Scatter plot for Petal width vs Sepal width
plt.figure(figsize=(8, 5))
plt.scatter(data[iris.feature_names[1]], data[iris.feature_names[3]], c=data['target'], cmap='viridis', edgecolor='k')
plt.title('Scatter Plot: Petal Width vs Sepal Width', fontsize=14)
plt.xlabel('Sepal Width (cm)', fontsize=12)
plt.ylabel('Petal Width (cm)', fontsize=12)
plt.colorbar(label='Class Label')
plt.show()

# Part (c): Density distribution for Petal length
plt.figure(figsize=(8, 5))
sns.kdeplot(data[iris.feature_names[2]], shade=True, color='purple')
plt.title('Density Distribution of Petal Length', fontsize=14)
plt.xlabel('Petal Length (cm)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.show()

# Part (d): Pair plot for pairwise bivariate distribution
sns.pairplot(data, hue='species', diag_kind='kde', palette='husl')
plt.show()
