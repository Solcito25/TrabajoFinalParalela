import os

for i in range(60,100,5):
    command='mpiexec -n 18 python -m mpi4py Random.py 5 3 '+str(i)
    print(command)
    os.system(command)