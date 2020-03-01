import sys
import cv2 as cv
from PyQt5.Qt import QApplication,QMainWindow,QFileDialog,QImage,QPixmap
from Gui_qt.mainwindow import Ui_MainWindow
# slot函数修饰符使用
from PyQt5.Qt import pyqtSlot
import face_list_compare_func as flcf
from Gui_qt.CallDialogForAddFace import MyDialogWindow
import json
# import shutil

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

            # 清空结果信息展示
            self.five_best_results=""
            self.nameShow.clear()
            self.sexShow.clear()
            self.ageShow.clear()
            self.phoneShow.clear()
            self.emailShow.clear()
            self.matchedPicShow.clear()


    @pyqtSlot()
    def on_matchBtn_clicked(self):
        print("start match.")
        print(self.upload_img_path)
        # 注意此处的相对路径问题，要退回上一级目录，所以用"../"。
        # todo：解决数据库路径是否可由用于选择的问题
        result_file_path = flcf.compare_face_on_json(self.upload_img_path,"../data_pic/3000_face_encoding_v2.json")
        print(result_file_path)

        #读取结果文件，展示前5名的图片与信息
        self.five_best_results = flcf.read_result_from_json(result_file_path, "../data_pic/3000_face_encoding_v2.json")
        print(self.five_best_results)

        # 图像显示
        img_cv = cv.imread("." + self.five_best_results[0]['pic_path'])
        img_qt = cv.cvtColor(img_cv, cv.COLOR_BGR2RGB)

        img_qt = cv.resize(img_qt, (self.matchedPicShow.width(), self.matchedPicShow.height()))
        height, width, depth = img_qt.shape
        img_qt = QImage(img_qt.data, width, height, depth * width, QImage.Format_RGB888)
        # self.selectedPic.setScaledContents(True)
        self.matchedPicShow.setPixmap(QPixmap.fromImage(img_qt))

        #第一名信息显示
        self.nameShow.setText(self.five_best_results[0]['name'])
        self.sexShow.setText(self.five_best_results[0]['sex'])
        self.ageShow.setText(str(self.five_best_results[0]['age']))
        self.phoneShow.setText(str(self.five_best_results[0]['phone']))
        self.emailShow.setText(self.five_best_results[0]['email'])



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

    @pyqtSlot()
    def on_firstBtn_clicked(self):
        # 图像显示
        img_cv = cv.imread("." + self.five_best_results[0]['pic_path'])
        img_qt = cv.cvtColor(img_cv, cv.COLOR_BGR2RGB)

        img_qt = cv.resize(img_qt, (self.matchedPicShow.width(), self.matchedPicShow.height()))
        height, width, depth = img_qt.shape
        img_qt = QImage(img_qt.data, width, height, depth * width, QImage.Format_RGB888)
        # self.selectedPic.setScaledContents(True)
        self.matchedPicShow.setPixmap(QPixmap.fromImage(img_qt))

        # 第一名信息显示
        self.nameShow.setText(self.five_best_results[0]['name'])
        self.sexShow.setText(self.five_best_results[0]['sex'])
        self.ageShow.setText(str(self.five_best_results[0]['age']))
        self.phoneShow.setText(str(self.five_best_results[0]['phone']))
        self.emailShow.setText(self.five_best_results[0]['email'])



    @pyqtSlot()
    def on_secondBtn_clicked(self):
        # 图像显示
        img_cv = cv.imread("." + self.five_best_results[1]['pic_path'])
        img_qt = cv.cvtColor(img_cv, cv.COLOR_BGR2RGB)

        img_qt = cv.resize(img_qt, (self.matchedPicShow.width(), self.matchedPicShow.height()))
        height, width, depth = img_qt.shape
        img_qt = QImage(img_qt.data, width, height, depth * width, QImage.Format_RGB888)
        # self.selectedPic.setScaledContents(True)
        self.matchedPicShow.setPixmap(QPixmap.fromImage(img_qt))

        # 第一名信息显示
        self.nameShow.setText(self.five_best_results[1]['name'])
        self.sexShow.setText(self.five_best_results[1]['sex'])
        self.ageShow.setText(str(self.five_best_results[1]['age']))
        self.phoneShow.setText(str(self.five_best_results[1]['phone']))
        self.emailShow.setText(self.five_best_results[1]['email'])

    @pyqtSlot()
    def on_thirdBtn_clicked(self):
        # 图像显示
        img_cv = cv.imread("." + self.five_best_results[2]['pic_path'])
        img_qt = cv.cvtColor(img_cv, cv.COLOR_BGR2RGB)

        img_qt = cv.resize(img_qt, (self.matchedPicShow.width(), self.matchedPicShow.height()))
        height, width, depth = img_qt.shape
        img_qt = QImage(img_qt.data, width, height, depth * width, QImage.Format_RGB888)
        # self.selectedPic.setScaledContents(True)
        self.matchedPicShow.setPixmap(QPixmap.fromImage(img_qt))

        # 第一名信息显示
        self.nameShow.setText(self.five_best_results[2]['name'])
        self.sexShow.setText(self.five_best_results[2]['sex'])
        self.ageShow.setText(str(self.five_best_results[2]['age']))
        self.phoneShow.setText(str(self.five_best_results[2]['phone']))
        self.emailShow.setText(self.five_best_results[2]['email'])


    @pyqtSlot()
    def on_fourthBtn_clicked(self):
        # 图像显示
        img_cv = cv.imread("." + self.five_best_results[3]['pic_path'])
        img_qt = cv.cvtColor(img_cv, cv.COLOR_BGR2RGB)

        img_qt = cv.resize(img_qt, (self.matchedPicShow.width(), self.matchedPicShow.height()))
        height, width, depth = img_qt.shape
        img_qt = QImage(img_qt.data, width, height, depth * width, QImage.Format_RGB888)
        # self.selectedPic.setScaledContents(True)
        self.matchedPicShow.setPixmap(QPixmap.fromImage(img_qt))

        # 第一名信息显示
        self.nameShow.setText(self.five_best_results[3]['name'])
        self.sexShow.setText(self.five_best_results[3]['sex'])
        self.ageShow.setText(str(self.five_best_results[3]['age']))
        self.phoneShow.setText(str(self.five_best_results[3]['phone']))
        self.emailShow.setText(self.five_best_results[3]['email'])


    @pyqtSlot()
    def on_fifthBtn_clicked(self):
        # 图像显示
        img_cv = cv.imread("." + self.five_best_results[4]['pic_path'])
        img_qt = cv.cvtColor(img_cv, cv.COLOR_BGR2RGB)

        img_qt = cv.resize(img_qt, (self.matchedPicShow.width(), self.matchedPicShow.height()))
        height, width, depth = img_qt.shape
        img_qt = QImage(img_qt.data, width, height, depth * width, QImage.Format_RGB888)
        # self.selectedPic.setScaledContents(True)
        self.matchedPicShow.setPixmap(QPixmap.fromImage(img_qt))

        # 第一名信息显示
        self.nameShow.setText(self.five_best_results[4]['name'])
        self.sexShow.setText(self.five_best_results[4]['sex'])
        self.ageShow.setText(str(self.five_best_results[4]['age']))
        self.phoneShow.setText(str(self.five_best_results[4]['phone']))
        self.emailShow.setText(self.five_best_results[4]['email'])



    @pyqtSlot()
    def on_addBtnTest_clicked(self):
        dialog = MyDialogWindow()
        result = dialog.exec()
        print(result)
        print(dialog.addedFace["new_face"])
        if result:
            temp_dict = dialog.addedFace["new_face"]

            try:
                fs = open("../data_pic/3000_face_encoding_v2.json", 'r')
            except OSError:
                return "File open error!"
            total_dict = json.load(fs)
            fs.close()
            index = total_dict.__len__()
            temp_dict['index'] = index + 1
            total_dict[str(index+1)] = temp_dict.copy()

            try:
                fs = open("../data_pic/3000_face_encoding_v2.json", 'w')
            except OSError:
                return "File open error!"
            new_json = json.dumps(total_dict, indent=4)
            fs.write(new_json)
            fs.close()





if  __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())