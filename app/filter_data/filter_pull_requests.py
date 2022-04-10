import pandas as pd
from datetime import datetime
import os

def filter(pull):
    reviews = pull['reviews']
    createdAt = datetime.strptime(pull['criado_em'], "%Y-%m-%dT%H:%M:%SZ")
    closedAt = datetime.strptime(pull['fechado_em'], "%Y-%m-%dT%H:%M:%SZ")
    diff = closedAt - createdAt
    hours = diff.total_seconds() / 3600
    return reviews > 0 and hours >= 1

def get_repo_names(repo_limit):
    df = pd.read_csv('tmp/repos/repositories.csv')
    return [df.iloc[index].to_dict()['nome'] for index in range(0, repo_limit)]

def start(repo_limit):
    if not os.path.exists('tmp/sampled_data'):
        os.mkdir('tmp/sampled_data')
    
    repo_names = get_repo_names(repo_limit)
    for repo in repo_names:
        df = pd.read_csv('tmp/pull_requests/{}.csv'.format(repo))
        filtered_data = df[df.apply(filter,axis=1)]
        filtered_data.to_csv('tmp/sampled_data/{}.csv'.format(repo), index=False)
