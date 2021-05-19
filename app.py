from dotenv import load_dotenv
from flask import Flask, request, jsonify, json
from flask_cors import CORS
import pymongo
import dns
import os


load_dotenv()

# connect to mongodb atlas
connection_url = os.getenv("CLIENT_ID")
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)


Database = client.get_database('computers')
computerSpecs = Database.computerSpecs




# GET all data in the collection 
@app.route('/find/', methods=['GET'])
def findAll():
    query = computerSpecs.find()
    output = {}
    i = 0
    for x in query:
        output[i] = x
        output[i].pop('_id')
        i+= 1
    # print(query)
    return jsonify(output)



# INSERT new data
@app.route('/insert-one/<owner>/<cpu>/<ram>/<gpu>/<storage>/', methods=['GET'])
def insertOne(owner, cpu, ram, gpu, storage):
    queryObject = {
        'Owner': owner,
        'CPU': cpu,
        'ram': ram,
        'GPU': gpu,
        'storage': storage
    }
    computerSpecs.insert_one(queryObject)
    return findAll()



# DELETE selected data
@app.route('/delete-one/<owner>/', methods=['GET'])
def deleteOne(owner):
    query = computerSpecs.find()

    for x in query:
        if x['owner'] == owner:
            computerSpecs.delete_one(x)
    return 'Query deleted!'



# UPDATE selected data
@app.route('/update-one/<owner>/<key>/<value>/', methods=['GET'])
def updateOne(owner, key, value):
    query = computerSpecs.find()

    for x in query:
        if x['Owner'] == owner:
            filter = { key: x[key]}
            newValue = { "$set": { key: value } }
            computerSpecs.update_one(filter, newValue)
    return 'Query updated!'        
            # computerSpecs.update_one()





if __name__ == '__main__':
    app.run(debug=True)









    