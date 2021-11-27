import sys
import webbrowser
import urllib.request
# import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QCoreApplication
from naru import TripAnalyzer
import datetime

main_ui = uic.loadUiType('screen1.ui')[0]
engine = TripAnalyzer()
engine.set_model()

class OptionWindow1(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow1, self).__init__(parent)
        option_ui = 'long.ui'
        uic.loadUi(option_ui, self)
        self.show()
        
        self.textlong.setPlaceholderText("ex - 올 겨울에 친구 3명과 함께 2박 3일로 여행을 갈 거야.")
        self.nextbtn.clicked.connect(self.clicked_option)
        
        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))


    def clicked_option(self):
        global sentence #여행 관련 데이터 입력
        sentence = self.textlong.text()
        engine.set_sentence(sentence)
        engine.run_model()
        print(engine.result)
        OptionWindow2(self)
        
class OptionWindow2(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow2, self).__init__(parent)
        option_ui = 'imagetext.ui'
        uic.loadUi(option_ui, self)
        self.show()
        
        self.textimage.setPlaceholderText("ex - 여행, 가방, 배낭여행, 면세점")
        self.nextbtn.clicked.connect(self.clicked_option)
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("images/image.png")
        self.labelpic.setPixmap(self.qPixmapFileVar)
        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))
        
    def clicked_option(self):
        global image
        image = self.textimage.text()
        print(image)
        OptionWindow3(self)
        
class OptionWindow3(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow3, self).__init__(parent)
        option_ui = 'screen2.ui'
        uic.loadUi(option_ui, self)
        self.show()
        
        engine.result_analyzing()
        engine.lookup_db_index()
        index=engine.recommand_analyzing()
        result=engine.lookup_db_data(index)

        self.qPixmapFileVar = QPixmap()



        url=result['image']
        image=urllib.request.urlopen(url).read()
        self.qPixmapFileVar.loadFromData(image)
        self.labelpic.setPixmap(self.qPixmapFileVar)

        
        self.qPixmapFileVar.load("images/jeju.png")
        self.bgimg.setPixmap(self.qPixmapFileVar)

        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))



        self.namelabel.setText(result['name'])
        self.addlabel.setText(result['full_addr'])
        self.taglabel.setText(result['tag'])
        self.infolabel.setText(result['info'])

    
        self.otherbtn_2.clicked.connect(self.clicked_option)


        today0 = datetime.date.today()        
        today = today0.strftime('%Y-%m-%d')
        roomurl="www.dailyhotel.com/search/stays/results?dateCheckIn="+today+"&stays=1&term="+result['short_addr']+"&title="+result['short_addr']

        self.roombtn_2.clicked.connect(lambda: webbrowser.open(roomurl))
        self.trafficbtn_2.clicked.connect(lambda: webbrowser.open('https://map.kakao.com/'))

    def clicked_option(self):
        OptionWindow4(self)

class OptionWindow4(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow4, self).__init__(parent)
        option_ui = 'scroll.ui'
        uic.loadUi(option_ui, self)
                

        # 여행지 이미지
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("images/jjlabel.png")
        self.jjlabel.setPixmap(self.qPixmapFileVar)
        self.qPixmapFileVar.load("images/pclabel.png")
        self.pclabel.setPixmap(self.qPixmapFileVar)
        self.pushButton_2.setPixmap(self.qPixmapFileVar)
        self.qPixmapFileVar.load("images/pslabel.png")
        self.pslabel.setPixmap(self.qPixmapFileVar)
        self.qPixmapFileVar.load("images/sulabel.png")
        self.sulabel.setPixmap(self.qPixmapFileVar)
        self.qPixmapFileVar.load("images/yslabel.png")
        self.yslabel.setPixmap(self.qPixmapFileVar)
        self.qPixmapFileVar.load("images/djlabel.png")
        self.djlabel.setPixmap(self.qPixmapFileVar)

        # self.pushButton.clicked.connect(lambda: webbrowser.open('http://tour.pc.go.kr/'))
        # self.pushButton_2.clicked.connect(lambda: webbrowser.open('http://tour.pc.go.kr/'))

        # self.jjlabel.clicked.connect(lambda: webbrowser.open('https://www.visitjeju.net/kr'))
        # self.jjlabel2.clicked.connect(lambda: webbrowser.open('https://www.visitjeju.net/kr'))
        # self.pclabel.clicked.connect(lambda: webbrowser.open('http://tour.pc.go.kr/'))
        # self.pclabel2.clicked.connect(lambda: webbrowser.open('http://tour.pc.go.kr/'))
        # self.pslabel.clicked.connect(lambda: webbrowser.open('https://bto.or.kr/kor/Main.do'))
        # self.pslabel2.clicked.connect(lambda: webbrowser.open('https://bto.or.kr/kor/Main.do'))
        # self.sulabel.clicked.connect(lambda: webbrowser.open('https://korean.visitseoul.net/index'))
        # self.sulabel2.clicked.connect(lambda: webbrowser.open('https://korean.visitseoul.net/index'))
        # self.yslabel.clicked.connect(lambda: webbrowser.open('https://www.yeosu.go.kr/tour'))
        # self.yslabel2.clicked.connect(lambda: webbrowser.open('https://www.yeosu.go.kr/tour'))
        # self.djlabel.clicked.connect(lambda: webbrowser.open('https://www.daejeon.go.kr/tou/index.do'))
        # self.djlabel2.clicked.connect(lambda: webbrowser.open('https://www.daejeon.go.kr/tou/index.do'))

        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))
    
        self.show()

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
                
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("images/intro.png")
        self.labelpic.setPixmap(self.qPixmapFileVar)    
        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))
        
        self.label_3.setText = ("intro")
        self.textstart.setPlaceholderText("이름을 입력하세요.")
        self.nextbtn.clicked.connect(self.clicked_option)

    def clicked_option(self):
        global name #사용자 이름 입력 ㅋㅋ
        name = self.textstart.text()
        OptionWindow1(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainWindow()
    main_dialog.show()
    app.exec_()
