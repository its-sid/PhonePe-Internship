# Week 2 Tasks:
1. summary for the day/week/month:<br />
highest requested host<br />
highest requested upstream_ip<br />
highest requested path (upto 2 subdirectories ex: /check/balance)<br />

2. total requests per status code (Ex: count of requests returning 404/401/502/504/500/200)

3. Top requests<br />
top 5 requests by upstream_ip<br />
top 5 requests by host<br />
top 5 requests by bodyBytesSent<br />
top 5 requests by path (upto 2 subdirectories ex: /check/balance)<br />
top 5 requests with the highest response time<br />
get top 5 requests returning 200/5xx/4xx per host<br />

4. find the time last 200/5xx/4xx was received for a particular host

5. get all request for the last 10 minutes

6. get all the requests taking more than 2/5/10 secs to respond

7. get all the requests in the specified timestamp (UI should have the capability to accept to and from timestamp Ex: from: 06/Mar/2021:04:48 to 06/Mar/2021:04:58)

8. the app should also be able to take the host (Ex: apptwo-new.ppops.com) as input and give the stats mentioned above.
