---
title: "PDBを綺麗にする"
source_title: "PDBを綺麗にする"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?PDB%A4%F2%E5%BA%CE%EF%A4%CB%A4%B9%A4%EB"
locale: "ja"
toc: true
home: false
---

back>[PDB toolbox](/notes/pdb-toolbox/)

<a id="content_1_0"></a><a id="t679c708"></a>

PDBファイルの中には書式がテキトウなのが結構あります．  
ツールが動かない！？なんてときは以下のスクリプトを試してみてください．（Biopythonが必要です）

```
#!/usr/bin/python
#
# Masahito Ohue
# python pdbclean.py pdbfile

import os
import sys
import Bio
from Bio.PDB import *

# delete terminal of rows
PDB = sys.argv[1]
fp = open(PDB, 'r')
line = fp.readlines()
fp.close()
fp = open(PDB, 'w')
for l in line:
    fp.write(l[0:67]+"\n")
fp.close()

# add element columns by biopython
parser = PDBParser()
str = parser.get_structure("test1", PDB) 

io = PDBIO()
io.set_structure(str)
io.save(sys.argv[1])
```

これで

```
$ python pdbclean.py protein.pdb
```

とするとprotein.pdbが綺麗になっています（上書き注意）．

<a id="content_1_1"></a>

### 注意 <a id="a700a05f"></a>

- ATOM行，HETATM行以外は知りません．
- エレメント列周辺を消してからbiopythonで自動的にエレメント列を付けます．
- 色々大事な情報が消えるかもしれません．
