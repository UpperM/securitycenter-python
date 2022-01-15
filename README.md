
# Genetec SecurityCenter Python wrapper

**Still in developpement !**
## Getting Started

I have a problem with ``requests.Session()`` who doesn't use correctly the cookies.

Before use, please logon on the web server and retrieve cookies (``webclient`` and ``XSRF-TOKEN``) from your browser and set the variables ``XSRF-TOKEN`` and ``webclient``

If needed, set ``partitions`` variable (can be found in your browser network requests)

For now, only basic functions for managing access control are available.

## Example
Check example.py for more informations

## Todo

 - [ ] Automatically use cookies with a ``login()`` function
 - [ ] Create function ``getPartitions()``
