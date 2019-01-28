import socket
import os
import platform
import multiprocessing




print(socket.gethostname())
print(os.name)
print(platform.system())
print(platform.release())
print(multiprocessing.cpu_count())
