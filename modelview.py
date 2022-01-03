from datetime import date
from jinja2 import Template
from dataclasses import dataclass, asdict

@dataclass()
class PrReport:
    def __init__(self):
        pass
    repo_name: str
    start_date: date
    open_prs: list
    closed_prs: list

def render_content(pr_report):
    with open('template.html.jinja', 'r') as tf:
        t = Template(tf.read())
        # use the asdict func to make each feild a key.
        return t.render(asdict(pr_report))
