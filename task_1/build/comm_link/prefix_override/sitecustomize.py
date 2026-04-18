import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/abhay-ramasamy/AUVT1/task_1/install/comm_link'
