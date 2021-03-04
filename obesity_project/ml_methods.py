import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

def RunPrediction(form_inputs):
    prediction_sample = np.array(form_inputs).reshape(1,-1)
    error_flag, predicted_result =  predictObesity(prediction_sample)

    return predicted_result 


def predictObesity(prediction_sample) -> []: 

    ### Initialize:
    # Intialize error = No
    error_flag = False
    predicted_result = None

    try:
        # Predict result:

        # Convert input to dataframe
        input_df = pd.DataFrame(prediction_sample)

        # Load the model from disk
        # filename = "data/model_lin.sav"
        # filename = "data/model_grb.sav"
        filename = "data/model_rfr.sav"
        # filename = "data/model_log.sav"
        # filename = "data/model_knn.sav"
        # filename = "data/model_svm.sav"
        model = pickle.load(open(filename, 'rb'))

        # Predict the result from model 
        predicted_result = model.predict(input_df)
        print(("Predicted result : {}").format(predicted_result))

    except Exception as e:
        print(('Exception occured : {}').format(e))
        error_flag = True

    
    # Return
    return error_flag, predicted_result
