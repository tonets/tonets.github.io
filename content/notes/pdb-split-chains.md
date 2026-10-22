---
title: "PDBをchainで分割する"
source_title: "PDBをchainで分割する"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?PDB%A4%F2chain%A4%C7%CA%AC%B3%E4%A4%B9%A4%EB"
locale: "ja"
toc: true
home: false
---

[PDB toolbox](/notes/pdb-toolbox/)

<a id="content_1_0"></a><a id="xc0cd694"></a>

名前通りのスクリプト．

<a id="content_1_1"></a>

### PDBの中のチェインをすべて取り出す <a id="uea517ce"></a>

- separate_single.py

  ```
  #!/usr/bin/python
  #last updated : 2014/10/21

  import re
  import sys 

  if (len(sys.argv) != 2):
      print 'Usage: # python %s pdbfile' % sys.argv[0]
      quit()

  id = sys.argv[1][0:4]
  fp = open(sys.argv[1])
  pdb = fp.read()
  fp.close()

  pdb = pdb.rstrip("\n")
  pdb = pdb.split("\n")

  cl = []

  for l in pdb:
      if l[0:6] == 'COMPND' and l[11:17] == 'CHAIN:':
          cl.append(l[18])

  for c in cl:
      fc = open(id + "_" + c + ".pdb", "w")
      for ll in pdb:
          l = ll
          if l[0:4] != 'ATOM' and l[0:6] != 'HETATM':
              continue
          if l[17:20] == 'HOH':
              continue
          if l[16] != ' ' and l[16] != 'A':
              continue
          if l[21] == c:
              fc.write(ll + "\n") 

      fc.write("TER\n")
      fc.write("END")
      fc.close()
  ```

つかいかた

```
$ python separate_single.py 1CGI.pdb
```

とすると，チェインごとのファイル（1CGI_I.pdb, 1CGI_E.pdb）が生成されます．

<a id="content_1_2"></a>

### 複数ファイルを扱うバージョン <a id="t34a9c6f"></a>

- separate.py

  ```
  #!/usr/bin/python
  # Masahito Ohue 

  import re
  import sys

  if (len(sys.argv) != 2):
      print 'Usage: # python %s listfile' % sys.argv[0]
      quit()

  fp = open(sys.argv[1])
  lst = fp.readlines()
  fp.close()

  for ll in lst:
      l = ll
      id = l.split(",")[0]
      cs = l.split(",")[1].strip()
      cl = list(cs)

      try:
          fp = open(id + ".pdb")
      except IOError:
          print 'not found, PDB ID =', id, ", Chain", cs
      else:
          print 'open, PDB ID =', id, ', Chain =', cs
          pdb = fp.read()
          fp.close() 

          fc = open(id + "_" + cs + ".pdb", "w")
          pdb = pdb.rstrip("\n")
          pdb = pdb.split("\n")
          for c in cl:
              for lll in pdb:
                  l = lll
                  if l[0:4] != 'ATOM' and l[0:6] != 'HETATM':
                      continue
                  if l[17:20] == 'HOH':
                      continue
                  if l[16] != ' ' and l[16] != 'A':
                      continue
                  if l[21] == c:
                      fc.write(lll + "\n")  

              fc.write("TER\n") 
          fc.write("END")
          fc.close()
  ```

こんなリストファイルを用意する．

- list.txt

  ```
  3WVL, A
  3WVL, O
  3WVL, ABCOPQ
  2ZYQ, B
  ```

  - [PDB 3WVL](http://www.rcsb.org/pdb/explore/explore.do?structureId=3WVL)
  - [PDB 2ZYQ](http://www.rcsb.org/pdb/explore/explore.do?structureId=2ZY9)

3WVL.pdbと2ZYQ.pdbがある場所で，以下を実行．

```
$ python separate.py list.txt
open, PDB ID = 3WVL , Chain = A
open, PDB ID = 3WVL , Chain = O
open, PDB ID = 3WVL , Chain = ABCOPQ
open, PDB ID = 2ZYQ , Chain = B
```

すると

```
3WVL_A.pdb 3WVL_O.pdb 3WVL_ABCOPQ.pdb 2ZYQ_B.pdb
```

ができている．

<a id="content_1_3"></a>

### 注意 <a id="k5a5b0ac"></a>

- ATOM行とHETATM行だけ見ます．
- 水(HOH)は省きます．省きたくない場合は該当のif文をコメントアウト．
- 残基名の前にAとかBとかあるやつ（同一残基が複数の座標に存在する可能性を持つもの）は，Aだけ抜き出します．
