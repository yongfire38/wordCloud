from konlpy.corpus import kolaw
kolaw.fileids()

c = kolaw.open('constitution.txt').read()
print(c[:40])