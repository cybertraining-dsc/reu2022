# FastAPI 

---

![](images/learning.png) **Learning Objectives**

* Learn how to use fastAPI

---

FastAPI is a Python framework that allows developers to use the
RestAPI interface to call functions that implement
applications. RestAPI is used to call the common building block of an
application.


## FastAPI Install

There are two ways to install the FastAPI: either completely with the
`uvicorn` or partially with both the `FastAPI` and the `uvicorn`.


##### Install 1

  This command install both the FastAPI and uvicorn together withe one command.
```bash
$ pip install "fastapi[all]"
```
##### Install 2
  This commands install the FastAPI and the uvicorn with different commands.

```bash
$ pip install "fastapi"
$ pip install "uvicorn[standard]"
```

## FastAPI Example

The simplest FastAPI file could look like this:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Copy it in a file called `main.py`.

Start the live server as follows:

```bash
$ uvicorn main:app --reload 

INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO: Started reloader process [28720]
INFO: Started server process [28722]
INFO: Waiting for application startup.
INFO: Application startup complete.

```

There's a line that output something like:

```
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

This line displays the URL where your app is served on your local machine.

Navigate to http://127.0.0.1:8000 in your browser.

The JSON response will appear as:

```
{"message": "Hello World"}
```

* Go to http://127.0.0.1:8000/docs.

* OpenAPI :

  Using the `OpenAPI` standard for defining APIs, FastAPI creates a `schema` with all of your APIs.

  You can see it directly at: http://127.0.0.1:8000/openapi.json.

It will display a JSON that starts with:

```json
{
    "openapi": "3.0.2",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {


```


### FastAPI instance

If you create your app like:

```python
from fastapi import FastAPI

my_awesome_api = FastAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}
```

And copy it in a file `main.py` then you would call `uvicorn` like:

```bash
$ uvicorn main:my_awesome_api --reload

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

To stop the server you will stop the server on the windows in which you enter doc url

```bash
$ cms cc stop
```
References: <https://fastapi.tiangolo.com/tutorial/first-steps/>
