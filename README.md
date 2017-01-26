#Twitter Client

To implement a simple Twitter client that can connect to Twitter services and fetch and display the tweets such that: <br/>
Contains the hashTag #custserv<br/>
re- Tweeted atleast once 

#My Research  :P
Twitter is great! and is concerned about our security .<br/>
With Twitter api1.0 , it was pretty easy to get data from twitter using REST apis, <br/>
but with twitter api1.1, oAuth is required, which makes things a little hard.<br/>
Now we are required to create a twitter app and thus we get the credentials which has to be kept safe and secure.<br/>

Now , if we are at the client side and interacting with the Twitter apis, then :<br/>
The nature of oAuth forces the client to expose applications credentials and this is a security vulnerability.<br/>
The provider may not support CORS and makes its impossible for the client to communicate with the provider.<br/>

So a simple and safer solution is needed in which : < br/>
We do not reveal the credentials to the client.<br/>
Should work even if the provider does not support CORS. <br/>
Great !<br/>

#Implementation
I will be doing the things on the server side. In this way there will be no need for exposing the credentials and this the things remain secure.
Then a client can simply request to the server for the resources ( in this case 'Tweets' ) using ajax etc.

I am using Flask , a microframework for python using Jinja2 template engine and a built in server.
for implementing the server side implementation of the Twitter Oauth for authentication and fetching the data.<br/>

###Server Side Implementation

My project structure:<br/>

app/ 
    static/ 
    templates/ 
    views.py 
run.py 

app  : my project package <br/>
app/static : for storing static files such as js, css , images etc <br/>
app/templates : for storing templates <br/>
views.py : logic part goes here <br/>
run.py  :  for running up the project <br/>

config.py file contains the twitter app credentials and kept secure.
It is kept in the root folder so that it can be easily accessible when required to edit or etc.
The config file have been added to the app in the __init__.py.

requirements.txt consist of all the libs required at the server side.


I have implemented the following routes :

GET /
GET /index
fetches the tweets for the #custserv and the tweets that have been re-Tweeted atleast once.

GET /api/default
returns the json Object of the fetched tweets which have the #custserv have been re-Tweeted atleast once.
Can be used for ajax request from the client side

GET /api/tweets/<hash_tag>
fetches the tweets containing hashTag hash_tag (in the url) and returns along side the index.html template

GET /api/tweets/get-json/<hash_tag>
returns the JSON object of the fetched tweets which contain the hashTag hash_tag and have been re-Tweeted atleast once.
Can be used for making ajax request for the tweets from the client side.

Now CORS may occur when we try to request resources from other server , so i have allowed CORS in each route at the server side to deal with cross origin request.



###Client Side Implementation

At client side i have : 

Implemented a Loader to show to the user while the tweets are being fetched using ajax call. ( for better UX )
The loader is implemented using pure css.

A simple ajax request to fetch all the tweets and show them in list view in the DOM using jquery.

In this case i have made request to the url : http://localhost:8000/api/default
which returns the JSON of the fetched tweets array which contains the hashTag #custserv and have been re-Tweeted atlease once ( as per the task)

But the client can be modified to get the tweets for any particular hashTag using the api 
GET /api/tweets/get-json/<hash_tag>

Each tweet in the list item is clickable and when clicked shows a popup which gives the other details about that tweet like re-Tweet count, Tweet user etc.

Structure of the client side:

client/
	css/
	js/
	client.html 

	
#Running up the Project

Setting up the serve side:

Go into the project dir 
	cd flask-tweet

Create a virtual environment for the project
	virtualenv flask

Activate the virtual env 
	source flask/bin/activate

Installing the requirements using pip.
	pip install -r requirements.txt

Run the server now :)
	python run.py

This will start the server at port 8000 Yeaah!!!
Now either you can simply go to the browser and open localhost:8000 and it will fetch the tweets and render it on the page.
You can also try other routes as well as defined and explained above.
or 
you can use the client as described below ( Preferred )


Client Side :

Now go inside the client folder 
	flask-tweet/client

open the client.html file in the browser.
Wait for some time and it will fetch the tweets containing #custserv and which have been re-Tweeted once.
Click on the tweet for getting more info :)


for any other queries :
Contact me at abhishekg785@gmail.com
