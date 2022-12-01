r='1'+'9'*100
while '19' in r or '299' in r or '3999' in r:
    r=r.replace('19','2',1)
    r=r.replace('299','3',1)
    r=r.replace('3999','1',1)
print(r)