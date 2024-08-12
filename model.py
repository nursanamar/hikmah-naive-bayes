import pickle
import pandas as pd
import os

dirname = os.path.dirname(__file__)

model_path = os.path.join(dirname,"model/naive_bayes_model.sav")
encoders_path = os.path.join(dirname,"model/label_encoder.sav")

model = pickle.load(open(model_path, 'rb'))
encoders = pickle.load(open(encoders_path, 'rb'))

def predict(input):
    df = pd.DataFrame(input)
    
    # Encode
    for col, _ in encoders.items():
        if col in df:
            df[col] = encoders[col].transform(df[col])
            
    #predict
    predictions = model.predict(df)
    
    return predictions


# Hanya untuk test function
if __name__ == "__main__":
    result = predict({
        'ips1': [3.78], 
        'ips4': [3.76], 
        'pemrograman_berorientasi_objek': ["A"] 
    })
    
    print(result)