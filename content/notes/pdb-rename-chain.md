---
title: "PDBのchain名を変える"
source_title: "PDBのchain名を変える"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?PDB%A4%CEchain%CC%BE%A4%F2%CA%D1%A4%A8%A4%EB"
locale: "ja"
toc: true
home: false
---

[PDB toolbox](/notes/pdb-toolbox/)

<a id="content_1_0"></a><a id="l3291a6d"></a>

その名の通り．chain名を揃えたいときなどに使う．

```
change_chainname.py
```

```
#!/usr/bin/python

import re
import sys 

if (len(sys.argv) != 4):
    print 'Usage: # python %s [pdbfile] [target chain name] [new chain name]' % sys.argv[0]
    quit()

id = sys.argv[1][0:4]
fp = open(sys.argv[1])
pdb = fp.read()
fp.close()

pdb = pdb.rstrip("\n")
pdb = pdb.split("\n") 

fc = open(sys.argv[1], "w")
for ll in pdb:
    l = ll
    if l[0:4] != 'ATOM' and l[0:6] != 'HETATM':
        continue
    if l[17:20] == 'HOH':
        continue
    if l[21] != sys.argv[2]:
        fc.write(l + "\n")
        continue
    fc.write(l[:21] + sys.argv[3] + l[22:] + "\n")  

fc.close()
```

<a id="content_1_1"></a>

#### 使い方 <a id="o4c06086"></a>

```
python change_chainname.py 対象のPDB 対象のチェイン名 変更後のチェイン名
```

```
python change_chainname.py 1CGI.pdb E K
```

（1CGI.pdbのチェインEの名前をKに変更する）
