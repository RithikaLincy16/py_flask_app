from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/hello', methods=['GET','POST'])
def hello():
    if request.method=="GET":
        return jsonify({"response": "GET request called!"})
    elif request.method=="POST":
        req_Json=request.json
        name=req_Json['name']
        return jsonify({"response": "Hello "+name})


if __name__== '__main__':
    app.run(debug=True, port=5000)