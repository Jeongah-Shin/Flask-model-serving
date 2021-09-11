import tensorflow as tf
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/detect_face', methods=['POST'])
def detect_face():
    if request.method == 'POST':
        # Check whether the POST request contains input_image part
        # POST API 입력으로 input image 주어졌는지 확인한다.
        if ('input_image' in request.files):
            input_image = request.files.get('input_image')
            result = None
            # result = detect()
            # result -> response mapping 수행 필요
            response = {
                "idx" : None,
                "bounding_box" : [0,0,0,0]
            }
            return json.dumps(response)

app.run(host='0.0.0.0', port='8080', debug=True)

def load_model(PB_PATH):
    graph = tf.Graph()
    with graph.as_default():
        detection_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PB_PATH, 'rb') as fid:
            serialized_graph = fid.read()
            detection_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(detection_graph_def, name='')
            with graph.as_default():
                sess = tf.Session(graph=graph)
                return sess, graph
