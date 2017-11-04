from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
@app.route('/index.html',methods=['GET'])
def index():
    return return_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')


# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
