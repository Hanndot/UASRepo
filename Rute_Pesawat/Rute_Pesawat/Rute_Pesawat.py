graph = {'a':{'b':4,'c':3},'b':{'a':4,'e':12,'f':5},'c':{'a':3,'d':7,'e':10},'d':{'c':7,'e':2},'e':{'b':12,'c':10,'d':2,'g':5},'f':{'b':5,'g':16},'g':{'e':5,'f':16}}
 
def alg(graph,asal,tujuan):
    jarak_terpendek = {}
    preD = {}
    unseenNodes = graph
    infinity = float('inf')
    path = []
    for node in unseenNodes:
        jarak_terpendek[node] = infinity
    jarak_terpendek[asal] = 0
 
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif jarak_terpendek[node] < jarak_terpendek[minNode]:
                minNode = node
 
        for childNode, weight in graph[minNode].items():
            if weight + jarak_terpendek[minNode] < jarak_terpendek[childNode]:
                jarak_terpendek[childNode] = weight + jarak_terpendek[minNode]
                preD[childNode] = minNode
        unseenNodes.pop(minNode)
 
    currentNode = tujuan
    while currentNode != asal:
        try:
            path.insert(0,currentNode)
            currentNode = preD[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,asal)
    if jarak_terpendek[tujuan] != infinity:
        print('Jaraknya ' + str(jarak_terpendek[tujuan]) + ' m')
        print('Jalurnya melewati  ' + str(path))

print('Daftar Wahana:')
print('a. Kandang Harimau\nb. Kandang Singa\nc. Kandang Gajah\nd. Kandang Panda\ne. Kandang Jerapah\nf. Kandang Beruang\ng. Kandang Llama')
print('')
x = input('Asal: ')
y = input('Tujuan: ')
alg(graph, x, y)
