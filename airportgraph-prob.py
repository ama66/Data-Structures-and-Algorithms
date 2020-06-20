## Q2 Ext H 


# Airport Connections

# You are given a list of airports (three-letter codes like 'JFK'), a list of routes 
# (one-way flights from one airport to another like ['JFK', 'SFO']), and a starting airport. 
# Write a function that returns the minimum number of airport connections (one-way flights) 
# that need to be added in order for someone to be able to reach any airport in the list, starting 
# at the starting airport. Note that the connections don't have to be direct; it's okay if an airport can 
# only be reached from the starting airport by stopping at other airports first.

# Sample input:
# [
#   "BGI",
#   "CDG",
#   "DEL",
#   "DOH",
#   "DSM",
#   "EWR",
#   "EYW",
#   "HND",
#   "ICN",
#   "JFK",
#   "LGA",
#   "LHR",
#   "ORD",
#   "SAN",
#   "SFO",
#   "SIN",
#   "TLV",
#   "BUD",
# ],
# [
#   ["DSM", "ORD"],
#   ["ORD", "BGI"],
#   ["BGI", "LGA"],
#   ["SIN", "CDG"],
#   ["CDG", "SIN"],
#   ["CDG", "BUD"],
#   ["DEL", "DOH"],
#   ["DEL", "CDG"],
#   ["TLV", "DEL"],
#   ["EWR", "HND"],
#   ["HND", "ICN"],
#   ["HND", "JFK"]
#   ["ICN", "JFK"],
#   ["JFK", "LGA"],
#   ["EYW", "LHR"],
#   ["LHR", "SFO"],
#   ["SFO", "SAN"],
#   ["SFO", "DSM"],
#   ["SAN", "EYW"],
# ],
# "LGA"
# Sample output: 3
# Find unreachable airports and give each one a score based on how many airports it can unlock once you get to
#it!  For example JFK is unreachable from LGA but it unlocks 0 other airports! 
# O(a * (a + r) + a + r + alog(a)) time | O(a + r) space - where a is the number of airports and r is the
# number of routes

class AirportNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.isReachable = True
        self.unreachableConnections = []


def airportConnections(airports, routes, startingAirport):
    ## build a graph for airports and connections
    airportGraph = createAirportGraph(airports, routes)
    ## find unreachable airports/Nodes
    print("starting @ airport ", startingAirport)
    print(" The following airports are unreachable")
    unreachableAirportNodes = getUnreachableAirportNodes(
        airportGraph, airports, startingAirport
    )
    for u in unreachableAirportNodes:
        print(u.airport)
    ## assign a score for each airport of the unreachables
    markUnreachableConnections(airportGraph, unreachableAirportNodes)
    ## now return minimum number of connections 
    return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)


# O(a + r) time | O(a + r) space
def createAirportGraph(airports, routes):
    airportGraph = {}
    for airport in airports:
        airportGraph[airport] = AirportNode(airport)
    for route in routes:
        airport, connection = route
        airportGraph[airport].connections.append(connection)
    return airportGraph


# O(a + r) time | O(a) space
def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
    visitedAirports = {}
    depthFirstTraverseAirports(airportGraph, startingAirport, visitedAirports)

    unreachableAirportNodes = []
    for airport in airports:
        if airport in visitedAirports:
            continue
        airportNode = airportGraph[airport]
        airportNode.isReachable = False
        unreachableAirportNodes.append(airportNode)
    return unreachableAirportNodes


def depthFirstTraverseAirports(airportGraph, airport, visitedAirports):
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    connections = airportGraph[airport].connections
    for connection in connections:
        depthFirstTraverseAirports(airportGraph, connection, visitedAirports)


# O(a * (a + r)) time | O(a) space
def markUnreachableConnections(airportGraph, unreachableAirportNodes):
    for airportNode in unreachableAirportNodes:
        airport = airportNode.airport
        unreachableConnections = []
        depthFirstAddUnreachableConnections(
            airportGraph, airport, unreachableConnections, {}
        )
        airportNode.unreachableConnections = unreachableConnections


def depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, visitedAirports):
    if airportGraph[airport].isReachable:
        return
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    unreachableConnections.append(airport)
    connections = airportGraph[airport].connections
    for connection in connections:
        depthFirstAddUnreachableConnections(
            airportGraph, connection, unreachableConnections, visitedAirports
        )


# O(alog(a) + a + r) time | O(1) space
def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes):
    ## loop over unreachableconnections starting with those with the highest number of unreachable connections
    ## increment newconnections number but mark all those unreachable connections as reachable (by virtue
    ## of connecting the representative unreachable connection)
    unreachableAirportNodes.sort(
        key=lambda airport: len(airport.unreachableConnections), reverse=True
    )
    print([(i.airport, len(i.unreachableConnections)) for i in unreachableAirportNodes])
    numberOfNewConnections = 0
    for airportNode in unreachableAirportNodes:
        if airportNode.isReachable:
            continue
        numberOfNewConnections += 1
        for connection in airportNode.unreachableConnections:
            airportGraph[connection].isReachable = True
    return numberOfNewConnections


starting @ airport  LGA
 The following airports are unreachable
BGI
CDG
DEL
DOH
DSM
EWR
EYW
HND
ICN
JFK
LHR
ORD
SAN
SFO
SIN
TLV
BUD
[('EYW', 7), ('LHR', 7), ('SAN', 7), ('SFO', 7), ('TLV', 6), ('DEL', 5), ('EWR', 4), ('CDG', 3), ('DSM', 3), ('HND', 3), ('SIN', 3), ('ICN', 2), ('ORD', 2), ('BGI', 1), ('DOH', 1), ('JFK', 1), ('BUD', 1)]

3


## to draw graph
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(routes)
plt.figure(figsize=(20,12))
nx.draw(G,cmap=None,with_labels=True,node_size=1000,node_color=None)
plt.show();
