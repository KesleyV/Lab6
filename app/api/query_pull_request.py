import app.api.query_utils as query_utils

query_template = """query MyQuery {
  repository(name: $name, owner: $owner) {
    pullRequests(states: [MERGED, CLOSED], first: $first, after: $after) {
      nodes {
        closedAt
        state
        reviews {
          totalCount
        }
        comments {
          totalCount
        }
        title
        participants {
          totalCount
        }
        additions
        deletions
        body
        createdAt
        id
      }
      pageInfo {
        endCursor
        hasNextPage
      }
      totalCount
    }
  }
  rateLimit {
    limit
    remaining
  }
}"""

def parse_data(res):
  pull_requests = res['data']['repository']['pullRequests']['nodes']
  page_info = res['data']['repository']['pullRequests']['pageInfo']
  total_count = res['data']['repository']['pullRequests']['totalCount']
  rate_limit = res['data']['rateLimit']
  return {"pull_requests": pull_requests, "page_info": page_info, "rate_limit": rate_limit, 'total_count': total_count}

def get_pull_requests(repo_name, repo_owner, first, after, token):
  params = {"$name": repo_name, "$owner": repo_owner, "$first": first, "$after": after}
  query = query_utils.create_query(params, query_template)
  data = query_utils.execute_query(query, token)
  return parse_data(data)