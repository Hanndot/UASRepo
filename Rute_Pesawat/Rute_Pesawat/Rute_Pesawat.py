graph = {'a':{'b':982,'c':421,'d':1431,'e':923,'f':1416,'g':946},'b':{'a':982,'d':632},
         'c':{'a':421,'g':624},'d':{'a':1431,'b':632,'g':561},'e':{'a':923,'f':519},'f':{'a':1416,'e':519},'g':{'a':946,'c':624,'d':561}}
 
def alg(graph,start,goal):
    shortest_distance = {}
    preD = {}
    unseenNodes = graph
    infinity = float('inf')
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                preD[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = preD[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]) + ' km')
        print('And the path is ' + str(path))

print('Airport List:')
print('a. CGK\nb. DPS\nc. SRG\nd. UPG\ne. PDG\nf. MES\ng. BDJ')
print('')
x = input('Source: ')
y = input('Destination: ')
alg(graph, x, y)
