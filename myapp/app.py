#!/usr/bin/env python3
   
from flask import Flask, request, url_for, render_template
import pymongo

#Mongo metadata
MONGO_URI = 'mongodb://root:example@localhost'
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
       mydict = { "phrase": text }
       mycol.insert_one(mydict)
       return 'Inserted phrase %s to mogoDB search is %s !!' % text,search



#myquery = { "address": "Highway 37" }

#mydoc = mycol.find(myquery)
#for x in mydoc:
#   print(x)

###handler = http.server.SimpleHTTPRequestHandler

###with socketserver.TCPServer(("",1234), handler) as httpd:
###    httpd.serve_forever()
