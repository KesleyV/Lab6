import app.csv_manager.state_manager_utils as sm
import math

base_path = 'tmp'
base_path_repo = '{}/repos'.format(base_path)
path_repo_state = '{}/state.csv'.format(base_path_repo)

def write_repo_state(end_cursor, total):
    sm.write_file(path_repo_state, [{ "end_cursor": end_cursor, "total": total}])

def write_repo_file(repo):
    sm.save(base_path_repo, 'repositories', repo)

def load_repo_state():
    state = sm.load_previous_state(base_path_repo)
    page_info = { "endCursor": ""}
    total = 0
    if(any(state)):
        page_info['endCursor'] = str(state['end_cursor']) if not str(state['end_cursor']) == 'nan' else ""
        total = int(state['total'])
    return page_info, total