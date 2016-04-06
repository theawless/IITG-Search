import sys, json

from search import search

# Load the data that PHP sent us
try:
    search_keyword = (sys.argv[1])
    radio = (sys.argv[2])
except:
    print "ERROR"
    sys.exit(1)

new_search=search_keyword.replace ("*", " ")
# Generate some data to send to PHP
results = search(new_search, radio)
# for i in results:
#    result[i] =  i['path']

# Send it to stdout (to PHP)

print json.dumps(results)

