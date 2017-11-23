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

# NNL_MAPS_JER002367093.jpg
# NNL_MAPS_JER002367094.jpg

# NNL_MAPS_JER002367095.jpg
# NNL_MAPS_JER002367097.jpg

# NNL_MAPS_JER002366921.jpg

# NNL_MAPS_JER002366853.jpg
# NNL_MAPS_JER002366854.jpg

# NNL_MAPS_JER002366846.jpg
# NNL_MAPS_JER002366847.jpg

# NNL_MAPS_JER002366848.jpg
# NNL_MAPS_JER002366849.jpg

# NNL_MAPS_JER002366850.jpg

# NNL_MAPS_JER002366843.jpg