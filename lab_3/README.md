## Questions

What your application does
- In this lab_2, API endpoint 'predict', takes INPUT JSON data and passed to ML model which can predict 
	and returns 'Median House Value'.

How to build your application
- we can run python script 'train.py' to train our model which will be used to pass INPUT features through FastAPI
	endpoint '/predict'. Further, we will use Docker file to build our application inside docker container.

How to run your application
- we create Docker file to setup a container that will hold our application, further
	we can run through github actions to setup our environment.

How to test your application
- Using pytest command, we can run tests on each API endpoints. We can run tests
	on our created poetry environment by passing the input data through curl command.

## Answer the following questions in your README.md

What does Pydantic handle for us?
- It handles for data data modeling/parsing the input data. It is well-efficient for error handling and a custom
	validation purpose. In our lab, we use pydantic models for FASTAPI application for parsing requests and responses.
 
What do GitHub Actions do?
- GitHub Actions allows to automate our workflow process to build, test, and deploy our application in desired
	location. It is a pipeline for continous integration and continous delivery.

In 2-3 sentences (plain language), describe what the Sequence Diagram below shows.
- The Sequence Diagram below shows that user provides input data/features as payload on JSON objects. The payload
	will be validated by pydantic model and returns if any errors in input data. If there are no error on input
	data, it will passed on ML model which returns as stored value on ouput data model designed in JSON format.
