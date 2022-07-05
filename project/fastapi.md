# FastAPI 

![](images/learning.png) **Learning Objectives**

* Learn how to use fastAPI

---
FastAPI is a Python framework that allows developers set up a REST service and 
define its functionality with an easy-to-use API.


## FastAPI Install

As FastAPI will need a web server, we will use `uvicron` for development purposes. 
In a production environment other, more mature Web services are recommended.
To install FastAPI and uvicorn simply use the command:

```bash
$ pip install "fastapi[all]"
```

TODO: THERE ARE TOO MANY DIFFERENT EXAMPLES, PLEASE CREATE ONE THAT 
BUILDS ON TOP OF EACH OTHER, USE  COMPUTERS WITH TEMPERATURES

## FastAPI Quickstart

One of the simplest FastAPI file looks like this, which we assume is placed 
in a file called `main.py`:

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"processor": "5950X"}
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

The first line includes information about which URL is used to contact it to 
obtain a response. An easy way to view it is to enter <http://127.0.0.1:8000> 
in your browser.
The JSON response will appear as:

```
{"message": "Hello World"}
```

One of the embedded features of FastAPI is its build in documentation 
framework based on OpenAPI schema but also alternative formats such as redoc. 
You can look at it while going with your browser to the URL 

* OpenAPI: <http://127.0.0.1:8000/docs>.
* OpenAPI json: <http://127.0.0.1:8000/openapi.json>
* Redoc: <http://127.0.0.1:8000/redoc>


### Path

One of the mechanisms FastAPI provides it to easily specify the URL that is needed to 
trigger the functionality of the defined function after its definition.

We have seen such an example in `@app.get("/")` which activates the `root` function when the
URL of the server is specified followed by "/"

You can add other path's and functions. Let us assume you add to our initial program the function 

```
@app.get("/temperature")
async def temperature():
    return {"temperature": 0}
```

The if you use the URL <http://127.0.0.1:8000/temperature>, we will see 

```
{"temperature": 0}
```


## Query Parameters

When you declare other function parameters that are not part of the path parameters, 
they are automatically interpreted as URL "query" parameters.

```python
from fastapi import FastAPI

app = FastAPI()
jobs = [{"name": "Foo"}, 
        {"name": "Bar"}, 
        {"name": "Baz"}]

@app.get("/jobs/")
async def get_job(skip: int = 0, limit: int = 10):
    return jobs[skip : skip + limit]
```

The query is the set of key-value pairs that go after the `?` in a URL, 
separated by & characters.
For example, in the URL:

```
http://127.0.0.1:8000/jobs/?skip=0&limit=10
```

In this case the query parameters are:

* skip: with a value of 0
* limit: with a value of 10

### Searching in the fastapi

```python
from fastapi import FastAPI

app = FastAPI()
jobs = [{"name": "Foo"}, 
        {"name": "Bar"}, 
        {"name": "Baz"}]

@app.get("/job/")
async def search_job(name:str):
    result = None
    for item in jobs:
        if item['name'] == name:
            result = name
    return result
```

For example, in the URL

```
http://127.0.0.1:8000/job/?name=Foo')
```

Output

```
"Foo"
```

### Running Through Git bash

```python
import requests

result = requests.get('http://127.0.0.1:8000/job/?name=Foo')

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

where r.py is the file name, yeilding in the output

```
"Foo"
200
application/json
utf-8
"Foo"
Foo
```

## Running the cc FastAPI service

The cloudmesh cc FastAPI service can be started with 

```bash
$ cms cc start
```

To see the documentation you do not have to type in the URL in the browser, 
but instead you can use the command 

```bash
$ cms cc doc
```

which will open the url `http://127.0.0.1:8000/docs` in the browser.

To stop the server, use the command

```bash
$ cms cc stop
```

## Testing

In order to test the FastAPI code, we want to create a new test file. In this file, we
import `TestClient from fastapi.testclient`. TestClient creates a test object that
follows pytest conventions. In addition, you must import the `app` FastAPI object from
the main module.

You can then create the test object by passing this FastAPI object into the TestClient.
You use assert statements to test for validity.

```python
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_temperature():
    response = client.get("/temperature")
    assert response.status_code == 200
    assert response.json() == {"temperature": 0}
```

You can create several test functions and run them with `pytest`.
Lastly, there are other parameters for `client.get()` that may be further explored
in the [requests documentation](<https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls>).

### Asynchronous Testing

To test asynchronous functions, for example async queries, we can no longer use TestClient
due to Pytest's inherent sync nature. Instead, we use a very similar client called
`HTTPX` that can make both synchronous and asynchronous requests.

In addition, we must mark these async test functions with the `pytest.mark.aniyo` flag.

```python
import pytest
from httpx import AsyncClient

from .main import app


@pytest.mark.anyio
async def test_temperature():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/temperature")
    assert response.status_code == 200
    assert response.json() == {"temperature": 0}
```

The `await` functions sends the asynchronous request.

This can once again be run with pytest, and additional async or sync test functions
can be added as well.

## Links

* <https://fastapi.tiangolo.com/tutorial/first-steps/>
* <https://fastapi.tiangolo.com/tutorial/testing/#using-testclient>
* <https://fastapi.tiangolo.com/advanced/async-tests/>
* cloudmesh cc TODO
