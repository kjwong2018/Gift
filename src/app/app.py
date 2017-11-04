from flask import Flask,request,jsonify,render_template,json
from sqlalchemy import create_engine

# host = "127.0.0.1"#host address
# port = 8080

app = Flask(__name__)

# class data
# def init_engine():
#     engine = create_engine('gift:gift12345@mysql+pymysql://giftdatabase.c03akep9s2fc.us-west-2.rds.amazonaws.com:3306/giftdatabase')

def get_data(filter):
    engine = create_engine('mysql+pymysql://gift:gift12345@giftdatabase.c03akep9s2fc.us-west-2.rds.amazonaws.com:3306/gift_db')
    connection = engine.connect()
    result = connection.execute('select * from tagType;')
    result_dict = result.__dict__
    # print(result_dict)
    connection.close()

@app.route('/',methods=['GET'])
@app.route('/index.html',methods=['GET'])
def index():
    get_data("hi")
    return render_template('index.html')

@app.route('/pick_gift.html',methods=['GET','POST'])
def pickGift():
    return render_template('pick_gift.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    # init_engine()


# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
