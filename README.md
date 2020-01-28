# How to run


As is, the project uses python and pandas with a dash of pytest for all the
beautiful tests I intended to write and ran out of time for.

It's recommended to use Pipenv:

`pipenv install`

`pipenv run python slcsp.py`

however a requirements.txt file is also provided
if you'd prefer to not use Pipenv.

`set up a virtualenv for yourself`

`python slcsp.py`


# How it works

Overall, I went off the deep end with exploratory data analysis using pandas.
Although this makes for more options for further analysis, it ended up (as I suspected at the beginning) being a bit overkill for the parameters of the project.

# How to test

You can use pytest! However, I ran out of time for tests; though there are some simple docstring tests
and some notes in the test file on what to test for. 

# What I learned

Although I used to use pandas all the time for data science/ETL work, it had been a minute. I learned that I was a bit rusty on the syntax. Also, it was hard to shoehorn my knowledge/workflow of pandas into a more application/test-driven development mindset, so I spent part of my time researching that instead of writing a solution. 

# What I'd do differently

Well, I made an actually properly working version using pandas here: https://github.com/easherma/slcsp/tree/patch-pandas

Furthermore, I would've started with a simple, naive approach using built-in python functionality. This would've gotten me results faster, and been easier to write tests for. A naive approach wouldn't scale well or be as flexible; this is where a highly optimized tool like pandas would come in handy; but only _after_ there is already a base level of functionality + tests to verify output. 
