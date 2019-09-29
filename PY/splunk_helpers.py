#!/usr/local/bin/python3

import os
import sys
import time
import splunklib.client as client
from splunklib import results as pkg_results

params = {
    'host': 'splunk-api.idk.domain.com',
    'port': 8089,
    'username': os.environ.get('SPLUNK_USERNAME', None),
    'password': os.environ.get('SPLUNK_PASSWORD', None),
    'scheme': 'http'
}


def perform_splunk_query(query):

    print("Fetching logs from Splunk")

    query_params = {}
    try:
        service = client.connect(**params)
        # print isinstance(service, client.Service)
        if not isinstance(service, client.Service):
            print("Error connecting splunk")
            exit(1)

        print ("Successfully connected to splunk")
        if not query.startswith('search'):
            query = 'search ' + query
        # print("Query: ", query)
        job = service.jobs.create(query, **query_params)
        # print("job:", job)

        while True:
            while not job.is_ready():
                sys.stdout.flush()
                sys.stdout.write("not ready ...\n")
                sys.stdout.flush()

            stats = {
                'isDone': job['isDone'],
                'doneProgress': job['doneProgress'],
                'scanCount': job['scanCount'],
                'eventCount': job['eventCount'],
                'resultCount': job['resultCount']
            }
            progress = float(stats['doneProgress']) * 100
            scanned = int(stats['scanCount'])
            matched = int(stats['eventCount'])
            results = int(stats['resultCount'])

            status = ("\r%03.1f%% | %d scanned | %d matched | %d results" % (
                progress, scanned, matched, results))
            sys.stdout.flush()
            sys.stdout.write(status)
            sys.stdout.flush()

            #print("stats['isDone'] =", stats['isDone'])
            if stats['isDone'] == '1':
                sys.stdout.write('\n')
                break

            time.sleep(1)

        result_list = []
        for r in pkg_results.ResultsReader(job.results(count=0)):
            x = dict(r)
            # print x
            result_list.append(x)

        job.cancel()
        # print ("response", result_list)
        return result_list

    except Exception as e:
        print("Exception:", e)
        sys.exit(1)
