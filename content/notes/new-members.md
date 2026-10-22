---
title: "覚え書き/研究室新メンバー向けのTips"
source_title: "覚え書き/研究室新メンバー向けのTips"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?%B3%D0%A4%A8%BD%F1%A4%AD/%B8%A6%B5%E6%BC%BC%BF%B7%A5%E1%A5%F3%A5%D0%A1%BC%B8%FE%A4%B1%A4%CETips"
locale: "ja"
toc: true
home: false
---

<a id="content_1_0"></a><a id="l59a590d"></a>
<a id="content_1_1"></a>

### ゼミ全般 <a id="jaf9723d"></a>

- **スライドのつくりかた**  
  この資料がよくまとまっています．一度見ておくことをおすすめします．  
  - 【プレゼン】研究室発表のプレゼン資料の作り方【初心者用】 <http://www.slideshare.net/yutamorishige50/how-to-present-better>

- フォントの選び方・使い方
  <https://www.slideshare.net/kmaztani/ss-73651272>

- これだけ守れば見やすくなるデザインの基礎 - Speaker Deck
  <https://speakerdeck.com/kinakobooster/koredakeshou-rebajian-yasukunarudezainfalseji-chu>

- 【note版】パワポ資料をぐっと魅力的にしてくれる「アイコン」をまとめました。すべて無料です！｜とくさん｜note
  <https://note.com/noritoku/n/nda18a1b13c9c>

- **参考文献の書き方**  
  いろんなスタイルがある．統一されていれば何でも良い．（ただし投稿論文では投稿先に決まりがあるはず．）
  とりあえずオーソドックスな例を．

  ```
  著者名リスト, 論文名, 雑誌名, vol(issue): pp-pp, 20XX.
  ```

  - 例: <http://pubs.acs.org/doi/abs/10.1021/ci400712h>

    ```
    Kunze J, Todoroff N, Schneider P, et al., Targeting Dynamic Pockets 
    of HIV-1 Protease by Structure-Based Computational Screening for 
    Allosteric Inhibitors, J. Chem. Inf. Model., 54(3): 987-991, 2014.
    ```
  - 省略するかしないか

- 氏名  
  姓名をフルで書くか，Myoji N. にするか，N. Myojiにする．複数人の場合，1人＋*et al*.(他)，3人＋*et al*.(他)など．*et al*.はラテン語なので*italic*体にする．

- 雑誌名  
  その雑誌ごとに省略形がだいたい決められている．省略ピリオドはつけなくても良いがスタイルを揃える．*italic*体にする．  
  例：  
  Journal of the American Chemical Society→J. Am. Chem. Soc.  
  Proceedings of the National Academy of Sciences of the United States of America→Proc. Natl. Acad. Sci. U.S.A. or Proc. Natl. Acad. Sci.  
  Journal of Molecular Biology→J. Mol. Biol.  
  BMC Bioinformatics→BMC Bioinform.  
  PLOS Computational Biology→PLOS Comput. Biol.  
  Nature Genetics→Nat. Genet.

- vol. issueなど  
  vol.54と書いたりすることもある．volを*italic*にしたり**bold**にすることもある． 54(3), **54**(3), *54*(3)

- pages  
  ページ範囲．987-91のように，共通桁を略す場合もある．-はハイフンでなくendashをできるだけ使う（TeXならハイフン2つ重ねで出せる）．ページ番号がない雑誌も増えてきている(BMC系，PLOS系)のでその場合は論文番号を書く．

- 年号  
  著者リストの直後か最後に書く．だいたい最後．()付きのものも多い．

<a id="content_1_2"></a>

### 月例報告 <a id="xd51e354"></a>

- 書くこと
  - 前回の月例報告からの進捗
    - 研究の進捗
    - 論文の状況等
    - イベント
    - 学会とか行ったら簡単なレビュー
    - 輪講やコロキウムの担当
  - 今後の予定
    - 輪講やコロキウム
    - イベント
    - 研究でやろうとしていること
    - 論文の計画等

<a id="content_1_3"></a>

### 日常 <a id="x1483984"></a>

- 電子メールを利用する上で知っておきたいこと | Smartnova
  <http://kwakita.wordpress.com/articles/cl/email-manners/>

- PuTTY
  - TSUBAME向け設定
    - login-t2.g.gsic.titech.ac.jp
    - PuTTYgenで作った秘密鍵ファイルを入力（公開鍵はT2ポータルで登録）
    - EUC-JPをUTF8に
    - Backspace設定をControl-Hに
    - アカウントを入れておけば入力を省ける
    - nullパケットを60秒おきくらいに送信するようにする　／参考 <http://morninglab.com/?p=150>

- TeX
  - KSImaterial/tex_practice.pdf at master · utmsks/KSImaterial · GitHub | <https://github.com/utmsks/KSImaterial/blob/master/contents/tex/tex_practice.pdf>
  - LaTeXにおける正しい論文の書き方 qiita <https://qiita.com/birdwatcher/items/5ec42b35d84d3ee2ffbb>

- Tips
  - 岩本ゼミにおけるレポート・論文の書式の基本ルール｜関大岩本ゼミのアドミン｜note　<https://note.com/iwasemi/n/ndb7fd31ce480>
