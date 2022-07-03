def hamm(s, t):
    assert len(s)==len(t)
    d=0
    for i in range(0, len(s)):
        if s[i] != t[i]:
            d+=1
    return(d)

with open('rosalind_hamm.txt', 'r') as f:
    s=f.readline().strip()
    t=f.readline().strip()
    print(hamm(s,t))