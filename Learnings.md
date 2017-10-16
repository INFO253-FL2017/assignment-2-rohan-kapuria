1) What is the function of the following technologies in your assignment:
<br/>Answer:
HTML: web pages
CSS: styling the web pages
JavaScript: validation of the contactUs form
Python:
Flask: Flask is a microframework for Python
HTTP: It is used to communicate with the web server
GET and POST requests: POST is used to send the request to mailgun (including mailgun credentials) to the server. GET is is used to get responses from the server

2) How does HTML, CSS, and JavaScript work together in the browser for this assignment?
<br/>Answer:
HTML provides the basic structure of sites, which is enhanced and modified by other technologies like CSS and JavaScript.
CSS is used to control presentation, formatting, and layout.
JavaScript is used to control the behavior of different elements.

3) How does Python and Flask work together in the server for this assignment?
<br/>Answer:
Flask is used to produce RESTful applications in Python. Flask provides very little upfront, not even an ORM, but the community provides a large set of extensions.


4) List all of the possible GET and POST requests that your server returns a response for and describes what happens for each GET and POST request
<br/>Answer:
GET / HTTP/1.1" 200 -
Standard response for successful HTTP requests. The actual response will depend on the request method used. In a GET request, the response will contain an entity corresponding to the requested resource. In a POST request, the response will contain an entity describing or containing the result of the action.

"POST /contact HTTP/1.1" 200 -
This is invoked when the form is submotted. Standard response for successful HTTP requests. The actual response will depend on the request method used. In a GET request, the response will contain an entity corresponding to the requested resource. In a POST request, the response will contain an entity describing or containing the result of the action.


 * Serving Flask app "webserver"
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
10.0.2.2 - - [16/Oct/2017 02:02:20] "GET / HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:02:21] "GET /8_Experiments_in_Motivation.html HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:02:22] "GET /contactus.html HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:02:22] "GET /static/js/script.js HTTP/1.1" 200 -
 * Serving Flask app "webserver"
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
10.0.2.2 - - [16/Oct/2017 02:13:26] "GET / HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:13:28] "GET /8_Experiments_in_Motivation HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:13:29] "GET /contactus HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:13:30] "GET /about_us HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:13:30] "GET / HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:13:32] "GET /How_to_Develop_an_Awesome_Sense_of_Direction HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:13:34] "GET /contactus HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:13:35] "GET /about_us HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:13:36] "GET / HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:13:37] "GET /8_Experiments_in_Motivation HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:14:01] "GET /about_us HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:14:05] "GET / HTTP/1.1" 200 -
10.0.2.2 - - [16/Oct/2017 02:14:07] "GET /Training_to_Be_a_Good_Writer HTTP/1.1" 200 -
