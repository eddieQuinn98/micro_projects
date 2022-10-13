from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


names = {
    "edward": {"age":24, "sex":"male"},
    "peter": {"age":19, "sex":"male"},
    "alice": {"age":19, "sex":"female"}
    }


class HelloWorld(Resource):

    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)