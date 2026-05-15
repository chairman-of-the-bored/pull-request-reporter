from github import Github
from modelview import PrReport

def get_pr_report(access_token, repo_name, start_date):
     open_prs = []
     closed_prs = []
     ghclient = Github(access_token)

     repo = ghclient.get_repo(repo_name)
     prs = repo.get_pulls(state='all', sort='updated', direction='desc')
     #Go through each pr and add it to one of 2 lists.
     # also calc the "comment total"
     for pr in prs:
          if pr.updated_at.date() < start_date: #prs are descending with time
               break
          _process_pr(open_prs, closed_prs, pr)
     return PrReport(
          repo_name=repo_name,
          start_date=start_date,
          open_prs=open_prs,
          closed_prs=closed_prs,
     )

def _process_pr(open_prs, closed_prs, pr):
     # add a new attribute we reference in the template
     pr.comment_total = _get_comment_total(pr)
     if pr.state == 'open':
          open_prs.append(pr)
     else:
          closed_prs.append(pr)

def _get_comment_total(pr):
     issue_comments = pr.get_issue_comments()
     review_comments = pr.get_review_comments()
     ans = issue_comments.totalCount + review_comments.totalCount
     return ans
