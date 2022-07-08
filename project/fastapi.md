# FastAPI 


---

![](images/learning.png) **Learning Objectives**

* Learn how to use FastAPI

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

## FastAPI Quickstart

One of the simplest FastAPI file looks like this, which we assume is placed 
in a file called `main.py`:

```python
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
{"processor": "5950X"}
```

One of the embedded features of FastAPI is its build in documentation 
framework based on OpenAPI schema, but it also has alternative formats such as
json or redoc. You can look at it while going with your browser to the URL:

* OpenAPI: <http://127.0.0.1:8000/docs>.
* OpenAPI json: <http://127.0.0.1:8000/openapi.json>
* Redoc: <http://127.0.0.1:8000/redoc>

In case you like to have a different name than `app` you can just use a different 
variable

```python
from fastapi import FastAPI

my_awesome_app = FastAPI()

@my_awesome_app.get("/")
async def root():
    return {"processor": "5950X"}
```
And copy it in a file `main.py` then you would call `uvicorn` like:

``` bash
$ uvicorn main:my_awesome_app --reload
```

## Path

One of the mechanisms FastAPI provides it to easily specify the URL that is needed to 
trigger the functionality of the defined function after its definition.

We have seen such an example in `@app.get("/")` which activates the `root` function when the
URL of the server is specified followed by "/"

You can add other path's and functions. Let us assume you add to our initial program the function 

```python
@app.get("/temperature")
async def temperature():
    return {"temperature": 0}
```

The if you use the URL <http://127.0.0.1:8000/temperature>, we will see 

```
{"temperature": 0}
```

### Path Arguments

Not only can you call functions through the path, you can also pass arguments through the path.
The arguments can be specified by type in the formal parameter. In this case, we specify
that it should be an int. This helps FastAPI validate data, which is done through the package
Pydantic.

```python
@app.get("/temperature/{temp_id}")
async def temperature(temp_id: int):
    return {"temperature": temp_id}
```

### Query and Search Parameters

When you declare other function parameters that are not part of the path parameters, 
they are automatically interpreted as URL "query" parameters, as seen in the function
`get_job()`.

The query is the set of key-value pairs that go after the `?` in a URL, 
separated by & characters.
For example, in the URL:

```
http://127.0.0.1:8000/jobs/?skip=0&limit=10
```

In this case the query parameters are:

* skip: with a value of 0
* limit: with a value of 10

In addition, this can be used to search in the FastAPI, as seen in `search_job()`.
You can use the URL to search the `jobs` variables like this:

```
http://127.0.0.1:8000/job/?name=Job1
```

Output:

```
"Job1"
```

```python
from fastapi import FastAPI

app = FastAPI()
jobs = [{"name": "Job1", "temperature": 0}, 
        {"name": "Job2", "temperature": 30}, 
        {"name": "Job3", "temperature": 10}]

@app.get("/jobs/")
async def get_job(skip: int = 0, limit: int = 10):
    return jobs[skip : skip + limit]

@app.get("/job/")
async def search_job(name:str):
    result = None
    for item in jobs:
        if item['name'] == name:
            result = name
    return result
```

## Running Through Git bash

```python
import requests

result = requests.get('http://127.0.0.1:8000/job/?name=Job1')

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

where r.py is the file name, yielding the output:

```
"Job1"
200
application/json
utf-8
"Job1"
Job1
```

## Integration with pedantic

TODO: user computer as model


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

## Running through Docker

In most cases, it is preferable to use a container to run the REST service, since there
are many dependencies and packages. Here we will show you how to create and export an
image for your FastAPI service to Docker.

To start, create a project directory. We will call it `project`. In this folder create
a subdirectory called `app`. This can be done through Git Bash.

```bash
$ mkdir project
$ cd project
$ mkdir app
```

In the `project` directory, create two files `requirements.txt` and `Dockerfile`.
`requirements.txt` will have the necessary package dependencies. Depending on what
packages are used, this will vary. This is an example of what it would look like.

```
fastapi>=0.68.0,<0.69.0
pydantic>=1.8.0,<2.0.0
uvicorn>=0.15.0,<0.16.0
```

In `Dockerfile`, copy this code:

```dockerfile
# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

In your `app` folder, add your FastAPI code. In this tutorial we have used the name
`main.py`. In addition, create a python file `__init__.py`. This can be left empty.

To build the Docker image, go back to the project directory and type the following
code:

```bash
$ docker build -t myimage .
```

To create a running instance of this image, execute the following code:

```bash
$ docker run -d --name mycontainer -p 80:80 myimage
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
* <https://fastapi.tiangolo.com/tutorial/path-params/>
* <https://fastapi.tiangolo.com/deployment/docker/>
* <https://fastapi.tiangolo.com/tutorial/testing/#using-testclient>
* <https://fastapi.tiangolo.com/advanced/async-tests/>
* cloudmesh cc TODO
