# Rest api  Service

# Import framework
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

# Instantiate the app
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

# Default data
dic = [{'name': "madam"},
        {'name': "Raam"},
        {'name': "Ganesh"},
        {'name': "aba"},
        {'name': "sam"}
]
# List the resource
class lst(Resource):
    def get(self):
        return dic
# Add fields 
class add(Resource):
    def put(self,nam):
        dic.append({'name': nam})
        return dic
# Find value
class find(Resource):
    def get(self,nam):
        for i in range(len(dic)):
            if dic[i]['name'] == nam:
                if nam == nam[::-1]:
                    return [{'name':'true'}]
                else:
                    return [{'name':'false'}]
# Delete value
class dlt(Resource):
    def delete(self,nam):
        for i in range(len(dic)):
            if dic[i]['name'] == nam:
                del dic[i]
        return dic

# Create routes
api.add_resource(lst, '/list')
api.add_resource(add, '/add/<string:nam>', methods=['PUT'])
api.add_resource(find, '/find/<string:nam>')
api.add_resource(dlt, '/delete/<string:nam>', methods=['DELETE'])

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
