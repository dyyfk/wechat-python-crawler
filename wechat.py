male = female = other = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

total = len(friends[1:])
print("男性好友比例: %.2f%%" % (float(male)/total*100) + "\n"+
      "女性好友比例: %.2f%%" % (float(female)/total*100) + "\n"+
      "未知性别: %.2f%%" % (float(other)/total*100) + "\n")


def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable

Signature = get_var('Signature')


import re
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("",signature)
    siglist.append(signature)
text = "".join(siglist)

import jieba
wordlist = jieba.cut(text,cut_all = True)
word_space_split = "".join(wordlist)

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

import numpy as np
from PIL import Image
coloring = np.array(Image.open("/Users/Chef/Desktop/wechat.jpg"))

my_wordcloud = WordCloud(background_color="white", max_words=2000,
                        mask=coloring,max_font_size=60,random_state=42,scale=2,
                         font_path='/Windows/Fonts/Arial.ttf').generate(word_space_split)


image_colors= ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
