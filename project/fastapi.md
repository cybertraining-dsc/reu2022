# FastAPI 

---

![](images/learning.png) **Learning Objectives**

* Learn how to use fastAPI

---
stAPI is a Python framework that allows developers set up a REST service and 
define its functionality with an easy to use API.


## FastAPI Install

As FatsAPI will need a web server, we use for development purposses `uvicron`. 
In a production environment other more mature Web services are recommended.
To install FastAPI and uvicorn simply use the command:

```bash
$ pip install "fastapi[all]"
```


## FastAPI Quickstart

One of the simplest FastAPI file looks like this, which we assume is placed in a file called `main.py`:

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Start the live FastAPI `app` in the `uvicorn` server use the command:

``` bash
$ uvicorn main:app --reload 
```

This will yield the output

```
1 INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
2 INFO: Started reloader process [28720]
3 INFO: Started server process [28722]
4 INFO: Waiting for application startup.
4 INFO: Application startup complete.

```

The first line includes information about which URL is used to contact it to obtain a response. An easy way to view it is to enter <http://127.0.0.1:8000> in your browser.
The JSON response will appear as:

```
{"message": "Hello World"}
```

Oneo of the embedded features of FastAPI is its build in documentation framework based on OpenAPI schema. You can look at it while going with your browser to the URL 

* <http://127.0.0.1:8000/docs>. 

* Other formats are also available, for example json:

* <http://127.0.0.1:8000/openapi.json>

In case you like to have a different name than `app` you can just use a different 
variable

```
from fastapi import FastAPI

my_awesome_app = FastAPI()

@my_awesome_app.get("/")
async def root():
    return {"message": "Hello World"}
```
And copy it in a file `main.py` then you would call `uvicorn` like:

``` bash
$ uvicorn main:my_awesome_app --reload

INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### Path operation

Path refers to the last part of the URL beginning with the first.  So,
in a URL like: `https://example.com/purple/flc` ...the path would be:
`/purple/flc`

"When developing an API, the `path` is the primary means of separating
"concerns" and "resources."


##### Define a path operation decorator

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

The `@app.get("/")` tells FastAPI that the function right below is in
charge of handling requests that go to:

* the path /
* using a `get` operation

#####  Define the path operation function

Our `path operation function` is as follows:

* path: is /.
* operation: is `get`.
* function: the function that comes after the "decorator" (below @app.get("/")): `async def root()` .


### Return the content

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

You can return a dict, a list, or singular values such as str, int,
and so on.

## Query Parameters

When you declare other function parameters that are not part of the path parameters, 
they are automatically interpreted as "query" parameters.

```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```

The query is the set of key-value pairs that go after the `?` in a URL, separated by & characters.
For example, in the URL:

```
http://127.0.0.1:8000/items/?skip=0&limit=10
```

the query parameters are:

* skip: with a value of 0
* limit: with a value of 10

### Searching in the fastapi

```python
from fastapi import FastAPI

app = FastAPI()

items = [{"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return items[skip : skip + limit]

@app.get("/search/")
async def search_item(name:str):
    result = None
    for item in items:
        if item['name'] == name:
            result = name
    return result
```
For example, in the URL
```
http://127.0.0.1:8000/search/?name=Foo')
```
Output
```
"Foo"
```

### Running Through Git bash

```python
import requests

result = requests.get('http://127.0.0.1:8000/search/?name=Foo')

print(result.text)

print(result.status_code)
print(result.headers['content-type'])
print(result.encoding)
print(result.text)
print(result.json())
```
Run python code on Git bash
```bash
$ python r.py
```
where r.py is the file name

output
```
"Foo"
200
application/json
utf-8
"Foo"
Foo
```

## Running the uvicorn server Through Git Bash

```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

Starting up the uvicorn server

```bash
$ cms cc start
```

To Enter the docs url `http://127.0.0.1:8000/docs` on another window

```bash
$ cms cc doc
```

To stop the server, you will stop it in the window server in which you enter doc url

```bash
$ cms cc stop
```
References: <https://fastapi.tiangolo.com/tutorial/first-steps/>
