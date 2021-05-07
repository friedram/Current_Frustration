from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


# dummy data for end points
input = open('data.json')
data = json.load(input)
hospital = data['hospital']
services = data['services']
complaint = data['complaint']


class Services(Resource):
    def get(self):
        return {"services":services}


class Complaints(Resource):
    def get(self):
        return {"complaints":complaint}

    def post(self):
        print(request)
        complaint.append({
            "name":request.json['name'],
            "email":request.json['email'],
            "contact":request.json['contact'],
            "description":request.json['description']
            })

        with open('data.json', 'w') as data_file:
            data['complaint'] = complaint
            json.dump(data, data_file)

        return {'status': 'success'}

class Hospital(Resource):
    def get(self):
        return {"hospitals":hospital}

    def post(self):
        hospital.append({
            "name":request.json['name'],
            "cleanliness":request.json['cleanliness'],
            "facilities":request.json['facilties'],
            "doc-behaviour":request.json['doc-behaviour'],
            "quality-of-service":request.json['quality-of-service']
        })

        with open('data.json', 'w') as data_file:
            data['hospital'] = hospital
            json.dump(data, data_file)

        return {'status':'success'}

# https://stackoverflow.com/questions/25149493/how-to-call-another-webservice-api-from-flask
from urllib.request import urlopen

@app.route('/hello')
def hello():
    with urlopen('http://localhost:3002/giveMeACat') as r:
        text = r.read()
    return text

api.add_resource(Services, '/services')
api.add_resource(Complaints, '/complaints')
api.add_resource(Hospital, '/hospital')

if __name__ == '__main__':
    app.run(debug=True)