import tensorflow as tf

# dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])
# dataset = dataset.map(lambda x: x*2)
# for data in dataset:
#     print(data)


import numpy as np
import tensorflow as tf
from tensorflow.keras.layers.experimental import preprocessing

data = np.array([[0.1, 0.2, 0.3], [0.8, 0.9, 1.0], [1.5, 1.6, 1.7],])
layer = preprocessing.Normalization()
layer.adapt(data)
normalized_data = layer(data)

print("Features mean: %.2f" % (normalized_data.numpy().mean()))
print("Features std: %.2f" % (normalized_data.numpy().std()))