"""Any functionality that need to be written in common for the entire application
example if i want to read the dataset from a database i can write the MongoDB client here, if i want to save the model into the cloud"""

import os
import sys
import dill

import numpy as np
import pandas as pd

from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)