
from app.api.query_repository import get_repositories
import app.extract_data.process_pull_requests as process_pull_requests
import app.csv_manager.state_manager_repo as sm
from app.utils.ProgressBar import ProgressBar

def map_repo(repo):
    return {
        "nome": repo['name'],
        "dono": repo['owner']['login'],
        "url": repo['url'],
        "id": repo['id'],
        "pull_requests_merged": repo['merged']['totalCount'],
        "pull_requests_closed": repo['closed']['totalCount']
    }

def is_valid_repo(repo):
    merged_count = repo['merged']['totalCount']
    closed_count = repo['closed']['totalCount']
    return merged_count + closed_count >= 100

def start(repo_first, repo_limit, token):
    page_info, total = sm.load_repo_state()
    
    if total == repo_limit:
        print("{} repositories already processed".format(repo_limit))
        return

    while(repo_limit - total > 0):
        data = get_repositories(repo_first, page_info['endCursor'], token)     
        repositories = [ map_repo(r) for r in data['repositories'] if is_valid_repo(r)]
        size = 0
        if(len(repositories) + total > repo_limit):
            exceed = len(repositories) + total - repo_limit
            index = len(repositories) - exceed
            repositories = repositories[:index]
        size = len(repositories)
        total += size
        sm.write_repo_file(repositories)
        sm.write_repo_state(page_info['endCursor'], total)
        page_info = data['page_info']