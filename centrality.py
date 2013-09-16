# Centrality: count the connections to the node
# node degree: connection counter

import os
import sys
import networkx as net
import matplotlib.pyplot as plot
import pylab

### This function returns a sorted degree list
### useful for celebrity spotting
def sorted_map(map):
	ms = sorted(map.iteritems(), key=lambda (k,v): (-v,k))
	return ms

### Remove pendant and isolated nodes from the graph
def trim_degrees(g, degree=1):
	print 'Show network for degree > ' + str(degree)
	filename = 'core' + str(degree) + '.png'
	g2=g.copy()
	d=net.degree(g2)
	for n in g2.nodes():
		if d[n]<=degree: g2.remove_node(n)
	net.draw(g2)
	plot.savefig(filename)
	plot.close()
	return g2

### Get Top10 list
def top(deg, toplist=10):
	print 'Sort the map to spot the celebrities'
	ds = sorted_map(deg)
	print 'and print the top '+str(toplist)
	print ds[0:toplist]
	return ds

	
inp_file='russians.net'
print 'Reading file '+inp_file
g = net.read_pajek(inp_file)
# Compute degree: number of connections to each node
print 'Get centrality by calculating connections to each node'
deg=net.degree(g)
ds=top(deg, toplist=15)
# Now find out how the degree is distributed
print 'Find how the degree is distributed'
h=plot.hist(deg.values(),100)
plot.savefig('centrality_hist.png')
plot.close()
# Reduce map by removing pendants and isolated nodes
print 'Remove pendants and isolated nodes'
core10=trim_degrees(g, degree=10)
core20=trim_degrees(g, degree=20)
core30=trim_degrees(g, degree=30)
# Calculate closeness for core30
print 'Calculate closeness for core30'
c=net.closeness_centrality(core30)
print 'Sort map'
top(c)
h=plot.hist(c.values(),100)
plot.savefig('hist_core30.png')
plot.close()
print 'Calculate closeness for core10'
c=net.closeness_centrality(core10)
print 'Sort map'
cs=top(c)
h=plot.hist(c.values(),100)
plot.savefig('hist_core10.png')
plot.close()
# Get betweenness
print 'Get betweenness centrality'
b30=net.betweenness_centrality(core30)
bs=sorted_map(b30)
b10=net.betweenness_centrality(core10)
bs=sorted_map(b10)
# Combine all information
print 'Combine all information'
names1=[x[0] for x in ds[:10]]
names2=[x[0] for x in cs[:10]]
names3=[x[0] for x in bs[:10]]
names=list((set(names1) | set(names2) | set(names3)))
table=[[name,deg[name],c[name],b10[name]] for name in names]
print table


