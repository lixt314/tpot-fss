import numpy as np
import pandas as pd
from sklearn.kernel_approximation import Nystroem
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier
from tpot.builtins import DatasetSelector

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=86)

# Average CV score on the training set was:0.6925217391304348
exported_pipeline = make_pipeline(
    DatasetSelector(sel_subset=4, subset_list="module23.csv"),
    Nystroem(gamma=0.30000000000000004, kernel="linear", n_components=4),
    DecisionTreeClassifier(criterion="gini", max_depth=2, min_samples_leaf=16, min_samples_split=20)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)