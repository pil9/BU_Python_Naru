import sys
import webbrowser
import urllib.request
# import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QCoreApplication
from naru import TripAnalyzer
import datetime



main_ui = uic.loadUiType('screen1.ui')[0]
engine = TripAnalyzer()
engine.set_model()



#여행 계획 입력
class OptionWindow1(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow1, self).__init__(parent)
        option_ui = 'long.ui'
        uic.loadUi(option_ui, self)
        self.show()

        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("images/sentence.png")
        self.bgimg.setPixmap(self.qPixmapFileVar)

        
        self.userlabel.setText(username+"님의")
        
        self.textlong.setPlaceholderText("ex - 올 겨울에 친구 3명과 함께 2박 3일로 여행을 갈 거야.")
        self.nextbtn.clicked.connect(self.clicked_option)
        
        #상단바 이름+아이콘 설정
        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))


    def clicked_option(self):
        global sentence #여행 관련 데이터 입력
        sentence = self.textlong.text()
        engine.set_sentence(sentence)
        engine.run_model()
        print(engine.result)
        OptionWindow2(self)



#살고 있는 지역 버튼 클릭
class OptionWindow2(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow2, self).__init__(parent)
        option_ui = 'imagetext.ui'
        uic.loadUi(option_ui, self)
        self.show()
        
        # self.textimage.setPlaceholderText("ex - 여행, 가방, 배낭여행, 면세점")
        # self.qPixmapFileVar = QPixmap()
        # self.qPixmapFileVar.load("images/image.png")
        # self.labelpic.setPixmap(self.qPixmapFileVar)

        
        self.userlabel.setText(username+"님은")

        #지역 버튼 클릭 시 다음 페이지로 이동
        self.pushButton_2.clicked.connect(self.clicked_option)
        self.pushButton_3.clicked.connect(self.clicked_option)
        self.pushButton_4.clicked.connect(self.clicked_option)
        self.pushButton_5.clicked.connect(self.clicked_option)
        self.pushButton_6.clicked.connect(self.clicked_option)
        self.pushButton_7.clicked.connect(self.clicked_option)
        self.pushButton_8.clicked.connect(self.clicked_option)
        self.pushButton_9.clicked.connect(self.clicked_option)
        self.pushButton_10.clicked.connect(self.clicked_option)
        self.pushButton_11.clicked.connect(self.clicked_option)
        self.pushButton_12.clicked.connect(self.clicked_option)
        self.pushButton_13.clicked.connect(self.clicked_option)
        self.pushButton_14.clicked.connect(self.clicked_option)
        self.pushButton_15.clicked.connect(self.clicked_option)
        self.pushButton_16.clicked.connect(self.clicked_option)
        self.pushButton_17.clicked.connect(self.clicked_option)



        #상단바 이름+아이콘 설정
        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))
        
    def clicked_option(self):
        # global image
        # image = self.textimage.text()
        # print(image)
        OptionWindow3(self)



#추천 여행지
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

        #Pixmap사용
        self.qPixmapFileVar = QPixmap()

        #결과 화면에서 고정으로 사용되는 배경 이미지
        self.qPixmapFileVar.load("images/jeju.png")
        self.bgimg.setPixmap(self.qPixmapFileVar)

        #DB에서 해당 여행지의 이미지 주소를 불러옴
        url=result['image']
        image=urllib.request.urlopen(url).read()
        self.qPixmapFileVar.loadFromData(image)
        self.labelpic.setPixmap(self.qPixmapFileVar)

        #상단바 이름+아이콘 설정
        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))

        self.userlabel.setText(username+"님께")
        self.namelabel.setText("'"+result['name']+"'")
        self.addlabel.setText(result['full_addr'])
        self.taglabel.setText(result['tag'])
        self.infolabel.setText(result['info'])
    
        #다른 여행지도 볼 수 있는 페이지로 이동
        self.otherbtn_2.clicked.connect(self.clicked_option)

        #오늘 날짜+여행지 지역 받아와서 숙박 예약 url로 이동
        today0 = datetime.date.today()        
        today = today0.strftime('%Y-%m-%d')
        roomurl="www.dailyhotel.com/search/stays/results?dateCheckIn="+today+"&stays=1&term="+result['short_addr']+"&title="+result['short_addr']
        self.roombtn_2.clicked.connect(lambda: webbrowser.open(roomurl))

        #지도 url로 이동
        self.trafficbtn_2.clicked.connect(lambda: webbrowser.open('https://map.kakao.com/'))

    def clicked_option(self):
        OptionWindow4(self)



#여행지 목록
class OptionWindow4(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow4, self).__init__(parent)
        option_ui = 'scroll.ui'
        uic.loadUi(option_ui, self)

        # 여행지 이미지 가져오기
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("images/jjlabel.png")
        self.jjlabel.setPixmap(self.qPixmapFileVar)
        self.qPixmapFileVar.load("images/pclabel.png")
        self.pclabel.setPixmap(self.qPixmapFileVar)
        self.qPixmapFileVar.load("images/pslabel.png")
        self.pslabel.setPixmap(self.qPixmapFileVar)
        self.qPixmapFileVar.load("images/sulabel.png")
        self.sulabel.setPixmap(self.qPixmapFileVar)
        self.qPixmapFileVar.load("images/yslabel.png")
        self.yslabel.setPixmap(self.qPixmapFileVar)
        self.qPixmapFileVar.load("images/djlabel.png")
        self.djlabel.setPixmap(self.qPixmapFileVar)

        #버튼 클릭 시 해당 지역 관광공사 url로 이동
        self.jjbtn.clicked.connect(lambda: webbrowser.open('https://www.visitjeju.net/kr'))
        self.pcbtn.clicked.connect(lambda: webbrowser.open('http://tour.pc.go.kr/'))
        self.psbtn.clicked.connect(lambda: webbrowser.open('https://bto.or.kr/kor/Main.do'))
        self.subtn.clicked.connect(lambda: webbrowser.open('https://korean.visitseoul.net/index'))
        self.ysbtn.clicked.connect(lambda: webbrowser.open('https://www.yeosu.go.kr/tour'))
        self.djbtn.clicked.connect(lambda: webbrowser.open('https://www.daejeon.go.kr/tou/index.do'))

        #상단바 이름+아이콘 설정
        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))
    
        self.show()



#인트로
class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #인트로 배경화면
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("images/intro.png")
        self.labelpic.setPixmap(self.qPixmapFileVar)  
        
        #상단바 이름+아이콘 설정
        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))
        
        self.label_3.setText = ("intro")
        self.textstart.setPlaceholderText("이름을 입력하세요.")
        self.nextbtn.clicked.connect(self.clicked_option)

    def clicked_option(self):
        global username #사용자 이름 입력
        username = self.textstart.text()
        OptionWindow1(self)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainWindow()
    main_dialog.show()
    app.exec_()
