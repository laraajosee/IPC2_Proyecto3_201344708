from flask import Flask, Response, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "*"}})


@app.route('/events/', methods=['POST'])
def post_events():
    data = open('data.xml', 'w+')
    data.write(request.data.decode('utf-8'))
    data.close()

    return Response(response=request.data.decode('utf-8'),
                    mimetype='text/plain',
                    content_type='text/plain')


@app.route('/stats/', methods=['GET'])
def get_events():
    data = open('data.xml', 'r+')
    return Response(response=data.read(),
                    mimetype='text/plain',
                    content_type='text/plain')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
