import app.api.query_utils as query_utils

query_template = """{
  search(query: "stars:>100", type: REPOSITORY, first: $first, after: $after) {
    nodes {
      ... on Repository {
        id
        name
        url
        owner {
          login
        }
        closed: pullRequests(states: CLOSED) {
          totalCount
        }
        merged: pullRequests(states: MERGED){
          totalCount
        }
      }
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
  rateLimit {
    limit
    remaining
  }
}"""

def parse_data(res):
  repositories = res['data']['search']['nodes']
  page_info = res['data']['search']['pageInfo']
  rate_limit = res['data']['rateLimit']
  return {"repositories": repositories, "page_info": page_info, "rate_limit": rate_limit}

def get_repositories(first, after, token):
  query = query_utils.create_query({"$after": after, "$first": first}, query_template)
  data = query_utils.execute_query(query, token)
  return parse_data(data)