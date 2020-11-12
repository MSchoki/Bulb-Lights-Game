# bulb-lights
# bulb-lights

Bulb-lights is a game that trains your memory, using HTML, CSS, Python and JavaScript.

## Installation

### Getting Started
Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.

- download the zip-file
- unpack the files
- To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

        $ export FLASK_APP=app.py
        $ export FLASK_DEBUG=true
        $ flask run
        * Running on http://127.0.0.1:5000/

## Usage

Start the game with the button. The computer lights up a randomly selected light bulb and a sound is played. Then click on the same bulb light. If you're right the computer goes ahead with two bulbs and so on. Try to remember as many light bulbs as possible in the right order.
After each game you can type in your player-name and save your highscore.

## Features

- scorekeeper
- play-sounds
- highscore-list

## Support

Bulb-lights has been tested in the following browsers:

    Chrome - 75.0.3770.142
    Firefox - 68.0
