import pandas as pd
import re
File_path = "c:/Users/happy/Downloads/200812_200812_주민등록인구및세대현황_연간.csv"#파일 위치
df = pd.read_csv(File_path,encoding='euc-kr')#불러오기
print(df.행정구역)
def re_compile(x):#행정구역 쉽게 바꾸기
    com = re.compile('[0-9 ()]')
    return com.sub('',x)
df.행정구역 = df.행정구역.apply(re_compile)#모든 행정구역에 입히기
print(df.행정구역)
df.to_excel("200812_200812_주민등록인구및세대현황_연간(최종).xlsx", index=False)