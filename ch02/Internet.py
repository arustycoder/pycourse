from urllib.request import urlopen
file = urlopen('http://helloworldbook.com/data/message.txt')
message = file.read()
print(message)