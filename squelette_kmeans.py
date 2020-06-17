import numpy as np
import pandas as pd



#import df

# df = ...

X = df.values

#verifier la dimension de X pour qu'elle soit de deux colonnes



def generate_one_centroid(X):
	"""
	retourn les coordinées d'un centroid choisit aléatoirement dans X

	"""
	return centroid





def generate_label(X, centroid1, centroid2):
	"""
	Pour chaque centroid, retourne la distance est calculé
	retourn le label de chaque point : une array qui va être un vecteur (array numpy one dimension), [0,1,0,1,0,1,1,0,1,0....]
	"""
	return label


def compute_new_cendroid_position(X, label):
	"""
	retourn la position des nouveaux cenroids

	"""
	return new_centroid1, new_centroid2



def plot_graph(X, label, centroid1, centroid2):
	"""
	retourn rien, affiche le graphe avec en coloration différente les clusters

	"""


centroid1 = generate_one_centroid(X)
centroid2 = generate_one_centroid(X)


label = generate_label(X, centroid1, centroid2)

new_centroid1, new_centroid2 = compute_new_cendroid_position(X, label)


while np.round(new_centroid1,3) != np.round(centroid1,3) and np.round(new_centroid2,3) != np.round(centroid2,3):
	centroid1, centroid2 = new_centroid1, new_centroid2
	label = generate_label(X, centroid1, centroid2)
	new_centroid1, new_centroid2 = compute_new_cendroid_position(X, label)
	plot_graph(X, label, centroid1, centroid2)
