import requests

"""
    This is a program that provides an example of how to utilize the python
    requests library. 
"""

r = requests.get("https://api.github.com/events")
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.head('https://httpbin.org/get')


print(r)
print(r.url)
print(r.text)
print(r.content)

