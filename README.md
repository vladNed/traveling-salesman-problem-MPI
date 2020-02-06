# Traveling Salesman Problem
This program only uses a greedy searach algorithm for finding the best distances between lat-long maps points.

Further implementation features: 
* Integration of Google Maps and weighted graph instead of a queue of points

# Modules
Then `algorithm.py` has all the metods for graph calculation.
 
Inside the `main.py` are the master-slave metods.
* The `def master_program()` method implements the master code with the semafor implementation.
First it sends some of the points to the slaves and then iterates through all and waits for recv.

# Installation Notes
Install MPI library from Microsoft website and use `pip install mpi4py` in order to fully use the MPI lirary.
 

