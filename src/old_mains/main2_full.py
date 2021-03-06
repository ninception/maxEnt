from __future__ import division
import pickle
import numpy as np
import itertools
#from matplotlib import pyplot as plt

import sys
#path_to_codebase = '/mnt/Study/umass/sem3/maxEnt/src/codebase/'
path_to_codebase = './codebase/'
sys.path.insert(0, path_to_codebase)
from codebase.utils import load_disease_data
from codebase.extract_features import ExtractFeatures
from codebase.optimizer import Optimizer

#filePath = '../data/test1-fy.csv'
filePath = '../data/2010-2014-fy.csv'
entropy_est = 'JAMES-STEIN'
k_val = 60 

data_array = load_disease_data(filePath)
#feats = ExtractFeatures(data_array, entropy_est, k_val)
#feats.compute_topK_feats_approx()
#feats.partition_features()

filename = "../out/pickles/feats_obj_full.pk"
with open(filename, 'rb') as rfile:
    feats = pickle.load(rfile)

opt = Optimizer(feats) 
soln_opt = opt.solver_optimize()
optlist = [opt, soln_opt]
outfilename = '../out/pickles/opt_obj_full.pk'

with open(outfilename, "wb") as outfile:
    pickle.dump(opt, outfile)
    pickle.dump(soln_opt, outfile)
    pickle.dump(optlist, outfile)

