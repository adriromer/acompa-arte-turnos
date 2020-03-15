from flask import Flask
from flask import url_for
from flask import json
from flask import request
from flask import abort
import doctors

import logging

app = Flask(__name__)
doc_data = doctors.DoctorData()

@app.route('/doctors', methods = ['GET'])
def api_doctors():

#   Api que devuelve la lista de todos los terapistas
    return json.dumps(doc_data.get_doctors())

#    return json.dumps(hola mundo)
#    ejemplo para imprimir en consola el objeto doc_data.get_doctors y tambien escribirlo en un archivo
#    app.logger.info('Processing default request')
#    print(doc_data.get_doctors())
#    with open("data_file.json", "w") as write_file:
#        json.dump(doc_data.get_doctors(), write_file)


@app.route('/appointments', methods = ['GET', 'POST', 'DELETE'])
def api_appointments():
    """ API to GET, POST and DELETE appointments. """
    try:
        if (request.method == 'POST' and request.headers['Content-Type'] == 'application/json'):
            return json.dumps(doc_data.add_appointment(request.json))
        elif request.method == 'GET':
            app.logger.info(request.json)
            return json.dumps(doc_data.get_appointments(request.json["doc_id"], request.json["date"]))
        elif request.method == 'DELETE':
            return json.dumps(doc_data.del_appointment(request.json["doc_id"], request.json["date"], request.json["apt_id"]))
    except (ValueError, KeyError) as exception:
        app.logger.error(exception)
        abort(400, description=exception)

if __name__ == '__main__':

#    print(doc_data.get_doctors())
    app.run(debug=True)
