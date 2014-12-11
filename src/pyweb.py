#!/usr/bin/python

import httplib

# Configure the proxy
proxy_host = "10.13.11.4";
proxy_port = 8080;
h = httplib.HTTPConnection(proxy_host, proxy_port);

# Issue the 'GET' request
h.request('GET', 'www.google.co.uk');
r = h.getresponse();

# Parse the headers information
rh = r.getheaders();
print 'Headers:';
idx=0;
for i in rh:
    print idx, ") ", i[0], ':', i[1];
    idx += 1;
print '\n';

# Get the retrieved content
rr = r.read()
print 'Content:'
print rr
print '\n'

h.close()
