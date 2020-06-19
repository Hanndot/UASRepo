import wpf

from System.Windows import Application, Window, MessageBox

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'test.xaml')


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
        pass

if __name__ == '__main__':
    Application().Run(MyWindow())
