import joblib
from feat_eng import feat_eng_data 


def predict(months):
    X_flc = feat_eng_data(months)

    vot_reg = joblib.load("model.sav")
                          
    return vot_reg.predict(X_flc)
    