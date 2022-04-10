import requests
import time

endpoint = "https://api.github.com/graphql"
interval_retry = 5
max_retries = 5

def create_query(params, query_template):
  q = query_template
  for k in params.keys():
      value = params[k]
      if type(value) == int:
          q = add_param_number(k, value, q)
      else:
          q = add_param_string(k, value, q)
  return q

def add_param_number(name, value, query):
    return query.replace(name, '%d' % value) 

def add_param_string(name, value, query):
    return query.replace(name, "null") if value == "" else query.replace(name, '"%s"' % value) 

def retry(query, token, sleep):
    next_sleep = sleep + interval_retry if sleep < 25 else sleep
    retry_count = sleep/interval_retry
    time.sleep(sleep)
    return execute_query(query, token, next_sleep)


def execute_query(query, token, sleep = 0):
    request = ''
    try:
        request = requests.post(endpoint, json = {'query': query}, headers = {
        'Content-Type': 'application/json',
        'Authorization': 'bearer ' + token
        })
    except (Exception) as e:
        return retry(query, token, sleep)

    if  request.status_code == 200:
        data = request.json()
        return data if "data" in data else retry(query, token, sleep)
    else:
        return retry(query, token, sleep)