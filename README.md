# pc-rest-api - a simple CRUD REST API
<img src="https://user-images.githubusercontent.com/27636896/123033609-03586280-d423-11eb-8071-9a7fda36fd47.png" width=50% height=50%>

**pc-rest-api**  is a basic backend CRUD API built in Python, that allows you to find, insert, update, and delete an individual's computer hardware specs.

## Technologies used
  
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) Web Application Framework
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) Cloud DataBase

## Installation <img src="https://user-images.githubusercontent.com/27636896/123034345-4961f600-d424-11eb-980b-fa3dd2f5188b.png" width=3% height=3%>

First you will have to create a MongoDB Atlas account if you do not have one already. Then you will have to set up your database along with one table/collection.
[Check out the getting started here](https://docs.atlas.mongodb.com/getting-started/)

## activate virtual environment from root folder

```
source bin/activate
```

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



## copy past http://127.0.0.1:5000/ in your browser



<img src="https://user-images.githubusercontent.com/27636896/123035083-b1650c00-d425-11eb-8484-c7d3ebef976c.png" width=3% height=3%> **INSERT** 
```
http://127.0.0.1:5000/insert-one/owner/cpu/ram/gpu/storage/
```

<img src="https://user-images.githubusercontent.com/27636896/123035220-f2f5b700-d425-11eb-965a-694c313fd5ce.png" width=3% height=3%> **FIND ALL** 
```
http://127.0.0.1:5000/find/
```

<img src="https://user-images.githubusercontent.com/27636896/123035220-f2f5b700-d425-11eb-965a-694c313fd5ce.png" width=3% height=3%> **FIND ONE** 
```
http://127.0.0.1:5000/find-one/owner/
```

<img src="https://user-images.githubusercontent.com/27636896/123035318-1d477480-d426-11eb-8ed0-c02c9423e416.png" width=3% height=3%> **UPDATE ONE** 
```
http://127.0.0.1:5000/update-one/owner/key/value/
```

<img src="https://user-images.githubusercontent.com/27636896/123035255-04d75a00-d426-11eb-9ab1-32446a7e2b93.jpg" width=3% height=3%> **DELETE ONE** 
```
http://127.0.0.1:5000/delete-one/owner/
```

## object structure
<img src="https://user-images.githubusercontent.com/27636896/123040935-8b446980-d42f-11eb-9803-5b2da8b10c8f.png" width=50% height=50%>


## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
