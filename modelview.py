from datetime import date
from jinja2 import Template
from dataclasses import dataclass, field, asdict

@dataclass()
class PrReport:
    repo_name: str = None
    start_date: date = None
    open_prs: list = field(default_factory=list)
    closed_prs: list = field(default_factory=list)

def render_content(pr_report):
    with open('template.html.jinja', 'r') as tf:
        t = Template(tf.read())
        return t.render(asdict(pr_report))
