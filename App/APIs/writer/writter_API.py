from flask_restful import Resource


class writerResource(Resource):
    def get(self):
        return {"msg": "successfully got"}