from flask import Flask,request,jsonify,render_template,json
from sqlalchemy import create_engine

# host = "127.0.0.1"#host address
# port = 8080

app = Flask(__name__)

def get_complete(msg):
    # myDict = {"init":{}}
    engine = create_engine('mysql+pymysql://gift:gift12345@giftdatabase.c03akep9s2fc.us-west-2.rds.amazonaws.com:3306/gift_db')
    connection = engine.connect()
    # result = connection.execute("SELECT tagName	FROM tagType AS t1 INNER JOIN tagTypeMap AS map	ON t1.tagType='Occasion' AND t1.typeID=map.tagTypeID INNER JOIN tag ON tag.tagID=map.tagID;")
    # i = 0
    # while len(msg) !=0:
    #     print("CREATE TEMPORARY TABLE temp"+str(i)+" AS (SELECT p.* FROM tag AS t INNER JOIN productTagMap map ON t.tagName="+"'"+msg.pop(0)+"'"+" AND map.tagID=t.tagID INNER JOIN product p ON p.productID=map.productID);")
    #     result = connection.execute("CREATE TEMPORARY TABLE temp"+str(i)+" AS (SELECT p.* FROM tag AS t INNER JOIN productTagMap map ON t.tagName="+"'"+msg.pop(0)+"'"+" AND map.tagID=t.tagID INNER JOIN product p ON p.productID=map.productID);")
    #     i += 1
    # result = connection.execute("SELECT * FROM temp6;")
    # for x in result:
    #     print(x)
    connection.close()
    return "hi"
def get_question():
    engine = create_engine('mysql+pymysql://gift:gift12345@giftdatabase.c03akep9s2fc.us-west-2.rds.amazonaws.com:3306/gift_questionair')
    connection = engine.connect()
    result = connection.execute('select * from questionair;')
    x = 1
    msg = {"question":{}}
    for i in result:
        word_list = i[2].split(",")
        msg["question"][x] = {"Question":i[1],"Answer":{}}
        y = 0
        while len(word_list) != 0:
            word = word_list.pop(0)
            msg["question"][x]["Answer"][y]= word
            y = y+1
        x = x+1
    connection.close()
    return msg


@app.route('/',methods=['GET'])
@app.route('/index.html',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/pick_gift.html',methods=['GET','POST'])
def pickGift():
    return render_template('pick_gift.html')

@app.route('/request',methods=['POST'])
def message():
    rcvd = request.data.decode('ascii')
    print(rcvd)
    # print("fk")
    # if(rcvd == "complete"):
    #     msg = get_complete()
    #     print(msg)
    #     return jsonify(msg)
    # elif(rcvd == "question"):
    msg = get_question()
    print(msg)
    return jsonify(msg)

@app.route('/complete',methods=['POST'])
def complete():
    rcvd = request.data.decode('ascii')
    print(rcvd)
    listAns = rcvd.split(",")
    listAns.pop(0)
    print(listAns)
    msg = get_complete(listAns)
    # print(msg)
    return render_template('index.html')

if __name__ == "__main__":
    threaded=True
    app.run(host='0.0.0.0')
