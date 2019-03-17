
from delphin.interfaces import ace
from delphin.mrs import simplemrs, mrx, dmrx, prolog
from delphin.mrs import eds

import os, sys
import jsonlines


def get_pos(ep):
    if ep.pred.pos:
        return ep.pred.pos
    elif ep.pred.lemma == 'named':
        return 'n'
    else:
        return ep.pred.pos


def get_lemma(ep):
    ''' Get lemma from a pyDelphin elementary predicate '''
    # if ep.pred == 'named':
    if ep.carg:
        return ep.carg
    elif ep.pred.pos == 'u' and ep.pred.sense == 'unknown' and "/" in ep.pred.lemma:
        cutpoint = ep.pred.lemma.rfind('/')
        return ep.pred.lemma[:cutpoint]
    elif ep.pred.type == 0:
        return None
    else:
        return ep.pred.lemma

    
def get_pred(ep):
    return dict(cfrom = ep.cfrom,
                cto = ep.cto,
                pos = get_pos(ep),
                sem = ep.pred.sense,
                type = ep.pred.type,
                form  = ep.pred.string,
                lemma = get_lemma(ep))


def parse(sent):
        res = ace.parse(os.getenv('ERG_DAT','/Users/ar/hpsg/ace/terg.dat'),
                        sent, cmdargs=['--timeout', '60', '--max-words', '150', '-n', '1',
                                       '--max-chart-megabytes', '4000', '--max-unpack-megabytes', '5000',
                                       '--rooted-derivations', '--udx', '--disable-generalization'])

        data = {}
        data["sent"] = sent
        if len(res['results']) > 0:
            x = res.result(0).mrs()
            data["parsed"] = True

            data["simplemrs"] = simplemrs.dumps([x])
            data["preds"] = [get_pred(ep) for ep in x.eps()]
        else:
            data["parsed"] = False
            
        return data


with jsonlines.open(sys.argv[2], mode='w') as writer:
    for line in open(sys.argv[1]).readlines():
        writer.write(parse(line))
