import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from tpot.builtins import DatasetSelector

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=85)

# Average CV score on the training set was:0.7012173913043479
exported_pipeline = make_pipeline(
    DatasetSelector(sel_subset=12, subset_list="module23.csv"),
    Normalizer(norm="l2"),
    RandomForestClassifier(bootstrap=True, criterion="entropy", max_features=0.05, min_samples_leaf=10, min_samples_split=14, n_estimators=100)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
