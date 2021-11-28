import sys
import webbrowser
import urllib.request
import datetime
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore
from naru import TripAnalyzer



#메인 ui 지정
main_ui = uic.loadUiType('screen1.ui')[0]

#인공지능 불러옴
engine = TripAnalyzer()
engine.set_model()



#인트로: 사용자 이름 입력
class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #배경 이미지 설정
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("images/intro.png")
        self.labelpic.setPixmap(self.qPixmapFileVar)  
        
        #상단바 이름+아이콘 설정
        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))
        
        #LineEdit 텍스트 입력 가이드
        self.textstart.setPlaceholderText("이름을 입력하세요.")

        #버튼 클릭 이벤트 > 다음 페이지로 이동
        self.nextbtn.clicked.connect(self.clicked_option)

    def clicked_option(self):
        #사용자 이름 전역변수로 받음
        global username
        username = self.textstart.text()

        OptionWindow1(self)



#여행 계획 입력
class OptionWindow1(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow1, self).__init__(parent)
        option_ui = 'long.ui'
        uic.loadUi(option_ui, self)
        self.show()

        #배경 이미지 설정
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("images/sentence.png")
        self.bgimg.setPixmap(self.qPixmapFileVar)

        #전역변수로 받은 유저 이름 출력
        self.userlabel.setText(username+"님의")
        
        #LineEdit 텍스트 입력 가이드
        self.textlong.setPlaceholderText("ex - 올 겨울에 친구 3명과 함께 2박 3일로 여행을 갈 거야.")

        #버튼 클릭 이벤트 > 다음 페이지로 이동
        self.nextbtn.clicked.connect(self.clicked_option)
        
        #상단바 이름+아이콘 설정
        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))


    def clicked_option(self):
        #여행 계획 전역변수로 받음
        global sentence
        sentence = self.textlong.text()

        engine.set_sentence(sentence)
        engine.run_model()
        print(engine.result)

        OptionWindow2(self)



#거주 지역 선택
class OptionWindow2(QMainWindow):
    def __init__(self, parent):
        super(OptionWindow2, self).__init__(parent)
        option_ui = 'imagetext.ui'
        uic.loadUi(option_ui, self)
        self.show()
        
        #전역변수로 받은 유저 이름 출력
        self.userlabel.setText(username+"님은")

        #지역 버튼
        #버튼 클릭 이벤트 > 다음 페이지로 이동
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

        for line in result.items():
            print(line)
        
        #배경 이미지 설정
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("images/jeju.png")
        self.bgimg.setPixmap(self.qPixmapFileVar)

        #DB에서 해당 여행지의 이미지 주소를 불러옴
        url=result['image']
        image=urllib.request.urlopen(url).read()
        self.qPixmapFileVar.loadFromData(image)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(600)
        self.labelpic.setPixmap(self.qPixmapFileVar)

        #상단바 이름+아이콘 설정
        self.setWindowTitle('나루')
        self.setWindowIcon(QIcon('images/luggage.png'))

        #전역변수로 받은 유저 이름 출력
        self.userlabel.setText(username+"님께")

        #추천하는 여행지 정보 출력
        self.namelabel.setText("'"+result['name']+"'")      #여행지 이름
        self.addlabel.setText(result['full_addr'])          #여행지 주소
        self.taglabel.setText(result['tag'])                #여행지 키워드 태그
        self.infolabel.setText(result['info'])              #여행지 정보
    
        #[다른 여행지 보기] 버튼
        #버튼 클릭 이벤트 > 다음 페이지로 이동
        self.otherbtn_2.clicked.connect(self.clicked_option)

        #[교통편 찾아보기] 버튼
        #버튼 클릭 이벤트 > 지도 url로 이동
        self.trafficbtn_2.clicked.connect(lambda: webbrowser.open('https://map.kakao.com/'))

        #[숙박 찾아보기] 버튼
        #버튼 클릭 이벤트 > 오늘 날짜+여행지 지역 받아와서 숙박 예약 url로 이동
        today0 = datetime.date.today()        
        today = today0.strftime('%Y-%m-%d')
        roomurl="www.dailyhotel.com/search/stays/results?dateCheckIn="+today+"&stays=1&term="+result['short_addr']+"&title="+result['short_addr']
        self.roombtn_2.clicked.connect(lambda: webbrowser.open(roomurl))

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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainWindow()
    main_dialog.show()
    app.exec_()