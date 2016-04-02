import sys, json

from search import search

# Load the data that PHP sent us
try:
    search_keyword = json.loads(sys.argv[1])
except:
    print "ERROR"
    sys.exit(1)

# Generate some data to send to PHP
results = search(search_keyword)
size_of_json_data = len(results)
# for i in results:
#    result[i] =  i['path']


# Send it to stdout (to PHP)
print json.dumps(results, size_of_json_data)