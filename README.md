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
I am using Flask , a microframework for python using Jinja2 template engine and a built in server.
for implementing the server side implementation of the Twitter Oauth for authentication and fetching the data.<br/>

My project structure:<br/>

app/ <br/>
    static/ <br/>
    templates/ <br/>
    views.py <br/>
run.py <br/>

app  : my project package <br/>
app/static : for storing static files such as js, css , images etc <br/>
app/templates : for storing templates <br/>
views.py : logic part goes here <br/>
run.py  :  for running up the project <br/>

config.py file in the root folder so that it can be easily accessible when required to edit or etc.

For getting the tweets that have been re-tweeted atleast once :
