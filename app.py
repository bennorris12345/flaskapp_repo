from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import os

import pickle
import pandas as pd
import sklearn

app=Flask(__name__)
base_dir=os.path.abspath(os.path.dirname(__file__))#this returns the base director of where we are working.
db_path=os.path.join(base_dir, 'kubrick.db') #so we can change file to kubrick database we have made.

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+db_path
db=SQLAlchemy(app)


@app.route('/')
def home():
    return jsonify(data='Welcoto my flask api home. v2')

#http://127.0.0.1:5000/get_consultant?email=bennorris@kubrickgroup.com
@app.route('/ishealthy')
def ishealthy():
    weight = request.args.get('weight', 0)
    height = request.args.get('height', 0)
    IsMale = request.args.get('IsMale', 1)

    # retrieve consultant info from database by name
    result_binary=model.predict(pd.DataFrame([[IsMale,weight,height]]))

    if result_binary[0]==0:
        result='This Person Is Not Healthy'
    elif result_binary[0]==1:
        result='This person Is Healthy'
    if IsMale==0:
        IsMale='Female'
    elif IsMale==1:
        IsMale='Male'

    return jsonify(weight=weight, height=height, IsMale=IsMale, result=str(result))

if __name__=='__main__':
    model=pickle.load(open(r'/code/model_bmi.pickle','rb'))
    app.run(host='0.0.0.0')
