
 # Randomizing data, generating summary statistics and histogram

import numpy as np

mu = 80
sigma = 10

x = np.random.normal(mu,sigma, 100)

print("Random normal array mean centered ", x[:10])

print("mean", np.mean(x))
