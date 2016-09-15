#字符串初始用
what_he_does = ' plays '
his_instrument = 'guitar'
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument

print(artist_intro)

#字符串与数字混用
num = 1
stringNum = '9'
num2 = int(stringNum)

print(num + num2)

#字符串相乘
words = 'word ' * 3
print(words)

#字符串分片与索引,[0:n]表示的是从0到n-1个数
name = 'My name is marco'
print(name[-1])
print(name[:-1])

#game
word = 'friends'
find_the_evil_in_your_friends = word[0]+word[2:4]+word[-3:-1]
print(find_the_evil_in_your_friends)

#字符串命名处理
url = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]
print(file_name)