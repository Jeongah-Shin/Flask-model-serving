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