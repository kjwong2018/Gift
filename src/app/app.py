from flask import Flask,request,jsonify,render_template
# from flask_sqlalchemy import  SQLAlchemy
# host = "127.0.0.1"#host address
# port = 8080

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'gift:gift12345@mysql+pymysql://giftdatabase.c03akep9s2fc.us-west-2.rds.amazonaws.com:3306/giftdatabase'
# db = SQLAlchemy(app)

# class data

@app.route('/',methods=['GET'])
@app.route('/index.html',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/pick_gift.html',methods=['GET','POST'])
def hi():
    return render_template('pick_gift.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')


# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
