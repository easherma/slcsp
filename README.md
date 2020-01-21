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

You can use pytest! However, I ran out of time for tests; there are some docstring tests
and some notes in the test file
