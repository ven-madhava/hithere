import numpy as np
import cv2
import random
import copy
import math
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import h5py

# Necessary Flask imports
# -----------------------
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from json import dumps
from flask_jsonpify import jsonify

# Main class
# ----------
class printhellothere(Resource):

    def put(self,msid):

        # Setting up key values to accept
        # -------------------------------
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('age')
        args = parser.parse_args()

        output_message = 'Hi, ' + str(args['name']) + ', how are you doing at ' + str(int(args['age'])) + ' xx'
        output = {'msgid':msid, 'output_message': output_message}

        return output, 200

# Flask stuff
# -----------
app = Flask(__name__)
api = Api(app)
api.add_resource(printhellothere, '/hellothere/<string:msid>') # Route_1
if __name__ == '__main__':
     app.run(port='5002')
