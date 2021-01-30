from flask import Flask, request
from flask_restful import Resource, Api
from models.model0 import Classifier

app = Flask(__name__)
api = Api(app)


class ToDoSimple(Resource):
    def get(self, todo_id):
        return {todo_id : todos[todo_id]}
    
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(ToDoSimple, '/<string:todo_id>')
## Needed to updated according to models/model0.py
model = Classifier()
class BugDetectorModel(Resource):
    def get(self, img):
        return {classname : "<Bug-Name>", bbox :{}}

if __name__ == '__main__':
    app.run(debug=True)