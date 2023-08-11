import numpy as np
import pandas as pd

experiment_file = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

experiment_file.to_csv('Experiment.csv', sep=',')
