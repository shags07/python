with open('fullforms.txt') as f1:
    files = [open('%d.txt' % i, 'w') for i in range(1)]
    for i, line in enumerate(f1):
        files[i % 1].write(line)
    for f in files:
        f.close()
