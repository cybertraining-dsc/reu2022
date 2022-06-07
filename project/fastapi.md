# FastAPI 
FastAPI ia a framework in python that allows developers to use restinterface to call function that implement application, it uses RestAPI to call the common building block of an application.

## FastAPI Install
To install the FastAPI they are two steps one might need to install it fully with the `uvicorn` or install both the `FastAPI ` and the `uvicorn` by part

#### Step 1

`$ pip install "fastapi[all]" `

#### Step 2

`$ pip install fastapi:`

`$ pip install "uvicorn[standard]" `

## FastAPI UserGuide


### Step 1: import FastAPI

The simplest FastAPI file could look like this:
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```
Copy that to a file `main.py`

Run the live server:
```
$ uvicorn main:app --reload 

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

```
In the output, there's a line with something like:

` INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit) `

That line shows the URL where your app is being served, in your local machine.

Check it

Open your browser at http://127.0.0.1:8000

You will see the JSON response as:

`{"message": "Hello World"}`

Interactive API docs

* go to http://127.0.0.1:8000/docs.

* Then go to http://127.0.0.1:8000/redoc.

* OpenAPI:

  FastAPI generates a `schema` with all your API using the `OpenAPI` standard for defining APIs.


* OpenAPI and JSON Schema

  OpenAPI defines an API schema for your API. And that schema includes definitions (or "schemas") of the data sent and received by your API using JSON Schema, the standard for JSON data schemas.

You can see it directly at: http://127.0.0.1:8000/openapi.json.

It will show a JSON starting with something like:
```


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

### Step 2: create a FastAPI "instance"
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Here the `app` variable will be an "instance" of the class `FastAPI`.

This will be the main point of interaction to create all your API.

This` app` is the same one referred by `uvicorn` in the command:

```
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

If you create your app like:
```

from fastapi import FastAPI

my_awesome_api = FastAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}
```
And put it in a file `main.py` then you would call `uvicorn` like:

```
$ uvicorn main:my_awesome_api --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### Step 3: create a path operation

Path here refers to the last part of the URL starting from the first .

So, in a URL like:
`https://example.com/items/foo`
...the path would be:


`/items/foo`

" While building an API, the "path" is the main way to separate "concerns" and "resources"."

Operation
"Operation" here refers to one of the HTTP "methods".

When building APIs, you normally use these specific HTTP methods to perform a specific action.
Normally you use:
* POST: to create data.
* GET: to read data.
* PUT: to update data.
* DELETE: to delete data.

In the HTTP protocol, you can communicate to each path using one (or more) of these "methods".

So, in OpenAPI, each of the HTTP methods is called an "operation".

#### Define a path operation decorator¶
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```
The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to:

the path /
using a get operation
@decorator Info

That @something syntax in Python is called a "decorator".

You put it on top of a function. Like a pretty decorative hat (I guess that's where the term came from).

A "decorator" takes the function below and does something with it.

In our case, this decorator tells FastAPI that the function below corresponds to the path / with an operation get.

It is the "path operation decorator".

You can also use the other operations:

@app.post()
@app.put()
@app.delete()
And the more exotic ones:

@app.options()
@app.head()
@app.patch()
@app.trace()



### Step 4: define the path operation function

This is our "path operation function":

path: is /.
operation: is get.
function: is the function below the "decorator" (below @app.get("/")).
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```
This is a Python function.

It will be called by FastAPI whenever it receives a request to the URL "/" using a GET operation.

In this case, it is an async function.

You could also define it as a normal function instead of async def:
```
from fastapi import FastAPI

app = FastAPI()

Reference: <https://fastapi.tiangolo.com/tutorial/first-steps/>
@app.get("/")
def root():
    return {"message": "Hello World"}
```


### Step 5: return the content
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```
You can return a dict, list, singular values as str, int, etc.

You can also return Pydantic models .

There are many other objects and models that will be automatically converted to JSON (including ORMs, etc). Try using your favorite ones, it's highly probable that they are already supported.


