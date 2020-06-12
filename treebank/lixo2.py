from delphin.interfaces import ace
from delphin.mrs import simplemrs, mrx, dmrx, simpledmrs, eds

sent = 'A man is untying a shoe'
res  = ace.parse('/Users/ar/hpsg/ace/erg-2018-osx-0.9.30.dat', sent,
		 cmdargs = ['--timeout', '60', '--max-words', '150', '-n', '1',
			    '--max-chart-megabytes', '6000', '--max-unpack-megabytes', '6000',
			    '--rooted-derivations', '--udx', '--disable-generalization'])

if len(res['results']) > 0:
    x = res.result(0).mrs()
    root = x.ep(x.nodeid(x.index))
    print(root.pred)
    print(simplemrs.dumps([x], pretty_print=True, properties = False))
    print(simpledmrs.dumps([x], pretty_print=True))
    print(eds.dumps([x], pretty_print=True))
