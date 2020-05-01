#!/usr/bin/env python3
   
from flask import Flask, request, render_template
import pymongo

#Mongo metadata
MONGO_URI = 'mongodb://root:example@mongo'
myclient = pymongo.MongoClient(MONGO_URI)
mydb = myclient["mydatabase"]
mycol = mydb["phrases"]

app = Flask(__name__)
 
@app.route("/",methods = ["GET"])
def hello():
    return render_template('index.html')


@app.route("/", methods = ["POST"])
def save_2_mongo():
       text = request.form["text"]
       search = request.form["search"]
       if text:
           mydict = { "phrase": text }
           mycol.insert_one(mydict)
           return 'Inserted phrase %s to mogoDB !!' % text
       if search:
           myquery = { "phrase": {'$regex': search }} 
           mydoc = mycol.find(myquery)

           mydict = [x for x in mydoc]
           search_result = {}
           count = 0
           for x in mydict:
               count+=1
               search_result.update({count: x[key] for key in x.keys() & {'phrase'}})

           #return 'search res %s !!' % search_result
           return render_template('search_results.html', search=search ,search_result=search_result)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
