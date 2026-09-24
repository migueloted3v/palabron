import json, base64, struct, sys
ALPHA = "abcdefghijklmnopqrstuvwxyzñ"
idx = {c:i for i,c in enumerate(ALPHA)}
words = sorted(set(w for w in json.load(open(sys.argv[1] if len(sys.argv)>1 else 'index.json')) if 2<=len(w)<=15 and all(c in idx for c in w)))
print("words", len(words))
class Node:
    __slots__=("final","edges","id","_key")
    cnt=0
    def __init__(s):
        s.final=False; s.edges={}; s.id=Node.cnt; Node.cnt+=1; s._key=None
    def key(s):
        return (s.final, tuple(sorted((c,n.id) for c,n in s.edges.items())))
root=Node(); reg={}; unchecked=[]; prev=""
def minimize(down):
    while len(unchecked)>down:
        p,c,ch=unchecked.pop()
        k=ch.key()
        if k in reg: p.edges[c]=reg[k]
        else: reg[k]=ch
for w in words:
    cp=0
    while cp<min(len(w),len(prev)) and w[cp]==prev[cp]: cp+=1
    minimize(cp)
    node=unchecked[-1][2] if unchecked else root
    for c in w[cp:]:
        n=Node(); node.edges[c]=n; unchecked.append((node,c,n)); node=n
    node.final=True; prev=w
minimize(0)
# serialize: edge = letter(5) | final(1)<<5 | last(1)<<6 | child<<7
nodes=[]; seen={}
def collect(n):
    stack=[n]
    while stack:
        x=stack.pop()
        if x.id in seen: continue
        seen[x.id]=None; nodes.append(x)
        for c in x.edges.values(): stack.append(c)
collect(root)
start={}; pos=1  # index 0 dummy
for n in nodes:
    if n.edges: start[n.id]=pos; pos+=len(n.edges)
arr=[0]*pos
for n in nodes:
    if not n.edges: continue
    items=sorted(n.edges.items(), key=lambda t: idx[t[0]])
    for i,(c,ch) in enumerate(items):
        v=idx[c] | (32 if ch.final else 0) | (64 if i==len(items)-1 else 0) | (start.get(ch.id,0)<<7)
        arr[start[n.id]+i]=v
print("nodes",len(nodes),"edges",pos, "rootstart", start[root.id])
assert start[root.id]==1
b=struct.pack("<%dI"%pos,*arr)
open("dawg.b64","w").write(base64.b64encode(b).decode())
print("bytes",len(b),"b64",len(base64.b64encode(b)))
