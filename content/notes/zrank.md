---
title: "ZRANKを動かす"
source_title: "ZRANKを動かす"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?ZRANK%A4%F2%C6%B0%A4%AB%A4%B9"
locale: "ja"
toc: true
home: false
---

[PDB toolbox](/notes/pdb-toolbox/)

関連: [ZDOCKを動かす](/notes/zdock/)

<a id="content_1_0"></a><a id="k89c3f01"></a>

- 使い方

  ```
  $ zrank zdockoutfile startidx endidx
  ```

  - startidx, endidxにリランキングしたいdecoyの順位の範囲を入力．（例 startidx=1, endidx=2000）

    ```
    $ zrank 1CGI.out 1 2000
    ```
  - outファイル中に書いてあるPDBが存在しかつ水素付きであること．
  - 出力は指定したoutファイルの名前に.zr.outがくっついた名前のファイル．
    中身は

    ```
    順位\tエネルギースコア
    ```

    の羅列

- Ref: Pierce, B., & Weng, Z. (2007). ZRANK: reranking protein docking predictions with an optimized energy function. Proteins, 67(4), 1078-86. doi:10.1002/prot.21373
