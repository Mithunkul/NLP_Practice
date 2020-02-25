from urllib import request


url = "https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters"
response = request.urlopen(url)
raw = response.read().decode('utf8')

with open("rawText.txt", 'w',  encoding="utf-8") as f:
    f.write(raw)