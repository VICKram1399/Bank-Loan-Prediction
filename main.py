# importing neccesary dependencies:
import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def homepage():
    return render_template('index.html')

# prediction function:
def ValuePredictor(to_predict_list):
    to_predict= np.array(to_predict_list).reshape(1,11)
    loaded_model= pickle.load(open('model_2','rb'))
    result= loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods=['POST'])
def result():
    if request.method=='POST':
        to_predict_list= request.form.to_dict()
        to_predict_list= list(to_predict_list.values())
        to_predict_list= list(map(float, to_predict_list))
        pred= ValuePredictor(to_predict_list)
        if float(pred)== 1:
            prediction= "CONGRATULATIONS Your Loan Can Be Approved!!"
        else:
            prediction= "SORRY Your Loan Application Is Rejected"
        return render_template('results.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
