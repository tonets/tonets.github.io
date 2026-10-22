---
title: "ZDOCKを動かす"
source_title: "ZDOCKを動かす"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?ZDOCK%A4%F2%C6%B0%A4%AB%A4%B9"
locale: "ja"
toc: true
home: false
---

[PDB toolbox](/notes/pdb-toolbox/)

<a id="content_1_0"></a><a id="kce58cd8"></a>

ZDOCKはZhiping Wengらのグループが作っているドッキングソフトウェア．

- ZDOCK2.3　PSC+Elec+ACE (2 FFTs)
  - ZDOCK2.3.1　2.3+Conv3D
  - ZDOCK2.3.2　2.3+Conv3D+その他の最適化（.outの形式がちょっと変わった）
- ZDOCK3.0　PSC+Elec+IFACE (7 FFTs)
  - ZDOCK3.0.1　3.0+Conv3D
  - ZDOCK3.0.2　3.0+Conv3D+その他の最適化（.outの形式がちょっと変わった）
    が存在する．

<a id="content_1_1"></a>

### ZDOCKの使い方 <a id="p033fd3f"></a>

基本

```
./zdock -R receptor.pdb -L ligand.pdb -o docking.out
```

**重要**  
receptor.pdb と ligand.pdb は mark_sur というプログラムを実行してUniCHARMMパラメータを付加したものでないといけない．  
(カレントディレクトリにUniCHARMMファイルがないとmark_surが動かない)  
(逆に言うとUniCHARMMファイルを編集してオリジナルのパラメータも入れられる)

```
mv receptor.pdb receptor.bak; ./mark_sur receptor.bak > receptor.pdb
mv ligand.pdb ligand.bak; ./mark_sur ligand.bak > ligand.pdb
```

- mark_surについて．バージョンごとのmark_surとuniCHARMMファイルを使うこと．
