"""
Convert OpenFace aus output to aus_openface.pkl
1. CSV_PATH for path that contains csv files of AUs extracted using OpenFace.
2. savePKL_PATH for path to save the output file.
"""

import pandas as pd
import numpy as np
import os
import pickle

CSV_PATH = ""
savePKL_PATH = ""

# create dict to record {filename : col 2 to 19}

CSV_files = [file for file in os.listdir(CSV_PATH) if file.endswith('.csv')]

csv_dict = dict()

for file in CSV_files:
    arr = pd.read_csv(CSV_PATH+file).to_numpy()
    
    key = file[:-4]
    value = arr[0,2:19]
    csv_dict[key] = value

# save dict as pkl
pickle.dump(csv_dict, open(os.path.join(savePKL_PATH, "aus_openface.pkl"), "wb" ) )