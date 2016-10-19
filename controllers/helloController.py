from flask_restful import Resource

class HelloController(Resource):

    def get(self):
        return {"response" : "hello get"} 
    
    def post(self):
        return {"response" : "hello post"}

    def put(self):
        return {"response" : "hello put"}

    def delete(self):
        return {"response" : "hello delete"}
