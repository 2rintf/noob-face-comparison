import sys
import cv2 as cv
from PyQt5.Qt import QApplication,QMainWindow,QFileDialog,QImage,QPixmap
from Gui_qt.mainwindow import Ui_MainWindow
# slot函数修饰符使用
from PyQt5.Qt import pyqtSlot
import face_list_compare_func as flcf
from Gui_qt.CallDialogForAddFace import MyDialogWindow


class MyMainWindow(QMainWindow,Ui_MainWindow):


    def __init__(self):
        super(MyMainWindow,self).__init__()
        # 把ui布局加载
        self.setupUi(self)
        self.upload_img_path = ""



    '''
    pyqt的槽函数必须加修饰符，否则会重复执行两次.
    记得导入pyqtSlot.
    '''

    @pyqtSlot()
    def on_selectBtn_clicked(self):
        print("select pic.")
        # 注意用双分号间隔多种后缀名。
        # 如果采用下面这种写法，那么括号中不同的后缀名用空格隔开即可。
        fileName, fileType = QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         "..",
                                                         "Image Files(*.jpg *.png)")

        print(fileName)
        print(fileType)

        if fileName=="":
            print("Null file name.")
        else:
            self.upload_img_path = fileName


            img_cv = cv.imread(self.upload_img_path)
            img_qt = cv.cvtColor(img_cv,cv.COLOR_BGR2RGB)
            img_qt = cv.resize(img_qt,(self.selectedPic.width(),self.selectedPic.height()))
            height, width, depth = img_qt.shape
            img_qt = QImage(img_qt.data,width,height,depth*width,QImage.Format_RGB888)
            # self.selectedPic.setScaledContents(True)
            self.selectedPic.setPixmap(QPixmap.fromImage(img_qt))


    @pyqtSlot()
    def on_matchBtn_clicked(self):
        print("start match.")
        print(self.upload_img_path)
        # 注意此处的相对路径问题，要退回上一级目录，所以用"../"。
        result_filae_path = flcf.compare_face_on_json(self.upload_img_path,"../data_pic/1870_face_encoding.json")
        print(result_filae_path)

    @pyqtSlot()
    def on_addBtnTest_clicked(self):
        dialog = MyDialogWindow()
        result = dialog.exec()
        print(result)
        print(dialog.addedFace["new_face"])

if  __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())