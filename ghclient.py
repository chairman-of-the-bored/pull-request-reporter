from os import stat
from github import Github
from modelview import PrReport
def get_pr_report(access_token, repo_name, start_date):
     open_prs = []
     closed_prs = []
     ghclient = Github(access_token)

     repo = ghclient.get_repo(repo_name)
     print("starting api")
     prs = repo.get_pulls(state='all', sort='updated', direction='desc')
     print("starting filter")
     #Go through each pr and add it to one of 2 lists.
     # also calc the "comment total"
     for pr in prs:
          if pr.updated_at.date() < start_date: #prs are descending with time
               break
          open_prs,closed_prs = _process_pr(open_prs,closed_prs,pr)
     pr_report = PrReport()
     pr_report.repo_name = repo_name
     pr_report.start_date = start_date
     pr_report.open_prs = open_prs
     pr_report.closed_prs = closed_prs
     return pr_report

def _process_pr(open_prs, closed_prs, pr):
     # add a new attribute we refrence it in the template
     pr.comment_total = _get_comment_total(pr)
     if pr.state == 'open':
          nopen_prs = open_prs + [pr]
          return nopen_prs,closed_prs
     else: # state is either open or closed
          nclosed_prs = closed_prs + [pr]
          return open_prs,nclosed_prs

def _get_comment_total(pr):
     issue_comments = pr.get_issue_comments()
     review_comments = pr.get_review_comments()
     ans = issue_comments.totalCount + review_comments.totalCount
     return ans
