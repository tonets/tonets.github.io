---
title: "PDBを取ってくる"
source_title: "PDBを取ってくる"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?PDB%A4%F2%BC%E8%A4%C3%A4%C6%A4%AF%A4%EB"
locale: "ja"
toc: true
home: false
---

[PDB toolbox](/notes/pdb-toolbox/)

<a id="content_1_0"></a><a id="e30fe51e"></a>

- なんのひねりもありません．

```
#!/bin/bash

CMDNAME=`basename $0`
if [ $# -ne 1 ]; then
        echo "Usage: $CMDNAME pdbid"
        exit 1
fi

wget http://www.rcsb.org/pdb/download/downloadFile.do\?fileFormat=pdb\&compression=NO\&structureId=$1 -O $1.pdb
```

使い方

```
$ bash PDBLoader.sh 1CGI
```
