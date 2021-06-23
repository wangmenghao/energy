from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys, csv
from energydiagram import ED
from matplotlib import pyplot as plt
import pandas as pd
class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("选择文件")
        self.myButton.clicked.connect(self.msg)
        self.myButton.setStyleSheet("QPushButton{font-family:'宋体';font-size:20px;}")

    def msg(self):

        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                    "选择文件",
                                    "./",
                                    "All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔

        
        diagram = ED()

        df = pd.read_csv(fileName1)

        max_location = df['location'].max()

        for index, row in df.iterrows():
            if 'color' in df:
                diagram.add_level(energy = row['energies'], bottom_text = row['name'], color = row['color'])
            if 'color' not in df:
                diagram.add_level(energy = row['energies'], bottom_text = row['name'])
            if (row['location']) < max_location:
                diagram.add_link(row['location'] - 1, row['location'])
        diagram.plot(show_IDs=False)
        plt.show()
        
if __name__=="__main__":  
    import sys  
  
    app=QtWidgets.QApplication(sys.argv)  
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())  