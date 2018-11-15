from bs4 import BeautifulSoup

DefaultPath = '/Users/cloudin/Desktop/LiuFeng/Spider/'
soup = BeautifulSoup(open(DefaultPath+'QiDian_test.htm'))
#print(soup.prettify())

# print(type(soup.title))
# print(soup.title.name)
# print(soup.title.string)