import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

import numpy as np

celsius_list = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit_list = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

for i,c in enumerate(celsius_list):
	print("{} degrees Celsius = {} degrees Fahrenheit".format(c,fahrenheit_list[i]))
