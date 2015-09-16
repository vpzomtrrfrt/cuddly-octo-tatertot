#!/usr/bin/env python
import json, sys, pkmn, re, os.path
h = open(os.path.dirname(os.path.realpath(__file__))+"/pkmnlist.txt", 'r')
L = h.readlines()
h.close()
rgx = None
if len(sys.argv) > 1:
	if "/" in sys.argv[1]:
		rgx = sys.argv[1].replace('/','')
	for l in L:
		if sys.argv[1].lower() in l.lower() or (rgx and re.search(rgx, l.lower())):
			pkmn.run([l.split("|")[0]])
else:
	pkmn.run(())
