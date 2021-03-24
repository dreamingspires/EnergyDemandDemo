import pandas as pd
import typer
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape


def load_dfs(dir: Path):
    filenames = {
        'A': 'A.csv',
        'B': 'B.csv',
        'C': 'C.csv',
        'D': 'D.csv',
        'E': 'E.csv',
        'F': 'F.csv',
    }
    dfs = {name: pd.read_csv(dir / filenames[name]).to_dict() for name in filenames.keys()}
    return dfs


input_template = Path("EnergyDemand.jinja.html")
output_file = Path("EnergyDemand.html")


env = Environment(
    loader=FileSystemLoader(input_template.parent),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template(input_template.name)

stream = template.stream(dfs = load_dfs(Path("zoneData")))
with output_file.open('w') as file:
    stream.dump(file)


