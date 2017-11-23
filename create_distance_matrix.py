import pickle
import keras.backend as K
import numpy as np
from scipy.linalg import sqrtm

style_dir = 'maps'

mtx = pickle.load(open('{}.pickle'.format(style_dir),'rb'))

other_distance_matrix = np.zeros(shape=(mtx.shape[0],mtx.shape[0]))

for ind_1 in range(other_distance_matrix.shape[0]):
	for ind_2 in range(other_distance_matrix.shape[1]):
		# distance_matrix[ind_1, ind_2] = np.mean(sqrtm(mtx[ind_1,:,:] - mtx[ind_2,:,:]), axis=(0, 1)).real
		other_distance_matrix[ind_1, ind_2] = np.linalg.norm((mtx[ind_1,:,:] - mtx[ind_2,:,:]), axis=(0, 1)).real

plt.figure()
plt.imshow(other_distance_matrix)
plt.colorbar()