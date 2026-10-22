---
title: "TSUBAME関連"
source_title: "TSUBAME関連"
source_url: "https://www.bi.cs.titech.ac.jp/~ohue/index.php?TSUBAME%B4%D8%CF%A2"
locale: "ja"
toc: true
home: false
---

[研究メモ](/notes/)

<a id="content_1_0"></a><a id="ka1fff0e"></a>

どちらかの用途だけでも使えます。ジョブの制限時間＆制限時間オプション、グループ、プレミアムオプションなどはスクリプト内で定義されています。

(例)Sキューに3つジョブを投げる

```
./auto-sleep.sh S 3
(一覧が出てくるので入りたいノードを選ぶ、もしくはそのまま終了)
```

(注意)デフォルトでは投げてから3秒待ってt2statをしますが、TSUBAMEが混んでるときはすぐにジョブが入らないことがあります。プレミアムオプションをつけるとすぐに入りやすくなります。

(例)既に投げてあるスリープジョブが走ってるノードに入る

```
./auto-sleep.sh a 0
(一覧が出てくるので入りたいノードを選ぶ)
```

以下、auto-sleep.shのソース。

```
#!/usr/bin/sh
CMDNAME=`basename $0`
if [ $# -ne 2 ]; then
	echo "Usage: ./$CMDNAME [Queue_name] [Number_of_jobs] (if [Number_of_jobs] == 0, only ssh)"
	exit 1
fi
echo -e "\n *** This script throws sleep-job & ssh to the sleep node. *** \n"
WTIME=90:00:00
QUE=$1
GROUP=t2g-acls2012
PREMIUM=2
if [ $2 -gt 0 ]; then
for i in `seq 1 $2`
do
echo "sleep 1500000" > sleep.sh
chmod 755 sleep.sh
t2sub -j oe -N sleep -W group_list=$GROUP -p $PREMIUM -q $QUE -l walltime=$WTIME -et 2 -l select=1:ncpus=12:gpus=3:mem=50gb ./sleep.sh
rm -f sleep.sh
sleep 3s
done
fi
echo -e "\n *** Result of t2stat. *** \n"
IFS=$'\n'
LINES=( $( t2stat -n1 | grep "sleep" ) )
node=0
for line in ${LINES[@]}; do
    echo $line
	#echo $node
	host=`echo $line | sed -e "s/^.*[^.]t2\(.*\)\/.*$/t2\1/"`
	#echo $host
	nodelist[$node]=$host
	node=`expr ${node} + 1`
	#echo $i
done
while :
do
echo -e "\n Node number\n"
node=0
for line in ${nodelist[@]}; do
	echo "$node : ${LINES[$node]}"
	node=`expr ${node} + 1`
done
echo "$node : end this script"
echo -e "\n Please input node number.\n"
read ans
if [ $ans -eq $node ]; then
break
fi
ssh="ssh ${nodelist[$ans]} -Y"
echo $ssh
eval $ssh
break
done
```
