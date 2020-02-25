import sys
import cv2 as cv
from PyQt5.Qt import *
# from Gui_qt.mainwindow import Ui_MainWindow
# slot函数修饰符使用
from PyQt5.Qt import pyqtSlot
import face_list_compare_func as flcf
from Gui_qt.dialogforaddnewface import Ui_DialogForAddNewFace



class MyDialogWindow(QDialog,Ui_DialogForAddNewFace):


    def __init__(self):
        super(MyDialogWindow,self).__init__()
        # 把ui布局加载
        self.setupUi(self)
        self.ageEdit.setValidator(QIntValidator())
        self.ageEdit.setMaxLength(3)
        self.phoneEdit.setValidator(QIntValidator())





        # todo: 输入框内容格式限制

        self.addedFace = {"new_face":
                            {"name":"",
                             "sex":"",
                             "age":0,
                             "phone":0,
                             "email":"",
                             "face_encoding":[],
                             "face_pic_path":""
                             }}



    # @staticmethod
    # def static_try():
    #     print("static test")

    '''
    pyqt的槽函数必须加修饰符，否则会重复执行两次.
    记得导入pyqtSlot.
    '''

    @pyqtSlot()
    def buttonBox_clicked(self):
        # print(self.buttonBox.clicked())
        print("button box test")
        # MyDialogWindow.static_try()

        print(self.buttonBox.getContentsMargins())

        print(QPushButton(QDialogButtonBox.button(self.buttonBox,QDialogButtonBox.Ok)))

        print("--------------")
        # print(button)
        print("--------------")

    @pyqtSlot()
    def on_selectNewFaceBtn_clicked(self):
        print("select pic.")
        # 注意用双分号间隔多种后缀名。
        # 如果采用下面这种写法，那么括号中不同的后缀名用空格隔开即可。
        fileName, fileType = QFileDialog.getOpenFileName(self,
                                                         "选取文件",
                                                         "..",
                                                         "Image Files(*.jpg *.png)")

        print(fileName)
        print(fileType)

        if fileName == "":
            print("Null file name.")
        else:
            self.addedFace["new_face"]["face_pic_path"] = fileName

            print(self.addedFace["new_face"]["face_pic_path"])

            img_cv = cv.imread(fileName)
            img_qt = cv.cvtColor(img_cv, cv.COLOR_BGR2RGB)
            img_qt = cv.resize(img_qt, (self.selectedPicShow.width(), self.selectedPicShow.height()))
            height, width, depth = img_qt.shape
            img_qt = QImage(img_qt.data, width, height, depth * width, QImage.Format_RGB888)
            # self.selectedPic.setScaledContents(True)
            self.selectedPicShow.setPixmap(QPixmap.fromImage(img_qt))




