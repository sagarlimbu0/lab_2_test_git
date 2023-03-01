### First Section:

* What your application does
 - Serves web application API requests with different endpoints and returns with response
 - web application is hosted inside a docker container 

* How to build your application
- application is built in a poetry environment
- with specified package installation. EG: fastapi, uvicorn, requests, etc.         

* How to run your application
- using `uvicorn` we can run our web application
- we need to Dockerfile that will be used to create a new docker container with supporting files of the web application. further we need to create a script that will spin up the container and test the web application

         
* How to test your application
- We can create `testing` python script for each end points
- with `pytest` we can check for `assertions` to return True or False status or with desired comments
     
### In a separate section, answer the following questions
         
* What status code should be raised when a query parameter does not match our expectations?
- Client Error Response: 400- 499
- Provide response or comments for desired output
         
* What does Python Poetry handle for us?
- Python Poetry manages the dependencies of the packages including updates on the existing ones
- Isolates the virutal environment from our system environment
       
* What advantages do multi-stage docker builds give us?
- Reduces the number of dependencies and unnecessary packages in the image
- Reduces the vulnerability and improves security base

