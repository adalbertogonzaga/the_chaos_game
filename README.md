# "The Chaos Game" Python implementation - A Sierpinski Triangle visualization

[The Chaos Game](https://en.wikipedia.org/wiki/Chaos_game) is a game/method where the user/player has to pick an arbitrary/random/any point inside an equilateral triangle and the game's algorithm starts its 'thing' by drawing some points between (halfway the distance) the chosen point and any one of the 3 triangle's corners (randomly picked as well). By doing that repeatedly, the resulting image is a fractal composed by many triangles inside another triangle, what is called [***The Sierpinski Triangle***](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle).

The first time I've heard about it (on year 2018) was while I was reading some random things on [Quora](http://www.quora.com) (I usually do that...) and thought that it would be a good a idea to try to implement it using Java Script (instead of doing that on paper with a pencil). The Quora's article/response that I read can be check trought [this link](https://www.quora.com/What-are-some-mind-blowing-facts-that-sound-unreal-but-are-actually-true/answer/David-Prifti-1?srid=478Q).

## The first exercise - implementing it using Java Script

I did the Chaos Game implementation for the 1st time using a simple Java Script code embedded on a single HTML file. It can be checked [here](./TheChaosGame.html).

## Python implementation

Many years after "finishing" the HTML/Java Script implementation I've decided to the same thing but using Python. I thought it would be a good idea for having the first contact with the [PyGame](https://www.pygame.org/wiki/about) library.

### How to run it

Assuming you know how to run a [Python](https://www.python.org/) code, just create a new [virtual environment/venv/env](https://docs.python.org/3/tutorial/venv.html) (or run it on your system/global install) and install the **pygame** module. This is the main requirement.

After having the pygame library installed (and assuming the Python venv/installation is ready), just run the script by typing the following command on the terminal
```python pygame_start.py```

### Extra: using pip to install all the required libraries/modules

You can install any python module by running the command
```pip install <module_name>```. For example, you can install the **pygame** module by running the following command on the terminal;console: ```pip install pygame```.

Another cool way of installing the dependencies of a project using the **pip** utility is by reading them from a text file. In this project we are using the ```requirements.txt``` file to list all the dependencies, so to install them directly from this file (let's assume some projects can have a lot of them, so installing it one by one typing commands may not be a good idea...) we can use the following command ```pip install -r requirements.txt```.

The ```requirements.txt``` file can be produced and updated/maintained by using the following command: ```pip freeze > requirements.txt```.
