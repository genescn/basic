content = 'We are not what we should be \
We are not what we need to be \
But at least we are not what we used to be \
  -- Football Coach'

l = content.split()
words = set(l)

dict = {}

for w in words:
    lw = []
    for count, d in enumerate(l):
        if d == w:
            try:
                lw.append(l[count+1])
            except IndexError:                
                continue
    dict[w] = lw

print(dict)    