import sys, json

from search import search

# Load the data that PHP sent us
try:
    search_keyword = json.loads(sys.argv[1])
    radio=json.loads(sys.argv[2])	
except:
    print "ERROR"
    sys.exit(1)

# Generate some data to send to PHP
results = search(search_keyword)
# for i in results:
#    result[i] =  i['path']


# Send it to stdout (to PHP)
print json.dumps(results)