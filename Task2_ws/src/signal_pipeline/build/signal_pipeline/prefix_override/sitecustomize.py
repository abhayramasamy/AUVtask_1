import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/abhay-ramasamy/AUVT1/Task2_ws/src/signal_pipeline/install/signal_pipeline'
