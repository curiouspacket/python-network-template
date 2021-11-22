import yaml
from jinja2 import Template
from pprint import pprint as p

#read in yaml file
with open('nodes.yaml') as file:
    nodes = yaml.safe_load(file)
#p(nodes)

#read in jinja template file
with open('ospf-temp.j2') as file:
    template = Template(file.read())

#iterate over devices 
configuration_data = template.render(nodes)
print(configuration_data)