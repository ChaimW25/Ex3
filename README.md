#  EX3 - OOP COURSE
# Directed Weighted Graph in Python

![גרף יפה](https://user-images.githubusercontent.com/74601548/147597078-12602deb-223a-4849-b3b8-9418eafdeb60.png)


## Introduction
In this assigment, we asked to convert the graph implementation we did in Java to Python. We will also finally be required to compare the performance of the program we wrote in Java with the performance of the program we will write in Python. In this task we implemented interfaces that creates a Directed Weighted Graph build from nodes and edges, later, we implemented algorithms class which run algorithms on the graph and then used matplotlib library to present our code in a graphic way.
 
## A view to our code:
An important detail about this project is the fact that we have already done most of the planning and implementation part in the previous project. you can have a look in the link : https://github.com/ChaimW25/ex2.git

That's why most of our hard work will be converting the old project in Java to Python language. It is important to remember that although the languages are similar, they are different, for example, we changed the uses in hasmap to dictionary. In addition The difference between the languages made us design the project differently and in a different structure, for example, We did not have to create a class of 'Edge'. We used the interfaces 'GraphInterface' and 'GraphAlgoInterface' as skeleton to our project and create their implementations in the classes 'DiGraph' and 'GraphAlgo', the class'Node' help us to implement the other classes. In addition, we created 2 tests classes: 'TestDiGraph', 'TestGraphAlgo'.

## UML of our project:


![image](https://user-images.githubusercontent.com/74601548/147594743-27545377-6c2b-40a7-925b-b8ecdcea6214.png)




## Introducing our json file graphs:

![graphs_page-0001](https://user-images.githubusercontent.com/74601548/147591292-38956503-1638-4131-9616-ecca33806a6b.jpg)

![graphs_page-0002](https://user-images.githubusercontent.com/74601548/147591303-000bb8bf-47b2-42cf-b24f-943f2f16da3e.jpg)

![graphs_page-0003](https://user-images.githubusercontent.com/74601548/147591307-4024884b-1566-4e17-b708-06ca050cb119.jpg)

![image](https://user-images.githubusercontent.com/74601548/147594841-6732da90-8f06-437d-a5c8-bcede5b08937.png)

## Our algorithm Performances:

As expected, the run times of our algorithm in Java were better than the run times in Python as we detailed in time trials and graphs on our wiki page which you can watch in this link:
https://github.com/ChaimW25/Ex3/wiki/Performances-report

## How to run the program?
Before Running this project, install the above package:matplotlib Version 3.4.3.

Then, go to the 'main' class and create one of the objects: 'DiGraph', 'GraphAlgo' and use their methods.
You can add as many nodes and edges as you like and run the algorithms on them, Or alternatively, load an existing graph from the json files.

If you want to display the graph on the screen: create GraphAlgo object and call the 'plot_graph' method.

An example for displaying a graph in the program in a few steps:
 
1. g_algo = GraphAlgo()
2. file = '../data/A0.json' (enter a json file you would like to load)
3. g_algo.load_from_json(file)
4. g_algo.plot_graph


