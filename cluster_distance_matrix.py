import numpy as np
from sklearn.manifold import TSNE
import pickle

X_embedded = TSNE(n_components=2, metric='precomputed').fit_transform(X)