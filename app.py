import streamlit as st

st.set_page_config(layout="wide")
st.title("Overseas Chinese YouTubers (中文海外油管大拿）") 
st.write("By Dr. Yan, v1.0, 3/12/2023")

a=f" ##### After choosing a name, click the related link. Click 'refresh' to clear everything."

data={
      "None": "haha",
      "XiaoMing 蕭茗看世界": "https://www.youtube.com/@user-tc3ev4bs8i",
      "Fang Zhuan 方的言":"https://www.youtube.com/@fangzhuan",
      "JiangFeng 江峰时刻":"https://www.youtube.com/@JiangFengTimes",
      "WenZhao文昭谈古论今": "https://www.youtube.com/results?search_query=wenzhao",
      "Mr. Shen 公子沈":"https://www.youtube.com/@gongzishen",
      "Sydney DaDDy 雪梨女乃爸":"https://www.youtube.com/@SydneyDaddy1",
      "weiyuksj 薇羽看世間":"https://www.youtube.com/@weiyuksj",
      "LiMuYang 新聞看點 李沐陽":"https://www.youtube.com/@MuYangShow",
      "jiangtaigong 加州姜太公NEWS":"https://www.youtube.com/@jiangtaigong",
      "LaoDeng 老灯":"https://www.youtube.com/@laodeng89",
      "LaoHei 公民老黑":"https://www.youtube.com/@laohei",
      "Ruiyan 睿眼看世界":"https://www.youtube.com/results?search_query=%E6%96%87%E7%9D%BF",
      "Jason Angle 杰森視角":"https://www.youtube.com/@jasonangle",
      "XuMoRen 说真话的徐某人":"https://www.youtube.com/@xumouren"
      }

data2={
      "None": "haha",
      "SHO TV 希望之聲TV":"https://www.youtube.com/@SOH_TV",
      "Tian Liang Times 天亮時分":"https://www.youtube.com/@TianLiangTimes",
      "Zhang Lin Shi Ye 張林視野":"https://www.youtube.com/@ZhangLinShiYe",
       "VOA Chinese 美国之音中文网":"https://www.youtube.com/@voachinese",
      "BBC News 中文":"https://www.youtube.com/@bbcnewschinese",
      "Rocky 洛奇":"https://www.youtube.com/@Rocky1108",
      "Fang Wei Time 方偉時間":"https://www.youtube.com/@FangWeiTime",
      "jayhsu1965 徐杰慢半拍":"https://www.youtube.com/@jayhsu1965",
      "Wang Dan 王丹學堂":"https://www.youtube.com/@wangdanschool",
      "ShangGuanLun 上官亂":"https://www.youtube.com/@shangguanluan",
      "GuoWenGui 郭文贵":"https://www.youtube.com/@user-jt1zr1ey7v"
      }


data3={
      "None": "haha",
      "Mark Space 馬克時空":"https://www.youtube.com/@markspacetime",
      "火力就是正義（百科頻道）":"https://www.youtube.com/watch?v=9J97ISB8mrA",
      "tansuoshifen 探索時分 · 周子定":"https://www.youtube.com/@tansuoshifen",
      "名将榜":"https://www.youtube.com/@agl",
      "Arms Say 兵器說":"https://www.youtube.com/@armssay",
      "military-focus 時事軍事-夏洛山":"https://www.youtube.com/@military-focus",
      "New Cold War Room 新冷战情报室":"https://www.youtube.com/@newcoldwarroom"
      }

data4={
      "None": "haha",
      "YueGe Movie 越哥说电影":"https://www.youtube.com/@yuegemovie",
      "A Yi Dian Ying 阿奕电影":"https://www.youtube.com/@ayidianying"

      }

with st.expander("Step 1: click here to see (or hide) a simple explanation."):
    st.write(a)
    
col1, col2,col3=st.columns([1.2,1.2,1.2])

#names=data.keys()
#names=("None","XiaoMing 萧茗","WenZhao 文昭谈古论今")
names=data.keys()
names2=data2.keys()
names3=data3.keys()
names4=data4.keys()

k="====>"
    
who=col1.selectbox("List 1 (时事 1): Choose a name, then go to his/her channel", names)
if who=="None":
    #col1.write(f' {k} No name chosen yet')
    col1.write('                       ')
elif who!="None":
    this=data[who]
    col1.write(this) 
else:
    col1.write('haha')
    
   
who2=col1.selectbox("List 2 (时事 2): Choose a name, then go to his/her channel", names2)
if who2=="None":
    #col1.write(f' {k} No name chosen yet from list #2.')
    col1.write('                       ')
elif who2!="None":
    this=data2[who2]
    col1.write(this) 
else:
    col1.write('haha')    


who3=col2.selectbox("List 3 （军事）: Choose a name, then go to his/her channel", names3)
if who3=="None":
    #col2.write(f' {k} No name chosen yet')
    col2.write('                       ')
elif who3!="None":
    this=data3[who3]
    col2.write(this) 
else:
    col2.write('haha')

who4=col3.selectbox("List 4 （影视）: Choose a name, then go to his/her channel", names4)
if who4=="None":
    #col3.write(f' {k} No name chosen yet')
    col3.write('                       ')
elif who4!="None":
    this=data4[who4]
    col3.write(this) 
else:
    col3.write('haha')

