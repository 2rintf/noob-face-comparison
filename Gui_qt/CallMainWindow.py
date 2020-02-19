import sys
from PyQt5.Qt import QApplication,QMainWindow
from Gui_qt.mainwindow import Ui_MainWindow
# slot函数修饰符使用
from PyQt5.Qt import pyqtSlot

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        # 把ui布局加载
        self.setupUi(self)


    '''
    pyqt的槽函数必须加修饰符，否则会重复执行两次.
    记得导入pyqtSlot.
    '''

    @pyqtSlot()
    def on_Btn1_clicked(self):
        print("Btn1 clicked.")

    @pyqtSlot()
    def on_Btn2_clicked(self):
        print("Btn2 clicked.")

if  __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())