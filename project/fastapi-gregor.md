# FastAPI 

---

![](images/learning.png) **Learning Objectives**

* Leran how to use fastAPI

---

FastAPI is a Python framework that allows developers set up a REST service and
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
```

### Path

One of the mechanisms FastAPI provides it to easily specify the URL that is needed to 
trigger the functionality of the defined function after its definotion.

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

## Arguments

TODO: use computers and temperature as model (see shelve)

<https://fastapi.tiangolo.com/tutorial/path-params/>

## Query

TODO: use computers and temperature as model

<https://fastapi.tiangolo.com/tutorial/query-params/>

## Integration with pedantic

TODO: user computer as model

## Links

* <https://fastapi.tiangolo.com/tutorial/first-steps/>
