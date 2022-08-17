from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def train_kmeans(X):
    kmeans = KMeans(n_clusters=2, n_init=1, init="k-means++", verbose=1)
    kmeans.fit(X)
    return kmeans
data=pd.read_csv('observacoes.txt', sep="  ", header=None, engine="python")
data.columns = ["x", "y"]
kmeans = train_kmeans(data)

transformed_data = kmeans.fit_transform(data)
print(kmeans.labels_)
print(kmeans.cluster_centers_)
print(kmeans.inertia_)
print(transformed_data)

label = kmeans.fit_predict(transformed_data)
filtered_label0 = transformed_data[label == 0]
filtered_label1 = transformed_data[label == 1]
plt.scatter(filtered_label0[:,0] , filtered_label0[:,1])
plt.scatter(filtered_label1[:,0] , filtered_label1[:,1])
plt.savefig("clusters.png")

mse = [
    583.8033335282207,
    515.1178271371449,
    511.9148247334133,
    511.1360873242597,
    510.60274513004094,
    509.447662236641,
    506.9438881104418,
    482.1341261458277,
    405.1266322687888,
    349.40922943993127,
    341.35283273256323,
    340.6367877954994,
]

plt.figure()
plt.plot(range(0,12),mse)
plt.savefig("MSE.png")