from delphin.interfaces import ace
from delphin.mrs import simplemrs, mrx, dmrx, simpledmrs, eds
from delphin.mrs.components import Pred
import json_lines

with open('expanded.jl', 'rb') as f:
    for item in json_lines.reader(f):
        if item['parsed']:
            try:
                x = simplemrs.loads(item['simplemrs'], single=True, errors = 'strict')
                root = x.ep(x.nodeid(x.index))
            except:
                print(item['sent'])
