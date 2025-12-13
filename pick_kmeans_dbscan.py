from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score

X_pca = None

kmeans = KMeans(n_clusters=5, random_state=42)
labels_kmeans = kmeans.fit_predict(X_pca)
score_kmeans = silhouette_score(X_pca, labels_kmeans)

dbscan = DBSCAN(eps=0.5, min_samples=5)
labels_dbscan = dbscan.fit_predict(X_pca)
mask = labels_dbscan != -1
score_dbscan = silhouette_score(X_pca[mask], labels_dbscan[mask])

print("Silhouette KMeans: ", score_kmeans)
print("Silhouette DBSCAN: ", score_dbscan)