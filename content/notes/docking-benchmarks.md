---
title: "研究メモ/protein complex benchmarks"
source_title: "研究メモ/protein complex benchmarks"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?%B8%A6%B5%E6%A5%E1%A5%E2/protein%20complex%20benchmarks"
locale: "ja"
toc: true
home: false
---

[研究メモ](/notes/)

<a id="content_1_0"></a><a id="tc4648ca"></a>

[ZDOCKグループ](http://zlab.umassmed.edu)のベンチマーク．現在ver4.0まで配布中．

- Benchmark3.0まで　[URL](http://zlab.bu.edu/zdock/benchmark.shtml)
- Benchmark4.0　<https://zlab.umassmed.edu/benchmark/benchmark4.html>
  - 以下の点に注意
    - PDB ID:1OYVより2種類の複合体を利用している(1OYV_A:I, 1OYV_B:I)．
      1OYV_A:I の方は1OYV, 1OYV_B:I の方は**BOYV**としてデータが収録されている．
      この2つのLigandは全く同じファイルである．
    - PDB ID:1QFWより2種類の複合体を利用している(1QFW_HL:AB, 1QFW_IM:AB)．
      1QFW_IM:ABの方は1QFW, 1QFW_HL:ABの方は**2QFW**としてデータが収録されている．
      この2つのLigandは全く同じファイルである．
    - 2012/7/6 にiRMSDが訂正され，難易度カテゴリが一部変更されている．Web上のTableが一番正しいものとおもわれる．
- Benchmark5.0 [URL](http://zlab.umassmed.edu/benchmark/)
  - The Complex PDB Code is the PDB code of the structure from which the bound receptor and ligand are obtained. In the cases of 1QFW and 9QFW both cases are obtained from the 1QFW PDB file, thus the creation of the PDB name 9QFW for the purpose of uniqueness was necessary. 9QFW is not a valid PDB code, and is only used in this benchmark. Similarly, BAAD is created from 3AAD, BOYV from 1OYV, and BP57 and CP57 from 3P57.
  - 1TFH contains two chains, A and B, for the same protein with an identical sequence. The two chains have different missing residues. 1TFH chain A is used as a unbound constituent of 1AHW and 1TFH chain B is used as as unbound constituent of 1JPS and 1FAK. To make them consistent, we added 1JPS_l_u.pdb.2 and 1FAK_l_u.pdb.2 using 1TFH chain A for the downloadable files.

**References**

- Mintseris, J., Wiehe, K., Pierce, B., Anderson, R., Chen, R., Janin, J., & Weng, Z. (2005). Protein-Protein Docking Benchmark 2.0: an update. Proteins, 60(2), 214-6. [doi:10.1002/prot.20560](http://onlinelibrary.wiley.com/doi/10.1002/prot.20560/abstract)
- Hwang, H., Pierce, B., Mintseris, J., Janin, J., & Weng, Z. (2008). Protein-protein docking benchmark version 3.0. Proteins, 73(3), 705-9. [doi:10.1002/prot.22106](http://onlinelibrary.wiley.com/doi/10.1002/prot.22106/abstract)
- Hwang, H., Vreven, T., Janin, J., & Weng, Z. (2010). Protein-protein docking benchmark version 4.0. Proteins, 78(15), 3111-4. [doi:10.1002/prot.22830](http://onlinelibrary.wiley.com/doi/10.1002/prot.22830/abstract)

<a id="content_1_1"></a>

## Dockground <a id="xd5d8d38"></a>

Vakserらのグループによるベンチマーク．

- <http://dockground.bioinformatics.ku.edu/index.shtml>

- version 3.0
  DOUBLE（unboundが両方あるやつ）とSINGLE（片方しかunboundがない）がある．  
  DOUBLEは102複合体，SINGLEは131複合体．unboundが一部水素付きであることに注意．  
  モノマー同士のペアは，DOUBLEが65個，SINGLEが105個．  
  単体タンパク質の重複，ZLAB Benchmarkとの重複など調査中．

**References**

- Liu, S., Gao, Y., & Vakser, I. A. (2008). DOCKGROUND protein-protein docking decoy set. Bioinformatics (Oxford, England), 24(22), 2634-5. [doi:10.1093/bioinformatics/btn497](http://bioinformatics.oxfordjournals.org/content/24/22/2634)

<a id="content_1_2"></a>

## NLC Dataset <a id="rc0d715d"></a>

- SDOCKのチームが使ってるドッキングベンチマーク
- NLC = no large conformational change
- <http://mdl.ipc.pku.edu.cn/mdlweb/register.php?id=12>

<a id="content_1_3"></a>

## Transcription Factor-DNA Docking Benchmark <a id="j5a788cc"></a>

- <http://bioinfozen.uncc.edu/tf-dna-benchmarks/>

**References**

- Kim, R., Corona, R. I., Hong, B., & Guo, J.-tao. (2011). Benchmarks for flexible and rigid transcription factor-DNA docking. BMC structural biology, 11(1), 45. [doi:10.1186/1472-6807-11-45](http://www.biomedcentral.com/1472-6807/11/45)

<a id="content_1_4"></a>

## Protein-RNA Docking Benchmark <a id="v2839965"></a>

- A protein–rna docking benchmark (i): Nonredundant cases
- A protein-RNA docking benchmark (II): extended set from experimental and homology modeling data
  - <http://life.bsc.es/pid/protein-rna-benchmark/>

**References**

- Barik A, C N, P M, Prasad Bahadur R. (2012). A protein-rna docking benchmark (i): Nonredundant cases.
  Proteins. [doi:10.1002/prot.24083](http://onlinelibrary.wiley.com/doi/10.1002/prot.24083/abstract)
- Pérez-Cano L, Jimenez-Garcia B and Fernandez-Recio J. (2012). A protein-RNA docking benchmark (II): extended set from experimental and homology modeling data. Proteins. [doi:10.1002/prot.24075](http://onlinelibrary.wiley.com/doi/10.1002/prot.24075/abstract)

<a id="content_1_5"></a>

## Protein-RNA Docking Benchmark (別グループ) <a id="dc7a7ac8"></a>

- <http://zoulab.dalton.missouri.edu/RNAbenchmark/>

**Reference**

- Huang SY, Zou X. A nonredundant structure dataset for benchmarking protein-RNA computational docking. J Comput Chem 34(4):311-8, 2013.[doi:10.1002/jcc.23149](http://onlinelibrary.wiley.com/doi/10.1002/jcc.23149/abstract)

<a id="content_1_6"></a>

### 番外編 <a id="s82eec5e"></a>

- Gao, M., & Skolnick, J. (2011). New benchmark metrics for protein-protein docking methods. Proteins, 79(5), 1623-34. [doi:10.1002/prot.22987](http://onlinelibrary.wiley.com/doi/10.1002/prot.22987/abstract)
