import sys
import os
import networkx as net
import urllib

def read_lj_friends(g, name):
    # Fetch the friends list from LiveJournal
    response=urllib.urlopen('http://www.livejournal.com/misc/fdata.bml?user='+name)
    # walk through the lines in the response and add each one as an edge in a network
    for line in response.readlines():
        # Comments in the response start with a '#'
        if line.startswith('#'): continue
        # the format is "< name" (incoming) or "> name" (outgoing)
        # make sure we don't have an  empty line
        parts=line.split()
        if len(parts)==0: continue
        # add the edge to the network
        if parts[0]=='<':
            g.add_edge(parts[1],name)
        else:
            g.add_edge(name,parts[1])

def snowball_sampling(g, center, max_depth=1, current_depth=0, taboo_list=[]):
    print center, current_depth, max_depth
    if current_depth==max_depth:
        print 'out of depth'
        return taboo_list
    if center in taboo_list:
        return taboo_list
    else:
        taboo_list.append(center) # we shall never return to the same node
    read_lj_friends(g,center) # call LiveJournal API and get data for node
    for node in g.neighbors(center):
        taboo_list=snowball_sampling(g, node, current_depth=current_depth+1,max_depth=max_depth, taboo_list=taboo_list)
    return taboo_list

g=net.Graph()
# read_lj_friends(g,'valerois')
# net.draw(g)
name='valerois'
max_depth=3
snowball_sampling(g,name,max_depth=max_depth)
print len(g)
net.write_pajek(g, name+'.net')
