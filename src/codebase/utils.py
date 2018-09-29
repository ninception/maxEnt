import pandas as pd
import numpy as np 


# Perform all utility taks here
# Etc data loading, data cleaning etc.
# Removing missing values, extra columns

def load_data(filePath):
    df = pd.read_csv(filePath)
    df1 = df.drop(['fyAGE', 'CCCfy98.1'], axis=1) # erroneous column. CCCfy98 repeated in original csv file
    tups = [tuple(x) for x in df1.values]

    data_arr = np.asarray(tups)

    return data_arr


####### CSV FILE HEADERS ######
# #Index([u'fyAGE', u'CCCfy49', u'CCCfy53', u'CCCfy98', u'CCCfy98.1', u'CCCfy100',
#        u'CCCfy101', u'CCCfy128', u'CCCfy204', u'CCCfy205', u'CCCfy651',
#        u'CCCsy49', u'CCCsy53', u'CCCsy98', u'CCCsy100', u'CCCsy101',
#        u'CCCsy128', u'CCCsy204', u'CCCsy205', u'CCCsy651'],
#       dtype='object')

def load_data_1yr(filePath):
    df = pd.read_csv(filePath)
    #### Erroneous column. CCCfy98 repeated in original csv file ####
    ### No need for AGE since its same for all ###
    df = df.drop(['fyAGE', 'CCCfy98.1'], axis=1) 

    drop_list = ['CCCsy49', 'CCCsy53', 'CCCsy98', 'CCCsy100', 'CCCsy101', 'CCCsy128', 'CCCsy204', 'CCCsy205', 'CCCsy651']
    df2 = df.drop(drop_list,axis=1) 
    tups = [tuple(x) for x in df2.values]

    data_arr = np.asarray(tups)

    return data_arr


def load_data_merge(filePath):
    df = pd.read_csv(filePath)
    df1 = df.drop(['fyAGE', 'CCCfy98.1'], axis=1) # erroneous column. CCCfy98 repeated in original csv file
    tups = [tuple(x) for x in df1.values]

    data_arr = np.asarray(tups)

    cols = data_arr.shape[1]
    clim = int(cols/2)
    for vec in data_arr:
        for i in range(int(cols/2)):
            vec[i] = vec[i] ^ vec[cols - 1 -i]

    data_arr = data_arr[:, :clim]

    return data_arr