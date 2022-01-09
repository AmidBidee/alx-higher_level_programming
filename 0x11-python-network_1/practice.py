"""
Contains practice code for urllib
"""

# simplest way to use urllib
import urllib.request as request


with request.urlopen('http://python.org') as response:
    html = response.read()

# to retrieve and store and temporary location
# you can do so via shutil.copyfileobj() and tempfile.NamedTemporaryFile() functions

import shutil
import tempfile


with request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass


# Calling urlopen with this Request object returns a response object for the URL requested.
# This response is a file-like object, which means you can for example call .read() on the response:
req = request.Request('http://www.voidspace.org.uk')
with request.urlopen(req) as response:
    page = response.read()

# Data
# you can use a POST to transmit arbitrary data to your own application. 
# In the common case of HTML forms, the data needs to be encoded in a standard way, 
# and then passed to the Request object as the data argument. 
# The encoding is done using a function from the urllib.parse library.
import urllib.parse as parse

url = 'http://wwww.someserver.com/cgi-bin/register.cgi'
values = {
    'name': 'Michael Ford',
    'location': 'Northampton',
    'language': 'Python'
}
data = parse.urlencode(values) # convert data into uri compatable
data = data.encode('ascii') # data should be bytes
req = request.Request(url, data)

with request.urlopen(req) as response:
    page = response.read()

