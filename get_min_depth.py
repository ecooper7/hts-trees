## ecooper 3/26/2017
## Get the minimum depth of a given label in a given dotfile for an HTS tree.
## This is mainly intended as an example of how to read in the dotfile to a
## tree structure in Python.
## This assumes that you have already created a dotfile out of the HTS tree.
## Scripts for tree->dotfile, by Heiga Zen, can be found here:
## http://hts.sp.nitech.ac.jp/hts-users/spool/2008/msg00157.html

import os
import pygraphviz
import networkx

label = 'yourlabelname'
dotfile = '/path/to/your/dotfile.dot'

g = pygraphviz.AGraph(dotfile, directed=True)
x = networkx.from_agraph(g)
d = networkx.to_dict_of_dicts(x)

parent = {}
for k, v in d.iteritems():
    children = v.keys()
    for c in children:
        if c in parent:
            print 'warning: ' + c + ' has a parent already: ' + parent[c]
        parent[c] = k
   
mynodes = [n for n in g.nodes() if n.attr['label'] == label]

depths = []
for n in mynodes:
    depth = 0
    p = str(n)
    while p != '0':
        p = parent[p]
        depth += 1
    depths.append(depth)

if depths == []:
    mymin = 'NONE'
else:
    mymin = str(min(depths))
print mymin

