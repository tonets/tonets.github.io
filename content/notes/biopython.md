---
title: "BioPython"
source_title: "BioPython"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?BioPython"
locale: "ja"
toc: true
home: false
---

[PDB toolbox](/notes/pdb-toolbox/)

<a id="content_1_0"></a><a id="off75acc"></a>

TSUBAMEにはnumpyが入っているので，そのままインストールできる．

```
python setup.py build
python setup.py test
python setup.py install --exec-prefix /AS/YOU/LIKE
```

- パスを通す

  ```
  （例）
  export PYTHONPATH=/home/usr5/A2600088/src/biopython/lib64/python2.6/site-packages:$PYTHONPATH
  ```

<a id="content_1_1"></a>

## マニュアル <a id="w7b6cb1f"></a>

チュートリアル

- <http://biopython.org/DIST/docs/tutorial/Tutorial.pdf>

その他

- <http://biopython.org/DIST/docs/cookbook/biopdb_faq.pdf>
- <http://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ>
- <http://www.bi.a.u-tokyo.ac.jp/~tak/biopython.html>

<a id="content_1_2"></a>

## PDBの操作例 <a id="jdd94382"></a>

```
import Bio
from Bio.PDB import *

parser = PDBParser()
str = parser.get_structure("hoge", nantoka.pdb)

for model in str.get.list():
   for chain in model.get_list():
      for residue in chain.get_list():
         residue.get_resname()
         for atom in residue.get_list():
            atom.get_name()
```

<a id="content_1_3"></a>

## 原子間距離 <a id="x8f9958b"></a>

atomオブジェクトの変数a1とa2に対し，

```
d = a1 - a2
```

で距離d[Å]が得られる．
