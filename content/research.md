---
title: "研究内容"
source_title: "研究内容"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?%B8%A6%B5%E6%C6%E2%CD%C6"
locale: "ja"
toc: true
home: false
---

<a id="content_1_0"></a><a id="bac36443"></a>
<a id="content_1_1"></a>

### ペプチド創薬・中分子創薬 <a id="q39ae229"></a>

- Takashi Tajimi, Naoki Wakui, Keisuke Yanagisawa, Yasushi Yoshikawa, **Masahito Ohue**, Yutaka Akiyama: Computational prediction of plasma protein binding of cyclic peptides from small molecule experimental data using sparse modeling techniques, *BMC Bioinformatics*, 19(Suppl 19): 527, 2018. doi: 10.1186/s12859-018-2529-z
    
  [ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/30598072) | [Journal Website](https://doi.org/10.1186/s12859-018-2529-z) ]

- 「ペプチド創薬の最前線」, 木曽良明監修, シーエムシー出版, 2019/5/14. （分担執筆: 秋山泰, **大上雅史**, 吉川寧, 和久井直樹: 第8章 中分子創薬に適した特性を有する環状ペプチドのインシリコ設計, pp. 70-78）  
  <https://www.cmcbooks.co.jp/products/detail.php?product_id=5619>

<a id="content_1_2"></a>

### Ligand-based Virtual Screening <a id="k9f340f0"></a>

標的に対する化合物の活性情報を教師データとして未知の化合物の活性を予測する機械学習手法を研究しています。

<a id="content_1_3"></a>

#### Learning-to-Lank <a id="d7466475"></a>

- **Masahito Ohue**, Shogo D. Suzuki, Yutaka Akiyama: Learning-to-rank technique based on ignoring meaningless ranking orders between compounds, *Journal of Molecular Graphics and Modelling*. doi: 10.1016/j.jmgm.2019.07.009 (in press)
    
  [ PubMed | [Journal Website](https://doi.org/10.1016/j.jmgm.2019.07.009) | [github](https://github.com/akiyamalab/SPDRank) ]

- Shogo D. Suzuki, **Masahito Ohue**, Yutaka Akiyama: PKRank: A novel learning-to-rank method for ligand-based virtual screening using pairwise kernel and RankSVM, *Artificial Life and Robotics*, **23**(2): 205-212, 2018. doi: 10.1007/s10015-017-0416-8
    
  [ [Journal Website](https://doi.org/10.1007/s10015-017-0416-8) ]

<a id="content_1_4"></a>

#### Graph Convolutional Deep Neural Network <a id="j08d8abf"></a>

![we.png](/assets/488eee0c153a.png)

![we2.png](/assets/29dfed6e95a7.png)

- **Masahito Ohue**, Ryota Ii, Keisuke Yanagisawa, Yutaka Akiyama: Molecular activity prediction using graph convolutional deep neural network considering distance on a molecular graph, In *Proceedings of the 2019 International Conference on Parallel and Distributed Processing Techniques & Applications (PDPTA'19)*, 122-128, Las Vegas, NV, USA, July 29, 2019.   
  [ [Paper](https://csce.ucmss.com/cr/books/2019/LFS/CSREA2019/PDP3528.pdf) | [arXiv](http://arxiv.org/abs/1907.01103) | [Slide](https://www.slideshare.net/tonets/pdpta19ohue/) ]

<a id="content_1_5"></a>

### Drug-Target Interaction予測 <a id="w28ce8f8"></a>

タンパク質と薬剤の２部ネットワークを予測する新規手法を開発しています。

<a id="content_1_6"></a>

#### NRLMFβ <a id="r44dbbe6"></a>

Beta分布を利用した新しい近傍正則化付ロジスティック行列因子分解法を開発しました。

- Tomohiro Ban, **Masahito Ohue**, Yutaka Akiyama: NRLMFβ: Bata-distribution-rescored Neighborhood Regularized Logistic Matrix Factorization for Improving Performance of Drug–Target Interaction Prediction, *Biochemistry and Biophysics Reports*, 18:100615, 2019. doi: 10.1016/j.bbrep.2019.01.008
    
  [ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/30793050) | [Journal Website](https://doi.org/10.1016/j.bbrep.2019.01.008) | [github](https://github.com/akiyamalab/NRLMFb) ]

<a id="content_1_7"></a>

#### BO-DTI <a id="z853f10f"></a>

ベイズ最適化 (GP-MI法) によってDTI予測の学習にかかる時間を約10倍高速化しました。

- Tomohiro Ban, **Masahito Ohue**, Yutaka Akiyama: Efficient Hyperparameter Optimization by Using Bayesian Optimization for Drug-Target Interaction Prediction, In *Proceedings of the 7th IEEE International Conference on Computational Advances in Bio and Medical Sciences (ICCABS 2017)*, 8 pages, Orlando, FL, USA, October 19-21, 2017. doi: 10.1109/ICCABS.2017.8114299   
  [ [Download](/)\* | [IEEE Xplore](https://doi.org/10.1109/ICCABS.2017.8114299) | Slide ]
  　\*2017 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.
  <http://www.github.com/akiyamalab/BO-DTI>

<a id="content_1_8"></a>

#### Link Indicator Kernel <a id="m32fe4aa"></a>

![icic2017.png](/assets/3985cbc2df44.png)

リンク指標を用いたマルチプルカーネル法を提案しました。

- **Masahito Ohue**, Takuro Yamazaki, Tomohiro Ban, Yutaka Akiyama: "Link Mining for Kernel-based Compound-Protein Interaction Predictions Using a Chemogenomics Approach", In *Proceedings of the Thirteenth International Conference On Intelligent Computing (ICIC2017)* (Lecture Notes in Computer Science), 10362, 549-558, Liverpool,UK August 7-10, 2017.   
  [ [Paper](https://link.springer.com/chapter/10.1007/978-3-319-63312-1_48) | [arXiv](https://arxiv.org/abs/1705.01667) | [Slide](https://www.slideshare.net/tonets/icic2017) ]

<a id="content_1_9"></a>

### Spresso <a id="g427ac90"></a>

![spresso_logo.png](/assets/4dd72bfb02a4.png)

タンパク質の3次元構造に基づいた高速なプレ・スクリーニングを提供します．
<http://www.bi.cs.titech.ac.jp/spresso>

- Keisuke Yanagisawa, Shunta Komine, Shogo D. Suzuki, **Masahito Ohue**, Takashi Ishida, Yutaka Akiyama: Spresso: An ultrafast compound pre-screening method based on compound decomposition, *Bioinformatics*, **33**(23): 3836-3843, 2017. doi: 10.1093/bioinformatics/btx178
    
  [ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/28369284) | [Journal Website](https://doi.org/10.1093/bioinformatics/btx178) ]

- Keisuke Yanagisawa, Shunta Komine, Rikuto Kubota, **Masahito Ohue**, Yutaka Akiyama: Optimization of memory use of fragment extension-based protein-ligand docking with an original fast minimum cost flow algorithm, *Computational Biology and Chemistry*, **74**: 399-406, 2018. doi: 10.1016/j.compbiolchem.2018.03.013 (In Proc. APBC2018)
    
  [ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/29628156) | [Journal Website](https://doi.org/10.1016/j.compbiolchem.2018.03.013) | [slide](https://www.dropbox.com/s/c3bktwvfzh6qkpl/APBC2018_yanagisawa.pdf?dl=1) ]

<a id="content_1_10"></a>

### MEGADOCK-Web <a id="ac69162b"></a>

logo.png

- Takanori Hayashi, Yuri Matsuzaki, Keisuke Yanagisawa, **Masahito Ohue**\*, Yutaka Akiyama\*: MEGADOCK-Web: an integrated database of high-throughput structure-based protein-protein interaction predictions, *BMC Bioinformatics*, **19**(Suppl 4): 62, 2018. doi: 10.1186/s12859-018-2073-x (In Proc. APBC2018)
    
  [ [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/29745830) | [Journal Website](https://doi.org/10.1186/s12859-018-2073-x) | [slide](https://www.dropbox.com/s/r4dzfi3s78j3t6g/MEGADOCK-Web-slide.pdf?dl=1) ]

- **大上雅史**, 林孝紀, 秋山泰: タンパク質間相互作用と複合体構造の予測結果を検索できるウェブサイト「MEGADOCK-Web」, 実験医学, 2019年6月号, Vol.37, No.9, pp. 1469-1474, 2019/5/20.   
  [ [羊土社](https://www.yodosha.co.jp/jikkenigaku/book/9784758125208) ]

<a id="content_1_11"></a>

### MEGADOCK <a id="hcb43714"></a>

[![http://www.bi.cs.titech.ac.jp/megadock/megadock-logo-ss.png](/assets/e332429c7bfb.png)](http://www.bi.cs.titech.ac.jp/megadock/megadock-logo-ss.png)

タンパク質の立体構造情報を利用するタンパク質間相互作用予測システムです．  
FFT-baseのドッキングアルゴリズムを踏襲しながらも，スコアモデルの改良やスレッド並列化などによって
高速な計算を実現しています．

詳しくはこちら：[ソフトウェア](/software/)  
NVIDIA Application Catalogにも掲載されています：<https://www.nvidia.com/en-us/data-center/gpu-accelerated-applications/catalog/>

<a id="content_1_12"></a>

### タンパク質間ドッキング予測 <a id="m1103948"></a>

タンパク質の立体構造から，それらの三次元形状同士の相補性（形の凸凹の相性）や表面電荷の相互作用などを解析して，複合体の形を高速に予測する方法を研究しています．

![ppd.png](/assets/256de92e912d.png)

- **Masahito Ohue**†, Yuri Matsuzaki†, Nobuyuki Uchikoga, Takashi Ishida, Yutaka Akiyama: "MEGADOCK: An all-to-all protein-protein interaction prediction system using tertiary structure data", *Protein and Peptide Letters*, **21**(8): 766-778, 2014.
    
  [ [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/23855673) | [BenthamScience](http://eurekaselect.com/112757) ]

<a id="content_1_13"></a>

#### 新しいボクセルスコアモデルの開発 <a id="ycecd5ab"></a>

rPSCと呼ばれる独自の形状相補性スコアモデルをベースとし，静電相互作用や脱水和自由エネルギーをモデル化した，高速に計算可能なスコアモデルを提案しています．

- **Masahito Ohue**, Yuri Matsuzaki, Takashi Ishida, Yutaka Akiyama: "Improvement of the Protein-Protein Docking Prediction by Introducing a Simple Hydrophobic Interaction Model: an Application to Interaction Pathway Analysis", *In Proceedings of The 7th IAPR International Conference on Pattern Recognition in Bioinformatics (PRIB2012), Lecture Notes in Bioinformatics 7632*, 178-187, Springer Heidelberg, 2012.  
  [ [SpringerLink](http://link.springer.com/chapter/10.1007%2F978-3-642-34123-6_16) | [Slide](https://dl.dropbox.com/u/342898/slide/prib2012.pdf) | [Streaming(e-Bio)](http://dna02.bio.kyutech.ac.jp/e-bio/lectures/detail/123) ]

<a id="content_1_14"></a>

#### High Performance Computing (HPC) <a id="j466e4f2"></a>

並列計算機（スーパーコンピュータ）を利用したタンパク質ドッキング予測計算を行うソフトウェアを開発しています．

- **Masahito Ohue**†, Takehiro Shimoda†, Shuji Suzuki, Yuri Matsuzaki, Takashi Ishida, Yutaka Akiyama: "MEGADOCK 4.0: an ultra–high-performance protein–protein docking software for heterogeneous supercomputers", *Bioinformatics*, **30**(22): 3281-3283, 2014.
    
  [ [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/25100686) | [Oxford](http://dx.doi.org/10.1093/bioinformatics/btu532) ]
- Yuri Matsuzaki, Nobuyuki Uchikoga, **Masahito Ohue**, Takehiro Shimoda, Toshiyuki Sato, Takashi Ishida, Yutaka Akiyama: "MEGADOCK 3.0: A high-performance protein-protein interaction prediction software using hybrid parallel computing for petascale supercomputing environments", *Source Code for Biology and Medicine*, **8**(1): 18, 2013.
    
  [ [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/24004986) | [BioMedCentral](http://www.scfbm.org/content/8/1/18/) ]

<a id="content_1_15"></a>

### タンパク質間相互作用ネットワーク予測 <a id="n5944a16"></a>

タンパク質間の相互作用は，体内での酵素反応や細胞内外での情報伝達の基本となり，生命活動の根幹を支えています．我々はタンパク質の立体構造に基づくドッキング計算から，相互作用をするタンパク質ペアを高速に予測する方法を研究しています．

![ppi.png](/assets/f43799a9a85a.png)

- **Masahito Ohue**†, Yuri Matsuzaki†, Nobuyuki Uchikoga, Takashi Ishida, Yutaka Akiyama: "MEGADOCK: An all-to-all protein-protein interaction prediction system using tertiary structure data", *Protein and Peptide Letters*, **21**(8): 766-778, 2014.
    
  [ [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/23855673) | [BenthamScience](http://eurekaselect.com/112757) ]
- **大上雅史**, 松崎由理, 松��裕介, 佐藤智之, 秋山泰: “MEGADOCK：立体構造情報からの網羅的タンパク質間相互作用予測とそのシステム生物学への応用”, *情報処理学会論文誌 数理モデル化と応用*, **3**(3): 91-106, 2010.
    
  [ [IPSJ Digital Library](https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=70731&item_no=1&page_id=13&block_id=8) ]

<a id="content_1_16"></a>

### タンパク質-RNA間相互作用予測 <a id="i6b59038"></a>

ヒトゲノム中にはnon-coding RNAが約1500個ほどコードされているといわれており，タンパク質同士だけでなく，多数のRNAがタンパク質と相互作用しています．我々は独自のタンパク質間相互作用予測の手法を応用した，新しいタンパク質-RNA間相互作用予測の手法を研究しています．

![pri.png](/assets/e66920e6acd4.png)

- **Masahito Ohue**, Yuri Matsuzaki, Yutaka Akiyama: "Docking-calculation-based Method for Predicting Protein-RNA Interactions",
  *Genome Informatics*, **25**(1): 25-39, Aug 3 2011.
    
  [ [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/22230937) | [J-stage](https://www.jstage.jst.go.jp/article/gi/25/1/25_1_25/_article) ]

<a id="content_1_17"></a>

### 細菌走化性パスウェイ解析への応用 <a id="hf8b014a"></a>

外界からの刺激に応答して運動が起こる性質を，走性と呼びます．
例えば，大腸菌は飢餓状態になると，べん毛の遺伝子を発現し，
栄養となる物質のより多い方へ移動する化学走性（走化性）を示します．
この性質を実現しているのは，刺激に応じて系の内部状態を変えられる細胞内のシグナル伝達系です．
外界の状態を感知し，内部状態を変えつつ対応するという行動は，
学習という概念にもつながる大変興味深い現象です．
また，走化性系によって制御されるべん毛モーターは，
きわめてエネルギー効率の良い分子モーターとしても注目され，
機械分野への応用研究も知られています．

![ch.png](/assets/5a70b9243997.png)

本研究では，この系の既知のPPIを「正解」と定義してMEGADOCKの評価を行うとともに，
この系の制御に関わる未知の相互作用の検出を試みました．

- Yuri Matsuzaki†, **Masahito Ohue**†, Nobuyuki Uchikoga, Yutaka Akiyama: "Protein-protein interaction network prediction by using rigid-body docking tools: application to bacterial chemotaxis", *Protein and Peptide Letters*, **21**(8): 790-798, 2014.
    
  [ [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/23855669) | [BenthamScience](http://eurekaselect.com/112775) ]

<a id="content_1_18"></a>

### ヒトアポトーシスパスウェイ解析への応用 <a id="e38d0856"></a>

アポトーシスとは，個体の状態を良好に保つために積極的に引き起こされる，
制御された細胞の自殺機構です．
アポトーシスの減少に起因する疾病として癌や自己免疫疾患があり，
アポトーシスの増加に起因するものとしてはAIDSや神経変性疾患が挙げられ，
これらの疾病に関わる創薬ターゲットとして，アポトーシスパスウェイ中のタンパク質群が注目されています．

この研究では，MEGADOCKによってアポトーシスに関連するタンパク質の相互作用ネットワークを予測するとともに，既知複合体構造をテンプレート情報として利用する手法と組み合わせることで適合率の高い予測が行えることを示しました．

![apo.png](/assets/a88bc2b6c82d.png)

- **Masahito Ohue**, Yuri Matsuzaki, Takehiro Shimoda, Takashi Ishida, Yutaka Akiyama: "Highly Precise Protein-Protein Interaction Prediction Based on Consensus Between Template-Based and *de Novo* Docking Methods", *BMC Proceedings*, **7**(Suppl 7): S6, 2013.
    
  [ [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/24564962) | [BioMedCentral](http://www.biomedcentral.com/1753-6561/7/S7/S6) ]
