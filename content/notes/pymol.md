---
title: "PyMOL"
source_title: "PyMOL"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?PyMOL"
locale: "ja"
toc: true
home: false
---

[研究メモ](/notes/)

<a id="content_1_0"></a>

### 便利なリンク <a id="wc53346d"></a>

- <http://www-cryst.bioc.cam.ac.uk/members/zbyszek/figures_pymol>
- <http://www.iam.u-tokyo.ac.jp/chem/IMCB-8ken-HP/Lab_Manuals/entori/2010/7/23_PyMOL_(PDB_viewer)_manyuaru.html>
- <http://d.hatena.ne.jp/biochem_fan/20130717/1374037184>

<a id="content_1_1"></a>

### コピペ用 <a id="kd2603e5"></a>

```
set cartoon_oval_length, 0.9
set cartoon_oval_width, 0.2
set cartoon_rect_length, 0.7
set cartoon_rect_width, 0.3
set cartoon_loop_radius, 0.15
set antialias, 3
set ambient, .2
set ray_trace_gain, 0
set ray_trace_mode, 1
set ray_trace_color, black
bg_color white
set opaque_background, 1
ray
```

<a id="content_1_2"></a>

### 絵描き <a id="uc76dc63"></a>

<https://gyazo.com/b15b8575275cb6b1d74f883c6f902cd8> (1IGT)

```
as spheres
set ray_trace_gain, 0
set ray_trace_mode, 3
set ambient, .4
set ray_trace_color, black
set antialias, 3
ray
```

<a id="content_1_3"></a>

### cartoonを細く <a id="oa2cdd12"></a>

```
set cartoon_oval_length, 0.6
set cartoon_oval_width, 0.15
set cartoon_rect_length, 0.6
set cartoon_rect_width, 0.25
set cartoon_loop_radius, 0.15
```

<a id="content_1_4"></a>

### コマンド <a id="i48d25ee"></a>

pdbidのchain XをHOGEという名前で選ぶ

```
select HOGE, (pdbid and chain X)
```

chain Xの430-440残基を選ぶ

```
select HOGE, (resi 430:440 and chain X)
```

透過png

```
set opaque_background, 0
```

白背景

```
bg_color white
```

ラベルのサイズ

```
set label_size, 20
```

ラベルの色

```
set label_color, red
```

ラベルの縁取り

```
set label_outline_color, black
```
