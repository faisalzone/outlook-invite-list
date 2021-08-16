import re
f = open('file_text.txt')
text = f.read()
f.close()

clean = re.sub('<.*?>', ' ', text)
clean2 = clean.replace('  ; ', '\n')

f = open('file_new.txt', 'w')
f.write(clean2)
f.close()
