Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> df = pd.read_excel("C:/travel/travel.xlsx")
>>> df
      번호      여행지  ...                                                 사진   지역
0      1   갈산근린공원  ...  http://tong.visitkorea.or.kr/cms/resource/62/2...   서울
1      2  감로암(서울)  ...  http://tong.visitkorea.or.kr/cms/resource/85/2...   서울
2      3  개운사(서울)  ...  http://tong.visitkorea.or.kr/cms/resource/26/2...   서울
3      4  경국사(서울)  ...  http://tong.visitkorea.or.kr/cms/resource/88/2...   서울
4      5      경복궁  ...  http://tong.visitkorea.or.kr/cms/resource/23/2...   서울
..   ...      ...  ...                                                ...  ...
194  195      NaN  ...                                                NaN  NaN
195  196      NaN  ...                                                NaN  NaN
196  197      NaN  ...                                                NaN  NaN
197  198      NaN  ...                                                NaN  NaN
198  199      NaN  ...                                                NaN  NaN

[199 rows x 6 columns]
>>> df.dropna()
      번호       여행지  ...                                                 사진   지역
0      1    갈산근린공원  ...  http://tong.visitkorea.or.kr/cms/resource/62/2...   서울
1      2   감로암(서울)  ...  http://tong.visitkorea.or.kr/cms/resource/85/2...   서울
2      3   개운사(서울)  ...  http://tong.visitkorea.or.kr/cms/resource/26/2...   서울
3      4   경국사(서울)  ...  http://tong.visitkorea.or.kr/cms/resource/88/2...   서울
4      5       경복궁  ...  http://tong.visitkorea.or.kr/cms/resource/23/2...   서울
..   ...       ...  ...                                                ...  ...
125  126  넥슨컴퓨터박물관  ...  http://tong.visitkorea.or.kr/cms/resource/73/2...  제주도
126  127    마라도 등대  ...  http://tong.visitkorea.or.kr/cms/resource/15/2...  제주도
127  128     백약이오름  ...  http://tong.visitkorea.or.kr/cms/resource/99/2...  제주도
128  129     사라봉공원  ...  http://tong.visitkorea.or.kr/cms/resource/92/1...  제주도
129  130  서귀포자연휴양림  ...  http://tong.visitkorea.or.kr/cms/resource/11/1...  제주도

[130 rows x 6 columns]
>>> df = df.dropna()
>>> df
      번호       여행지  ...                                                 사진   지역
0      1    갈산근린공원  ...  http://tong.visitkorea.or.kr/cms/resource/62/2...   서울
1      2   감로암(서울)  ...  http://tong.visitkorea.or.kr/cms/resource/85/2...   서울
2      3   개운사(서울)  ...  http://tong.visitkorea.or.kr/cms/resource/26/2...   서울
3      4   경국사(서울)  ...  http://tong.visitkorea.or.kr/cms/resource/88/2...   서울
4      5       경복궁  ...  http://tong.visitkorea.or.kr/cms/resource/23/2...   서울
..   ...       ...  ...                                                ...  ...
125  126  넥슨컴퓨터박물관  ...  http://tong.visitkorea.or.kr/cms/resource/73/2...  제주도
126  127    마라도 등대  ...  http://tong.visitkorea.or.kr/cms/resource/15/2...  제주도
127  128     백약이오름  ...  http://tong.visitkorea.or.kr/cms/resource/99/2...  제주도
128  129     사라봉공원  ...  http://tong.visitkorea.or.kr/cms/resource/92/1...  제주도
129  130  서귀포자연휴양림  ...  http://tong.visitkorea.or.kr/cms/resource/11/1...  제주도

[130 rows x 6 columns]
>>> df.to_excel("C:/travel/travel2.xlsx")
>>> 