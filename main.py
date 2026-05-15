import mailclient
import ghclient
import modelview
import argparse
import json
import datetime
def merge_configs():
    parser = argparse.ArgumentParser(description='Email notification for pull requests')

    parser.add_argument('--config-file', default="", help='Path to config file')
    parser.add_argument('--secrets-file', default="", help='Path to config file with secrets')
    args = parser.parse_args()
    
    config = {}
    secrets = {}
    with open(args.config_file, 'r') as cf:
        config = json.load(cf)
 
    with open(args.secrets_file, 'r') as sf:
        secrets = json.load(sf)

    return config, secrets

if __name__ == "__main__":
    c, s = merge_configs()

    today = datetime.date.today()
    margin = datetime.timedelta(weeks=c['prior_weeks'])
    prior_week = today - margin

    repo = c['github']['repo']
    pr_report = ghclient.get_pr_report(s['github']['access_token'], repo, prior_week)
    content = modelview.render_content(pr_report)
    with open('report.html', 'w') as rf:
        rf.write(content)

    mailclient.send_mail(s['gmail']['password'],c['addresses']['from'],c['addresses']['to'], 
        f"Pull Request Report for {repo}","./report.html")
    print("Enjoy your report!")
