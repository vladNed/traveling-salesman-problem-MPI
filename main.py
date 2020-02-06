from algorithm import algorithm
import numpy as np
import time
from mpi4py import MPI
from random import randint

comm = MPI.COMM_WORLD
status = MPI.Status()
rank = comm.Get_rank()

def upload_data(example=2):
	with open(f'datasets/dataset{example}.txt', 'r') as file:
		cities = file.read().splitlines()
	return np.array([ list( map( float, coord.split() ) ) for coord in cities])


def master_program(cities=None):
	job_index = 0
	status = MPI.Status()
	size = comm.Get_size()

	#Generate first series of work for each slave
	for rank in range(1,size):
		job = [cities[job_index],np.where(cities == cities[job_index])[0][0]]
		comm.send(job,dest=rank,tag=1)
		job_index += 1


	while True:
		if job_index >= len(cities): break
		job = [cities[job_index],np.where(cities == cities[job_index])[0][0]]
		job_index += 1
		
		# Here the master received results from slave
		result = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
		distances.append(result[1])
		paths.append(result[0])

		# Send another job
		comm.send(job,dest=status.Get_source(),tag=1)
    
	for rank in range(1,size):
		result = comm.recv(source=MPI.ANY_SOURCE,tag=MPI.ANY_TAG,status=status)
		distances.append(result[1])
		paths.append(result[0])
		
	
	for rank in range(1,size):
		comm.send(0,dest=rank,tag=0)
		print(f'Closing thread {rank}')
	
	print(f'The shortest path is {paths[distances.index(min(distances))]} with {round(min(distances))} km to travel')
	print(time.perf_counter())

def slave_program(cities=None):
	while True:
		job = comm.recv(source=0,tag=MPI.ANY_TAG,status=status)
		if status.Get_tag() == 0: break
		order, length= algorithm(cities,job[0],job[1])
		comm.send([order,length],dest=0,tag=0)


if __name__ == "__main__":
	root = 0
	distances = []
	paths = []
	cities = upload_data(2)
	
	if rank == root:
		master_program(cities)
	else:
		slave_program(cities)	



		


