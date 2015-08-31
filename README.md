# iframe-not-rendering
Minimal test case for iframe not rendering (Chrome bug
https://code.google.com/p/chromium/issues/detail?id=481922).

Seems like higher network latencies is required (e.g. 450Kbps, RTT >= 150ms).
Use network throttling to achieve this with Chrome Dev Tools.

Screenshot:
![Chrome Network Throttling Screenshot](chromeNetworkThrottling.png)

Assuming server on port 8000 visit: http://localhost:8000/

Expected: iframe with text inside

Actual: iframe not rendered (shows as white)
