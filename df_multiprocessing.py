import pandas as pd
import pickle
from multiprocessing import Pool
import numpy as np
import os


def function_processing(dataframe):
    # An example of a function with complicated logic
    for column in df.columns:
        dataframe[str(column) + '_new'] = \
            dataframe[column].apply(lambda x: 'error'
                                    if len(str(x).split('5')) >= 4
                                    else np.sin(x))
    return dataframe


def multiprocessing_apply(dataframe, function):
    chunks = np.array_split(dataframe, os.cpu_count() - 1, axis=0)

    with Pool(processes=os.cpu_count() - 1) as pool:
        results = pool.map(function, chunks)

    return pd.concat(results)


if __name__ == '__main__':
    df = pickle.load(open('df.pickle', 'rb'))
    df = multiprocessing_apply(df, function_processing)
