This is the github repository of a Team Project of the University of Mannheim.
The goal of this project is to analyze a dataset of tweets about the topic Climate Change using Computer Vision and Natural Language Processing techniques.


# GUI Instructions:

start Port tunneling with the following command:  
ssh -L 5173:localhost:5173 username@wifo5-33.informatik.uni-mannheim.de  
where 5173 is replaced by the port on which vue.js is running and username is replaced by your actual username    
Then you can access the GUI in the browser on your local machine on the adress localhost:5173  

# Backend Instructions
go to directory  
/data/teamproject/Flask  
activate venv with   
source env/bin/activate    
run flask Backend with  
flask run --port=5001  

to keep job running after you disconnect your ssh session, use screen command

then also start port tunnel for backend on your computer with command
ssh -L 5001:localhost:5001 username@wifo5-33.informatik.uni-mannheim.de


# Documentation
The Backend revcieves a http request args for the columns and search words to be filtered.


The argument "custom" is meant to hand over parameters for a custom search/aggregation at a later time, that can then be easily implemented in python in the flask app.py

The Backend then returns a list with pictures that fulfil the search criteria, so the GUI can load them and select a couple of them to show.

The individual parameters of the current shown center image are requested by another Backend call, to avoid large transfer of data if the filter applies to a large ammount of pictures

Important for future changes in the input dataset:
The checkboxes are created from a hardcoded list that contains the column names (as well as "custom")
The names must match the column description, since the backend will compare it to the columns of the input records. Otherwise the search function will not work.
So if the column names change, the list in index.html must be adapted.
# TODO
-Error Handling  
-Performance  
-Aggregation Display  
-Layout  
