seqs = {}
seq = ''
seqid = ''

def GC(seq):
    gc = (seqs[seqid].count('G')+seqs[seqid].count('C'))/len(seq)*100
    return gc

for line in open('rosalind_gc.txt', 'r'):
  print(line)
  if line[0] == '>':
    if len(seq) > 0:
      seqs[seqid] = seq
      
    seqid = line.rstrip()[1:]
    seq = ''
  else:
    seq += line.rstrip().upper()

if len(seq) > 0:
    seqs[seqid] = seq
print(seqs)
maxid = max(seqs, key=seqs.get)

print(maxid, seqs[maxid])