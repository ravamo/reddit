# Reddit

## libs

This is the main libs used in this project:

* praw
* vcrpy
* unittest

## problem
I never used Reddit and I don't know well the behavior still confuse me with the terms 

## solution
I have written only one class, (as I will comment later, I think there should be two parts, one server or one client).
I charge the configuration of an init file, I generate a connection to the API using **praw** (in my opinion should a singleton pattern) and I am processing the content.

To do the sorting and I used a lambda function for comfort, with the volume I have not noticed anything of improvement that with the iterative mode

I write all the popo that I have generated in a list and I go read the list and generating the KPI.  Writing in a file of text should be a factory pattern in case need to change the export CSV, database, Kafka,etc..


## bonus track
1. How can you integrate your solution with a central scheduler?

No i can't use luigi in my mac.. I'm trying to use docker and pip install ..... but doesn't work.

2. How would you handle restarts and retries of failed tasks?

The principal idea is to generate a server part, this part read the information in an API create a model and send the queque part. 
The other part is a consumer this part reading a topic check the id (in my case an auto-increment number but you can use the id from the post, subreddit) consume the information and generates the kpi and save in persistence layer.  basically the Kappa architecture 
3. How can you containerize the pipeline?

attached my docker file
4. How can you automate deployment and testing of your solution?

the docker exit a script when building the container run the test if the test fail don't build the container  
