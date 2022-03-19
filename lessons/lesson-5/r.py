import re

text = "Hello! my name is Jack!"

#result = re.search("!", text)

result = re.findall("m", text)

print(result)
