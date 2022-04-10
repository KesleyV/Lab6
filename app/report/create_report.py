import pandas as pd
from datetime import datetime

def transform(pull, repo):
    createdAt = datetime.strptime(pull['criado_em'], "%Y-%m-%dT%H:%M:%SZ")
    closedAt = datetime.strptime(pull['fechado_em'], "%Y-%m-%dT%H:%M:%SZ")
    diff = closedAt - createdAt
    hours = int(diff.total_seconds() / 3600)
    return {
        "tamanho": pull['tamanho'],
        "tempo_de_analise": hours,
        "descricao": pull['descricao'],
        "interacoes": pull['comentarios'],
        "reviews": pull['reviews'],
        "repo_url": repo['url']   
    }

def start(repo_limit):
    df = pd.read_csv('tmp/repos/repositories.csv')
    files = []
    for index, repo in df.iterrows():
        df2 = pd.read_csv('tmp/sampled_data/{}.csv'.format(repo["nome"]), usecols = ['criado_em', 'fechado_em', "comentarios", "descricao", "tamanho", "reviews"])
        files.append(pd.DataFrame([transform(pull,repo) for index, pull in df2.iterrows()])) 
    df = pd.concat(files)
    df.to_csv('report.csv', index=False)