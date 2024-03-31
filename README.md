<h1 align="center" id="title">Programming in Python Projects</h1>

<p id="description">This repository contains all the assignments for the Programming in Python course at TUL.
</p>

<h2>▶️ dataset-analysis</h2>
The task in this assignment was to perform a statistical analysis of the given dataset, using Jupyter Notebook.
It utilizes Matplotlib, Pandas, and Seaborn for data analysis and visualization.

<h2>▶️ wolf-sheep-simulator</h2>
The task in this assignment was to develop a simulation involving a wolf that tries to catch sheep scattered in a meadow, which uses text mode.
The winner is determined by whether the wolf manages to catch all the sheep or not.
<h3>Features</h3>
* Logging the position of the wolf and sheep after each round in a JSON file
* Logging the number of alive sheep after each round in a CSV file
* Allowing for a break after each round, where the user can press any key to continue
* Using logging to provide information about the progress of the game

To run the game, you need to execute the ```script.py``` file. This script accepts several command-line arguments:
* ```-c, --config FILE:``` Specifies a path to a configuration file.
* ```-h, --help:``` Displays a help message.
* ```-l, --log LEVEL:``` Specifies a logging level. Choices are 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
* ```-r, --rounds NUM:``` Specifies the number of rounds that will be played.
* ```-s, --sheep NUM:``` Specifies the number of sheep that will be placed in the meadow.
* ```-w, --wait:``` If this argument is provided, the game will wait for you to press any key after each round.
Here is an example of how you might run the script from the command line:
```
python script.py -r 100 -s 10 -l INFO
```
This command will start the game with 100 rounds, 10 sheep, and the logging level set to 'INFO'.
Please note that the game logs will be written to ```data/pos.json``` and ```data/alive.csv```.

<h2>▶️ webapp</h2>
<p>The task in this assignment was to develop a web application storing data that can be used for a classification task performed by a machine learning model.

The stored data involves continuous and categorical features. The Django web application stores the data in a relational database consisting of a single table that holds individual data points as records.

Each data point consists of a height, weight, and quality value. The application provides an interface for managing these data points.</p>
<h3>Features</h3>
* Adding a new data point
* Viewing all data points
* Deleting a data point
* API endpoints for managing data points programmatically

To run the app, start the development server using ```python manage.py runserver```.