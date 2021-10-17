from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os

def split_and_save(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts_dir = config["artifacts"]['artifacts_dir']
    raw_local_dir = config["artifacts"]['raw_local_dir']
    raw_local_file = config["artifacts"]['raw_local_file']

    raw_local_file_path = os.path.join(artifacts_dir, raw_local_dir, raw_local_file)

    print(raw_local_file_path)
    
    df = pd.read_csv(raw_local_file_path)
    print(raw_local_file_path)
    print(df.head())