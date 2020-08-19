# Supervised_Machine_Learning_Flask_Deployment

For deployment of ML models using Flask, we have the following five subdivisions of work files.
- static/css contains the styling elements for our webpage.
- templates contains the html code for the webpage.
- Linear_Regression.py is the main python file which has the code for building the ML model. We have used the pickle module to serialise our model. So, running this Linear_Regression.py file creates a pickle file named Linear_Regression.pkl
- app.py uses flask API for hosting our model on a local port(port 5000) 
- request.py is used to return important json formats.

The flow goes this way:-
First we create Linear_Regression.py file. Running this creates our pickle file for use.
Then we run app.py to use our model and render it on a local port having specifications as written in the templates folder and static/css. 
