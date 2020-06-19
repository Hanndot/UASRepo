import wpf

from System.Windows import Application, Window, MessageBox

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'test.xaml')

    class alg(object):
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
                MessageBox.Show('Tidak Ada Jalan')
                break
        path.insert(0,asal)
        if jarak_terpendek[tujuan] != infinity:
            MessageBox.Show('Jaraknya ' + str(jarak_terpendek[tujuan]) + ' m')
            MessageBox.Show('Jalurnya melewati  ' + str(path))



    def button_Click(self, sender, e):
        if self.combo1.Text == "" or self.combo2.Text == "":
            MessageBox.Show("Belum Diisi")
        else:
            if self.combo1.Text == self.combo1.Items.GetItemAt(0).ToString():
                x = 'a'
            elif self.combo1.Text == self.combo1.Items.GetItemAt(1).ToString():
                x = 'b'
            elif self.combo1.Text == self.combo1.Items.GetItemAt(2).ToString():
                x = 'c'
            elif self.combo1.Text == self.combo1.Items.GetItemAt(3).ToString():
                x = 'd'
            elif self.combo1.Text == self.combo1.Items.GetItemAt(4).ToString():
                x = 'e'
            elif self.combo1.Text == self.combo1.Items.GetItemAt(5).ToString():
                x = 'f'
            elif self.combo1.Text == self.combo1.Items.GetItemAt(6).ToString():
                x = 'g'
            elif self.combo2.Text == self.combo2.Items.GetItemAt(0).ToString():
                y = 'a'
            elif self.combo2.Text == self.combo2.Items.GetItemAt(1).ToString():
                y = 'b'    
            elif self.combo2.Text == self.combo2.Items.GetItemAt(2).ToString():
                y = 'c'    
            elif self.combo2.Text == self.combo2.Items.GetItemAt(3).ToString():
                y = 'd'    
            elif self.combo2.Text == self.combo2.Items.GetItemAt(4).ToString():
                y = 'e'    
            elif self.combo2.Text == self.combo2.Items.GetItemAt(5).ToString():
                y = 'f'    
            elif self.combo2.Text == self.combo2.Items.GetItemAt(6).ToString():
                y = 'g'
            alg(graph, x, y)
        pass

if __name__ == '__main__':
    Application().Run(MyWindow())
