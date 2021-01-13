#OOP Course Exercise 3.

The following project represents a data structure for a directed-weighted graph data structure, which uses python dictionary data structure to achieve O(1) complexity for searching and inputting specific nodes.

Additionally, the project contains 3 ‫UnitTests tests to test (::drums::)  each class we've created - Node, DiGraph, and GraphAlgo.

The basic implementation of the graph is classic through using a dictionary data structure to achieve O(1) complexity for searching and inputting specific nodes. Each node is a class by itself which contains 2 dictionary data structures one for all edges where this node is at the end of the edge and one for all edges where this node is at the start of the edge. The Algorithm class is implementing very known algorithms like Dijkstra, DFS, and SCC algorithm mainly based on Tarjan's strongly connected components algorithm plus all the required by the interface algorithms like saving and loading the graph as a JSON file. More info you can find in the project's wiki.

The project also contains a visualization of the graph data structure using the Matplotlib library.
Also, there is an implementation of the GUI using the NetworkX library and a comparison with an implementation of the graph in our previous project (https://github.com/VictoKu1/OOP_Ex2) in Java and a runtime comparison with NetworkX visualization.

The main 2 classes DiGraph and GraphAlgo and the implementing GraphInterface and GraphAlgoInterface "interfaces" .that were provided with the assignment in the following repository (https://github.com/simon-pikalov/Ariel_OOP_2020/tree/master/Assignments/Ex3).

The project was created on Python interpreter version 3.8.

#Downloading and running.
## Linux 

Please make sure that your Python interpreter version is 3.8 or higher, if not simply install it by following the instructions in the following: link: https://tecadmin.net/install-python-3-8-ubuntu/.

1) Open the terminal by pressing simultaneously ctrl+alt+t.
2) Copy the following to the terminal :

```
git clone https://github.com/porat-ah/assignment_3_oop.git

```
3) Make sure you have Pycharm.

4) Enter the project file using Pycharm.

5) Enjoy!

## Windows

Please make sure that your Python interpreter version is 3.8 or higher, if not simply install it by following the instructions in the following link: https://www.python.org/downloads/.

1) Open your command prompt (CMD).
2) Copy the following to the CMD :

```
git clone https://github.com/porat-ah/assignment_3_oop.git

```
3) Make sure you have Pycharm.

4) Enter the project file using Pycharm.

5) Enjoy!
