from importlib.resources import Resource

import pandas as pd
import pyodbc
from fbprophet import Prophet
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import pickle

from pyexpat import model

from flask.json import JSONEncoder
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

conn = pyodbc.connect('Driver={SQL Server};'  # connect with SQL server
                      'Server=DESKTOP-05ICLAS\\SERVER2;'
                      'Database=DUAN_KHUCNC;'
                      'Trusted_Connection=yes;')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printPerson(self):
        print(self.name + " " + self.age)


myList = [Person("hieu", 15), Person("Trung", 37), Person("Dat", 18)]


class Company:
    def __init__(self, SO_CNDKKD, TEN_DN):
        self.SO_CNDKKD = SO_CNDKKD
        self.TEN_DN = TEN_DN


# funtion release

# get company name from db
list_company = pd.read_sql_query('SELECT SO_CNDKKD ,TEN_DN FROM dbo.DOANHNGHIEP', conn)


# logic

# Controller
class GetAllCompany(Resource):
    def get(self):
        listOfReading = [(Company(row.SO_CNDKKD, row.TEN_DN)) for index, row in list_company.iterrows()]
        response = [vars(ob) for ob in listOfReading]
        return response


api.add_resource(GetAllCompany, "/api/getAllCompany")


# end


# begin test
class HelloWorld(Resource):
    def get(self, name, test):
        return {"name": name, "test": test}


class ABC(Resource):
    def get(self):
        listOfReading = [(Company(row.SO_CNDKKD, row.TEN_DN)) for index, row in list_company.iterrows()]
        respone = [vars(ob) for ob in listOfReading]
        # json.dumps([ob.__dict__ for ob in myList])
        return respone


api.add_resource(ABC, "/")


# @app.route('/api/', methods=['GET'])
# def hello_world():
#     return 'Hello World!'+request.args.get('name') + request.args.get('age')


# @app.route('/api/', methods=['POST'])
# def hello_world():
#     # return 'Hello World!' + request.form.get('name') + request.form.get('age')
#     final_permistion = open("E:\\do_an_tot_nghiep\\Source\\service\data\\final_prediction.pickle",'rb')
#     pickle_data = pickle.load(final_permistion)
#     return pickle_data.to_json()

@app.route('/api/', methods=['POST'])
def hello_world():
    # return 'Hello World!' + request.form.get('name') + request.form.get('age')
    final_permistion = open("E:\\do_an_tot_nghiep\\Source\\service\data\\final_prediction.pickle", 'rb')
    m = Prophet()
    m = pickle.load(final_permistion)
    future = m.make_future_dataframe(periods=10)  # so ngay can du bao
    future.tail()

    forecast = m.predict(future)
    a = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

    print(a)
    return a.to_json()


@app.route('/api/apc', methods=['GET'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)


# end test
if __name__ == '__main__':
    app.run(debug=True)
