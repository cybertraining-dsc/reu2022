# Requests with Python

The `requests` library is a python library that allows the user to interact with the internet via HTTP very easily. Typically, users specify the type of request they are making via their programming, but with the `requests` library, it is much easier to program for user enhancement. 

## Installing and Importing

The `requests` library can be easily installed from the command line and imported at the top of any python file. 

The following script can be used to install `requests`:

```bash
$ python -m pip install requests
```

Once this has been done, it is simple to import the library into a python file. Simply execute the following:

```python
import requests
```

## Using Requests

The `requests` library has many functions that allow it to be utilized in the way it is. Typical functions are `requests.put()`, `requests.head()`, `requests.delete()`, `requests.get()`, and `requests.options()`. What the `requests` library does is it properly encodes everything that is programmed by the user. 

A basic example of how requests could be utilized within a program:

```python
import requests
r = requests.get("https://api.github.com/events")
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.head('https://httpbin.org/get')
```

This code can be accessed from [GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/requests/test-requests.md)

For requests, an `r` value of 200 means that the method was a success whereas a 100 means not a success. 

In addition to these functions, the `requests` library has a plethora of other functionalities. It can send more data, convert to `json` files, execute `patches`, etc. The documentation for the `requests` library can be found [here](https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls). This link is also where the examples are drawn from.


## Links

* [Requests Documentation](https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls)