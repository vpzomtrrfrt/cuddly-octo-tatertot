#!/usr/bin/env python2
import urllib2, sys, random, subprocess
def run(args):
	if len(args) > 0:
		num = str(args[0])
	else:
		num = str(random.randrange(1, 650))
	num = (3-len(num))*"0"+num
	try:
		f = urllib2.urlopen("http://bulbapedia.bulbagarden.net/wiki/File:"+num+".png")
	except:
		f = urllib2.urlopen("http://bulbapedia.bulbagarden.net/wiki/File:"+num+"MS.png")
	L = f.readlines()
	f.close()
	for l in L:
		ind = l.find("fullImageLink")
		if ind > -1:
			ind+=34
			url = l[ind:l.find('"', ind)]
		ind = l.find("sprite of")
		if ind > -1:
			ind = l.find(">",ind)+1
			pname = l[ind:l.find("<",ind)]
	subprocess.Popen(["display", "-sample", "400x400", "-title", pname+" (#"+num+")", url])
if __name__ == "__main__":
	run(sys.argv[1:])
