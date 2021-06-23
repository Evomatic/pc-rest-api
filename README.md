# pc-rest-api - a simple CRUD REST API

**pc-rest-api**  is a basic backend CRUD API built in Python, that allows you to find, insert, update, and delete an individual's computer hardware specs.

## Technologies used
  
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) Web Application Framework
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) Cloud DataBase

## Installation

First you will have to create a MongoDB Atlas account if you do not have one already. Then you will have to set up your database along with one table/collection.
[Check out the getting started here](https://docs.atlas.mongodb.com/getting-started/)

## install dependencies

```
pip install -r requirements.txt 
```

## create a .env then add the following

```
CLIENT_ID=MongoDB Atlas connection key
```
## run the flask server in terminal

```
python3 app.py
```

## object structure

```
{
Owner: "Evan"
CPU: "intel core i9 9900k 4.0ghz"
ram: "32Gb 3200mhz"
GPU: "RTX 2080TI"
storage: "2Tb M.2"
}
```

**copy past http://127.0.0.1:5000/ in your browser

**INSERT
```
http://127.0.0.1:5000/insert-one/owner/cpu/ram/gpu/<storage>/
```

**FIND ALL
```
http://127.0.0.1:5000/find/
```

**UPDATE ONE
```
http://127.0.0.1:5000/update-one/owner/key/value/
```

**DELETE ONE
```
http://127.0.0.1:5000/delete-one/owner/
```
