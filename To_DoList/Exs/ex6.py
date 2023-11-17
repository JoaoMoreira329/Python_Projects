filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for name in filenames:
    file = open(name, 'w')
    file.write("Hello")
    file.close()
    