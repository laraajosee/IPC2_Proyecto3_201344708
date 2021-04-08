from flask import Flask, Response, request
from flask_cors import CORS
from flask_cors.core import parse_resources

app = Flask(__name__)
#cors = CORS(app, resources {r"/*": {"origin": "*"}})

@app.route('/')
def Index():
    return 'Hello  World'

@app.route('/events', methods=['POST'])
def post_events():
    data_xml = open('data.xml', 'w+' )
    data_xml.write(request.data.decode('utf-8'))
    data_xml.close
    return Response(response= request.data.decode('utf-8'),
                    mimetype='text/plain',
                    content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
