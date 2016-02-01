# Python script for fetching CDRs from Analytics API

import urllib2
import base64
import json

# Add in the URL with the proper parameters, i.e. fromDate, toDate,
# pageSize, pageNumber, and outputType
req = urllib2.Request("https://reports.thinkingphones.com/analytics/webservices/content/realtime/doQuery?path=voice/raw_data/realtime_call_detail_records.cda&dataAccessId=2&fromDate=2016-1-01&toDate=2016-01-14&pageSize=10&pageNumber=1&outputType=json");

# Add in your ThinkingPhones credentials
base64string = base64.encodestring('%s:%s' % ('mhaase.test', 'Think123')).replace('\n', '')

req.add_header("Authorization", "Basic %s" % base64string)
response = urllib2.urlopen(req).read()


parsed = json.loads(response)
print json.dumps(parsed, indent = 4, sort_keys = True)

