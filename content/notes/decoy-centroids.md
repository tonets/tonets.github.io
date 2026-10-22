---
title: "decoy ligand重心の分布図を作る"
source_title: "decoy ligand重心の分布図を作る"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?decoy%20ligand%BD%C5%BF%B4%A4%CE%CA%AC%C9%DB%BF%DE%A4%F2%BA%EE%A4%EB"
locale: "ja"
toc: true
home: false
---

back>[PDB toolbox](/notes/pdb-toolbox/)

<a id="content_1_0"></a><a id="qfd51db7"></a>

**目次**

<a id="content_1_1"></a>

### 概要 <a id="l2011d96"></a>

タンパク質ドッキングで作ったリガンドの分布図を作ります．  
こんな感じの絵を描くのが目標です．

[![1ACB_Centers.png](/assets/dfc37873fab0.png)](/assets/1ACB_Centers.png)

真ん中のタンパク質(receptor)の周りのリガンドタンパク質の予測位置を重心のみで周りに表示しています．  
赤い点は各候補構造，黄色い球は上位1〜10位の候補構造，ピンクのリボンは正解位置のリガンドタンパク質です．  
ドッキングツールはMEGADOCKおよびZDOCKを想定しています．  
使うツールは一番下にまとめました．> [ツール群](/notes/decoy-centroids/#a4a7ab47)

<a id="content_1_2"></a>

### Ligand (decoy) PDBを作る <a id="e90db7f6"></a>

ドッキングさせたLigandのPDBを作ります．  
MEGADOCKやZDOCKではドッキングさせた複合体構造は，
outファイルの中に回転角情報と座標情報のみ記載されています．
ここからPDBファイルを生成します．

基本的にはMEGADOCKのdecoygen，ZDOCKのcreate.pl/create_ligを使います．  
2000個の候補構造を生成(MEGADOCK/ZDOCKのデフォルト)したとして今後の説明を行います．

- MEGADOCK (zsh表記)

  ```
  for i (`seq 1 2000`) ./decoygen decoy.$i.pdb ligand.pdb docking.out $i
  ```
- ZDOCK

  ```
  create.pl docking.out　（.outファイルに記載のパスのPDBを参照します）
  ```

ZDOCKの場合，3.0.2とそれ以前のバージョンとでは形式が変わっていますので注意が必要です．  
その他のドッキングツールでも，レセプターの位置が変化せずリガンドのみの座標(PDB)で候補解が記述されていればこの後の処理は同様です．

<a id="content_1_3"></a>

### Ligand decoyの重心座標を計算してファイルにまとめる <a id="v4f0c19b"></a>

<a id="content_1_4"></a>

#### 重心座標を計算する <a id="t8f61241"></a>

2000個のPDBができました．これらの重心座標を計算します．  
重心計算には[pdb-Tools](https://pdb-tools.googlecode.com/files/pdbTools_0.2.1.tar.gz)を使います．  
pythonがあればダウンロードして適当なディレクトリに展開して使えます．  
ホームディレクトリの ~/src/に展開したとして話を進めます．

```
$ ~/src/pdbTools_0.2.1/pdb_centermass.py ligand.pdb
ligand.pdb    11.4160    9.2530    2.8806
```

という形で出力されます（スペース区切りです）．  
そのままでは非常に使いづらいので，カンマ区切りのcsvにしてしまいましょう．

- cmcoord.sh

  ```
  #!/bin/sh
  cmtext=`~/src/pdbTools_0.2.1/pdb_centermass.py $1`
  echo $cmtext | sed "s/ /, /g" | cut -d , -f 1,2,3,4
  ```

これで

```
$ bash cmcoord.sh ligand.pdb
ligand.pdb, 11.4160, 9.2530, 2.8806
```

となります．  
2000個のdecoyの重心座標を計算するには，

```
$ for i (`seq 1 2000`) { bash cmcoord.sh decoy.$i.pdb; } > Centers.csv
```

とすると，Centers.csvにdecoy.1.pdbからdecoy.2000.pdbまでの重心が記録されます．

なお，pdbToolsのpdb_centermass.pyはエレメント列がちゃんとないと動きません．  
PDBファイルの中にはエレメント列がテキトウになっているのも多いので，
その場合は以下のスクリプトで綺麗にしましょう．（Biopythonが必要です）

- pdbclean.py

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
$ python pdbclean.py ligand.pdb
```

とするとligand.pdbが綺麗になっています（上書き注意）．  
decoyのpdbを生成する前にやりましょう．

<a id="content_1_5"></a>

#### 重心座標をまとめたPDBを作る <a id="sf5b575d"></a>

Centers.csvを読み取ってPDBビューワで表示できるようにします．  
具体的には重心座標にテキトウな原子（FEとか）を置いてやれば良いです．  
PDBの形式に注意してスクリプトを用意します．

- pdbcm.py

  ```
  #!/usr/bin/python
  # Masahito Ohue
  import os
  import sys
  import csv

  cm = sys.argv[1]
  line = csv.reader(open(cm))
  i = 0
  ch = "L"  # chain name

  for l in line:
      i = i+1
      xcoord = float(l[1])
      ycoord = float(l[2])
      zcoord = float(l[3])
      print('HETATM %4d  FE  FE  %s%4d    %8.3f%8.3f%8.3f  1.00  1.00           C' % (i, ch, i, xcoord, ycoord, zcoord))
  ```

これで，

```
$ python pdbcm.py Centers.csv > Centers.pdb
```

とすると，重心座標を鉄原子にしたCenters.pdbができます．  
receptor.pdbとチェイン名が被らないように適宜変更して下さい．

<a id="content_1_6"></a>

### Centers.pdbをPyMOLで表示する <a id="wa781be2"></a>

あとはCenters.pdbをPyMOLに読み込ませればOKです．  
しかし設定をマウスでカチカチ変えるのも面倒なので，スクリプトを書いて表示します．  
PyMOLはpythonスクリプトが動くので，それで．  
（pdbidを引数にして，たとえば1ACB_r_b.pdbと1ACB_Centers.pdbを表示します．）

- decoys.py

  ```
  def showdecoys(pdbid):
  	cmd.delete("all")
  	cmd.load(pdbid+"_r_b.pdb") 
  	cmd.load(pdbid+"_Centers.pdb")
  	cmd.load(pdbid+"_l_b.pdb")
  	cmd.zoom("all")
  	cmd.hide("all")
  	cmd.bg_color("white")
  	cmd.set("ray_opaque_background", "0")
  	cmd.color("green", pdbid+"_r_b")
  	cmd.color("magenta", pdbid+"_l_b")
  	cmd.show("cartoon", "all")
  	cmd.select("lig", "chain L in "+pdbid+"_Centers.pdb")
  	cmd.hide("everything", "lig")
  	cmd.color("red", "lig")
  	cmd.set("sphere_scale", "0.15", "lig")
  	cmd.show("sphere", "lig")
  	
  	cmd.select("top", "res 1-10 in chain L in "+pdbid+"_Centers.pdb")
  	cmd.set("sphere_scale", "0.7", "top")
  	cmd.show("sphere", "top")
  	cmd.color("yellow", "top")
  	cmd.ray()
  	cmd.png(pdbid+"_Centers")
  ```

これをPyMOLのコマンドウィンドウで，

```
PyMOL> run decoys.py
PyMOL> showdecoys("1ACB")
```

と入力すれば，最初のような図ができます．

<a id="content_1_7"></a>

### 1ACBで実例 <a id="wedb4bef"></a>

ZLAB Protein-Protein Dockign Benchmark (<http://zlab.umassmed.edu/benchmark/)> の1ACB(bound)で実際に実行してみます．  
1ACB_r_b.pdbと1ACB_l_b.pdbはエレメント列がないので，最初にpdbclean.pdbをかけています．  
ドッキングにはMEGADOCK 4.0を使っています．

**�� PDBを綺麗にして，MEGADOCK，decoyのpdb生成**

```
$ python pdbclean.py 
$ ./megadock -R 1ACB_r_b.pdb -L 1ACB_l_b.pdb -o 1ACB_b.out
$ for i (`seq 1 2000`) ./decoygen 1ACB_l_b.$i.pdb 1ACB_l_b.pdb 1ACB_b.out $i
```

（1ACB_l_b.1.pdbから1ACB_l_b.2000.pdbができます．）

**�� 重心座標の計算，鉄原子に置き換えたPDBの生成**

```
$ for i (`seq 1 2000`) { bash cmcoord.sh 1ACB_l.$i.pdb; } > 1ACB_Centers.csv
```

（少し時間がかかります．お茶でも淹れましょう．）

```
$ python pdbcm.py 1ACB_Centers.csv > 1ACB_Centers.pdb
```

**�� PyMOLでの表示**  
PyMOLを開きます．（カレントディレクトリに該当のpdbがあるものとします．）

```
PyMOL> run decoys.py
PyMOL> showdecoys("1ACB")
```

これでカレントディレクトリにpngファイルができましたね．

[![1ACB_Centers.png](/assets/dfc37873fab0.png)](/assets/1ACB_Centers.png)

<a id="content_1_8"></a>

### ファイル，関連ツール一覧 <a id="a4a7ab47"></a>

- MEGADOCK <http://www.bi.cs.titech.ac.jp/megadock>
- ZDOCK <http://zdock.umassmed.edu/software/>
- PDB-Tools <https://code.google.com/p/pdb-tools/>
- Biopython <http://biopython.org>
- スクリプト [ [まとめてダウンロード](/) ]
  もしくは

  ```
  wget http://www.bi.cs.titech.ac.jp/~ohue/script/centermass.zip
  ```

  - cmcoord.sh
  - pdbclean.py
  - pdbcm.py
  - decoys.py
