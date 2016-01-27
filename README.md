# google_traffic
Gathering and Analyzing Traffic Data from Google Map's API

For this project, you'll need a Google API Key. You can do so here:
https://developers.google.com/maps/documentation/javascript/get-api-key#key

traffic_times.py is a python2 script that returns 3 travel duration estimates assuming you depart
now.  You can run it via "python traffic_times.py to_work" to output times from the "home" variable to 
the "work" variable in the script, or "python traffic_times.py from_work" for the reverse.

I have my crontab setup to run the following:

Run to_work during morning commute times:
*/10 11-15 * * 1-5 /usr/bin/python traffic_times.py to_work
Run from_work during evening commute times:
*/10 19-23 * * 1-5 /usr/bin/python traffic_times.py from_work

I run the r script from time to time to update graphs (Rscript traffic_plots.R)

*******************************************************************************
MIT License
Copyright (c) 2016 Michael Smith

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

*******************************************************************************


