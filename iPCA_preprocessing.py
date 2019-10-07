#!/usr/bin/env python
# coding: utf-8

# In this case dataset file is too large for our RAM and we can not read it as usual.
# Every entry has 13 features and one binary label. In order to avoid "Out-of-memory" errors, we need to preprocess our dataset.
# For this purpose i use StandardScaler for scaling and IncrementalPCA for preprocessing data.

import numpy as np
import pandas as pd
from sklearn.decomposition import IncrementalPCA
from sklearn.preprocessing import StandardScaler

# I select 10000 rows per chunk to be sure, that it will be finished (i have only 2 Gb RAM)

chunk_size = 10000
components = 3

# Only three components is not good idea, but i have huge dataset and after preprocessing my data also can be large.

for chunk in pd.read_csv('train.tar.gz', compression='gzip', sep=';', header=0, quotechar='"', chunksize=chunk_size):
    labels = chunk.iloc[:, 2]
    selected_features = chunk.iloc[:, [3:16]]

    scaled_features = StandardScaler().fit_transform(selected_features)

    ipca = IncrementalPCA(n_components=components)
    principalComponents = ipca.fit_transform(scaled_features)
    preprocessed_data = pd.DataFrame(data=principalComponents)

    merged_data = pd.concat([preprocessed_data, labels], axis=1)

    merged_data.to_csv('preprocessed_data.csv', mode='w', sep=';', header=0)

# P.S. Of course chunksize and number of components depends on your available computer resources.
