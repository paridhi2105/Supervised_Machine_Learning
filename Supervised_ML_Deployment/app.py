import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
Linear_Regression = pickle.load(open('Linear_Regression.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    feature = [float(x) for x in request.form.values()]
    final_feature = np.array(feature).reshape(-1,1)
    prediction = Linear_Regression.predict(final_feature)
    prediction=float(prediction)
    

    return render_template('index.html', prediction_text='Percentage should be {}'.format(prediction))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = Linear_Regression.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)