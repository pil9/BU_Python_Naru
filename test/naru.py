from konlpy.tag import Kkma
import sqlite3
'''
[('겨울', 'NNG') - >일반명사
 ('에', 'JKM'),
 ('가족', 'NNG'),
 ('들', 'XSN'),
 ('과', 'JKO'),
 ('갈', 'VV'),
 ('ㄹ', 'ETD'),
 ('만하', 'VXA'),
 ('ㄴ', 'ETD'),
 ('풍경', 'NNG'),
 ('이', 'JKS'),
 ('좋', 'VA'), -> 형용사
 ('은', 'ETD'), -> 관형사형 전성어미
 전성 -> 용언의 어간에 붙어 다른 품사의 기능을 수행하게 하는 어미
 어간 -> 활용시 변하지 않는 부분
 ('여행지', 'NNG')]
'''
# k.pos(user_string)

class TripAnalyzer:
    def __init__(self):
        self.model = None
        self.sentence = str()
        self.result = list()
        self.analyzed = dict()
        self.tag_index = dict()
    '''Set to model with initial'''
    def set_model(self):
        self.model = Kkma()

    '''Input to user sentence about trip'''
    def set_sentence(self, user_string):
        self.sentence = user_string

    '''Run to Kkma NLP Lib '''
    def run_model(self):
        self.result = self.model.pos(self.sentence)

    '''Morphological classification by list'''
    def result_analyzing(self):
        NNG_list = list()
        VA_list = list()
        ETD_list = list()

        for task in self.result:
            if task[1] == 'NNG':
                # 일반명사
                NNG_list.append(task[0])

            elif task[1] == 'VA':
                # 형용사
                VA_list.append(task[0])

            elif task[1] == 'ETD':
                #관형사형 전성어미
                ETD_list.append(task[0])

            else:
                continue
        
        self.analyzed = dict(
            NNG=NNG_list,
            VA=VA_list,
            ETD=ETD_list
        )
            
        return self.analyzed

    def lookup_db_index(self):
        conn = sqlite3.connect("place.db")
        cur = conn.cursor()
        cur.execute('select 번호, 태그 from info')
        tag_index = cur.fetchall()
        for index in tag_index:
            try:
                self.tag_index[index[0]] = index[1].split(',')
            except AttributeError:
                self.tag_index[index[0]] = ['테스트']
            # self.tag_index[num][1] = index[1].split(',')

        conn.close()
        return self.tag_index

    def lookup_db_data(self, index):
        conn = sqlite3.connect("place.db")
        cur = conn.cursor()
        cur.execute("select * from info where 번호==?", [index])
        data = cur.fetchone()

        tag_label=""
        for tag in data[6].split(','):
            tag_label += '#'+tag+' '

        return dict(
            name = data[1],
            full_addr = data[2],
            info = data[3],
            image = data[4],
            short_addr = data[5],
            tag = tag_label
        )
        
    def recommand_analyzing(self):
        ''''''
        match_cnt = 0
        last_match_cnt = 0
        last_match_index = 0
        for index in self.tag_index:
            for tag in self.analyzed['NNG']:
                if tag in self.tag_index[index]:
                    match_cnt +=1
            if last_match_cnt <= match_cnt:
                last_match_cnt = match_cnt
                last_match_index = index
            match_cnt = 0
        # print(type(last_match_index))
        return last_match_index


# engine = TripAnalyzer()
# engine.set_model()
# engine.set_sentence("겨울에 낚시하러 갈만한 여행지")
# engine.run_model()
# test = engine.result_analyzing()
# test = engine.lookup_db_index()
# test = engine.recommand_analyzing()
# data = engine.lookup_db_data(test)
# print(type(data))
# print(data)

# print(test)