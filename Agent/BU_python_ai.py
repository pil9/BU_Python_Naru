from konlpy.tag import Kkma
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
                #관형사형 전성어미 << 뭐여 -_-
                ETD_list.append(task[0])

            else:
                continue
        return dict
