import os
import sys
import networkx as net
import matplotlib.pyplot as plot

print 'Reading retweets from Egypt'
e=net.read_pajek("C:\Development\python\SNABook-master\chapter1\egypt_retweets.net")
print 'Find connected components in network with '+str(len(e))+' nodes.'
nccs=net.connected_component_subgraphs(e)
print len(nccs)
x=[len(c) for c in net.connected_component_subgraphs(e)]
plot.hist(x)
plot.savefig("connected_comps_hist.png")
