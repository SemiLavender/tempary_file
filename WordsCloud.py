import  matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import jieba
from wordcloud import WordCloud, ImageColorGenerator

text = open(r'/Users/cloudin/PycharmProjects/CloudWorld/words.txt', "r").read()

cut_text = jieba.cut(text, cut_all=False)
res = '/'.join(cut_text)

image = Image.open(r'/Users/cloudin/PycharmProjects/CloudWorld/test2.jpg')
graph = np.array(image)

wc = WordCloud(font_path=r'/Users/cloudin/Downloads/weuruan/msyh.ttf',
               background_color='white', max_font_size=50, mask=graph)
wc.generate(res)

image_color = ImageColorGenerator(graph)
wc.recolor(color_func=image_color)
wc.to_file(r'/Users/cloudin/PycharmProjects/CloudWorld/cloudWord_images.jpg')

plt.figure('词云图')
plt.imshow(wc)
plt.axis('off')
plt.show()