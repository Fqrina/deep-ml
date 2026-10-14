import numpy as np
def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	points = np.array(points)
	initial_centroids = np.array(initial_centroids)
	dis = np.sum((points[:, None, :] - initial_centroids[None, :, :])**2, axis=2) #6,2
	cls = np.argmin(dis, axis=1) #6
	for i in range(max_iterations):
		new_centroids = np.array([np.mean(points[cls == j], axis=0) if len(points[cls==j]) > 0 else initial_centroids[j] for j in range(k)]) #2
		if np.array_equal(new_centroids, initial_centroids):
			return [tuple(centroid) for centroid in new_centroids]
		# print(i, " , ", new_centroids, " , ", initial_centroids)
		initial_centroids = new_centroids
		dis = np.sum((points[:, None, :] - initial_centroids[None, :, :])**2, axis=2)
		cls = np.argmin(dis, axis=1)