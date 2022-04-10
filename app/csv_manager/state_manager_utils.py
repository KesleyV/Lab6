import pandas as pd
import os

def add_items(file, items):
    df = pd.DataFrame(items)
    df.to_csv(file, mode='a', header=False, index=False)

def write_file(file_name, items):
    df = pd.DataFrame(items)
    df.to_csv(file_name, index=False)

def load_previous_state(base_name):
    if not os.path.exists(base_name):
        os.mkdir(base_name)
    if (os.path.isfile(base_name + '/state.csv')):
        df = pd.read_csv(base_name + "/state.csv")
        return df.iloc[0].to_dict()
    return {}

def create_folder(basename):
    if not os.path.exists(basename):
        os.mkdir(basename)

def save(path, file_name, items):
    if len(items) == 0: return
    create_folder(path)
    path_file = "{}/{}.csv".format(path, file_name)
    if os.path.isfile(path_file):
        add_items(path_file, items)
    else:
        write_file(path_file, items)

def delete_state(path):
    file_name = '{}/state.csv'.format(path)
    if os.path.isfile(file_name):
        os.remove(file_name)