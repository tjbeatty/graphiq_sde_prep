import urllib.request, ssl, json

# Prevent cert error
ssl.match_hostname = lambda cert, hostname: True

# Get response from url as object
response = urllib.request.urlopen('https://monitor4b.d.giq.io/monitor/queue')

# Get response as string (.decode() since it default returns as bytes)
string = response.read().decode('UTF-8')

# Load data into json
json_data = json.loads(string)

# Parse into individual elements and print
for entry in json_data:
    json_string = json.dumps(entry)
    json_dict = json.loads(json_string)
    job_name = json_dict['nice_job_name']
    server = json_dict['server']
    print("Job Name: {0}\t\tServer: {1}\n".format(job_name, server))
