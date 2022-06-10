# FastAPI 

---

![](images/learning.png) **Learning Objectives**

* Leran how to use fastAPI

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

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Copy it in a file called `main.py`.

Start the live server as follows:

``` bash
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

```
from fastapi import FastAPI

my_awesome_api = FastAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}
```
And copy it in a file `main.py` then you would call `uvicorn` like:

``` bash
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

```
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
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

You can return a dict, a list, or singular values such as str, int,
and so on.


References: <https://fastapi.tiangolo.com/tutorial/first-steps/>
