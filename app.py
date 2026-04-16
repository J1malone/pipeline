from flask import Flsk, Jsonify, app 
import datetime

app = Flask(__name__)   

@app.route('/')
def home():
    return jsonify({"message": "Devfin ops "})
"time": str(datetime.datetime.now())})

@app.route('/health')
def health():
    return jsonify({"status" : "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


    