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
        self.setWindowTitle("相似人脸匹配demo---By zd_Chen")
        self.upload_img_path = ""
        self.five_best_results = ""



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
        # todo：解决数据库路径是否可由用于选择的问题
        result_file_path = flcf.compare_face_on_json(self.upload_img_path,"../data_pic/3000_face_encoding_v2.json")
        print(result_file_path)

        #todo:读取结果文件，展示前5名的图片与信息
        self.five_best_results = flcf.read_result_from_json(result_file_path, "../data_pic/3000_face_encoding_v2.json")
        print(self.five_best_results)
        # for one_result in five_best_results:
        #     # 此处注意相对路径，所以要在读到的路径上再返回上一层。
        #     img_cv = cv.imread("."+one_result[0])
        #     img_qt = cv.cvtColor(img_cv, cv.COLOR_BGR2RGB)
        #
        #     img_qt = cv.resize(img_qt, (self.matched_pic1.width(), self.selectedPic.height()))
        #     height, width, depth = img_qt.shape
        #     img_qt = QImage(img_qt.data, width, height, depth * width, QImage.Format_RGB888)
        #     # self.selectedPic.setScaledContents(True)
        #     self.selectedPic.setPixmap(QPixmap.fromImage(img_qt))

    # @pyqtSlot()
    # def on_firstBtn_clicked(self):
    #
    #     return
    #
    #
    # @pyqtSlot()
    # def on_secondBtn_clicked(self):
    #
    #
    #
    #     return
    #
    # @pyqtSlot()
    # def on_thirdBtn_clicked(self):
    #     return
    #
    #
    # @pyqtSlot()
    # def on_fourthBtn_clicked(self):
    #     return
    #
    #
    # @pyqtSlot()
    # def on_fifthBtn_clicked(self):
    #     return
    #


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