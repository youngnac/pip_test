"""
test requests
"""
import requests

r = requests.get('http://www.google.com')
print(r.text)