import os, sys
BASE_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(BASE_DIR, 'lib'))
sys.path.append(os.path.join(BASE_DIR, '..'))

import argparse
from dataset import Dataset
from network_config import NetworkConfig

parser = argparse.ArgumentParser()
parser.add_argument('config_file', help='YAML configuration file')
parser.add_argument('--test', action='store_true', help='Run network in test time')
parser.add_argument('--test_pc_in', type=str)
parser.add_argument('--test_h5_out', type=str)
parser.add_argument('--test_folder', type=str)
args = parser.parse_args()

conf = NetworkConfig(args.config_file)

batch_size = conf.get_batch_size()
n_max_instances = conf.get_n_max_instances()

train_data = Dataset(
    batch_size=batch_size, 
    n_max_instances=n_max_instances, 
    csv_path=conf.get_train_data_file(), 
    noisy=conf.is_train_data_noisy(), 
    fixed_order=False, 
    first_n=conf.get_train_data_first_n()
)

for data in train_data:
    pass