import numpy as np
from sklearn.manifold import TSNE
import os
from sklearn.cluster import DBSCAN
import pickle
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import euclidean_distances

style_dir = 'ephemera'
img_list = os.listdir(style_dir)

mtx = pickle.load(open('{}.pickle'.format(style_dir),'rb'))
pca = PCA(n_components=2)
X_after_PCA = pca.fit_transform(mtx.reshape(mtx.shape[0], mtx.shape[1] * mtx.shape[2]))



# img_list = pickle.load(open('/Users/michaeldoron/makers/NLI/NLIhackton2107/{}_image_list.pickle'.format(style_dir),'rb'))[1:]
fig, ax = plt.subplots(figsize=(10,10))
artists = []
for image_ind in range(len(img_list)):
	try:
		im = OffsetImage(plt.imread('{}/{}'.format(style_dir, img_list[image_ind])), zoom=0.03)
		x, y = X_after_PCA[[image_ind], 0][0], X_after_PCA[[image_ind], 1][0]
		x, y = np.atleast_1d(x, y)
		ab = AnnotationBbox(im, (x, y), xycoords='data', frameon=False)
		ax.update_datalim(np.column_stack([x, y]))
		artists.append(ax.add_artist(ab))
		ax.autoscale()
	except:
		pass

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.tick_params(direction='in', width=0, size=0)
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
plt.savefig('{}_small.pdf'.format(style_dir), transparent=True, bbox_inches='tight', format='pdf', dpi=300)

PCA_distance_matrix = euclidean_distances(X_after_PCA[:,0], X_after_PCA[:,1])
