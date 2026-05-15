from datetime import date
from jinja2 import Template
from dataclasses import dataclass, field

@dataclass()
class PrReport:
    repo_name: str = None
    start_date: date = None
    open_prs: list = field(default_factory=list)
    closed_prs: list = field(default_factory=list)

def render_content(pr_report):
    with open('template.html.jinja', 'r') as tf:
        t = Template(tf.read())
        return t.render(
            repo_name=pr_report.repo_name,
            start_date=pr_report.start_date,
            open_prs=pr_report.open_prs,
            closed_prs=pr_report.closed_prs,
        )
