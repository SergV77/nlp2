#!/usr/bin/python
#-*- coding: utf-8 -*-

from locLib import *
from handler import *


from flask import Flask
app = Flask(__name__)

@app.route('/')
def test():
    return 'Мое Flask приложение в докере!'


@app.route('/requestApi', methods=['POST'])
def requestApi():

    symptoms_list = request.json['symptom']
    print(symptoms_list)

    url = 'https://cs.socmedica.com/api/pars/ParsingConcept'

    param = {'key': '9244f7d34ca284b1',
             'lib': [25],
             'text': symptoms_list
             }

    response = requests.post(url, param)
    outs = response.json()
    #print(outs)

    conceptName = []
    conceptId = []
    conceptCh = []

    for out in outs['Result']:
        print(out['nameConcept'])
        print(out['idConcept'])        
        print(out['chance'])
        conceptName.append(out['nameConcept'])
        conceptId.append(out['idConcept'])
        conceptCh.append(out['chance'])

    diagnosis = handlerConcept(conceptId)

    result = {}
    for keys, values in diagnosis.items():
        result[keys] = round(values, 2)


    #result = {'Имя концепта': conceptName, 'ID концепта': conceptId, 'Вероятность концепта': conceptCh}
    

    return result






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

