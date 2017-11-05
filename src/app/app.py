from flask import Flask,request,jsonify,render_template,json
from sqlalchemy import create_engine

# host = "127.0.0.1"#host address
# port = 8080

app = Flask(__name__)

# class data
# def init_engine():
#     engine = create_engine('gift:gift12345@mysql+pymysql://giftdatabase.c03akep9s2fc.us-west-2.rds.amazonaws.com:3306/giftdatabase')

def get_init():
    myDict = {"init":{}}
    engine = create_engine('mysql+pymysql://gift:gift12345@giftdatabase.c03akep9s2fc.us-west-2.rds.amazonaws.com:3306/gift_db')
    connection = engine.connect()
    result = connection.execute('select * from tagType;')
    x = 0
    for i in result:
        if(i[0] == 1):
            myDict["init"][i[1]]={}
            t = i[1]
        else:
            myDict["init"][t][x]=i[1]
            x = x+1
    print(myDict)
    connection.close()
    return myDict

def get_question():
    myDict = {"question":{}}
    engine = create_engine('mysql+pymysql://gift:gift12345@giftdatabase.c03akep9s2fc.us-west-2.rds.amazonaws.com:3306/gift_questionair')
    connection = engine.connect()
    result = connection.execute('select * from questionair;')
    for i in result:
        print(i)


@app.route('/',methods=['GET'])
@app.route('/index.html',methods=['GET'])
def index():
    get_question()
    return render_template('index.html')

@app.route('/pick_gift.html',methods=['GET','POST'])
def pickGift():
    return render_template('pick_gift.html')
@app.route('/init',methods=['POST'])
def message():
    rcvd = request.data
    print(rcvd)
    # if(rcvd == "init"):
    msg = get_init()
    print(msg)
    return jsonify(msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    # init_engine()


# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
# @app.route('/',methods=['GET'])
