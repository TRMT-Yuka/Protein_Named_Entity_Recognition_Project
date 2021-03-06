# Protein_Eigen_Expression_Extraction_Project
タンパク質固有表現同士の関係予測タスクにおいて，P.Dutta et al.（2020）では各固有表現ごとにタンパク質およびDNAの識別IDといった付属情報を付与することで，関係予測精度が向上したことを報告している．一方，それら付属情報のアノテーションについては人手で行う必要があり，人的コストの面からみて実用性は低い．本プロジェクトでは，Pythonモジュールmygeneを利用し，アノテーション作業がどこまで自動化可能かを確認したものである．

## data
医療ドメインのテキスト，タンパク質固有表現の出現箇所，固有表現間の関係性がアノテーションされたデータセット．[外部サイト](http://corpora.informatik.hu-berlin.de/)よりダウンロードできるデータのうち，タンパク質を対象としたxml形式データを格納．ファイル名は以下の5種類．


+ amied
+ bioinfer
+ hprd50
+ iepa
+ lll 


## data_summary 
上記5種類のデータについて，基本的な集計を行った結果を格納したディレクトリである．元データには各タンパク質間の関係性として同一（true）と非同一（false）の二種類のうちいずれかが付与されている．
	
## data_summary / TF
本ディレクトリでは各データごとに同一（true）と非同一（false）のラベルの割合を格納している．例えば，\data_summary\TF\aimed_bioc_TF.txt は以下のような内容となっているが，これはaimedデータ全体では，true:falseが1000 : 47291存在し，割合としてはそれぞれおよそ2%と97%であったことを表している．これらの値は，同一（true）と非同一（false）のラベルの偏りが最終的なモデル精度に影響する可能性があると考え，事前に算出を行った．
	
```
【Ratio of T to F】
TRUE:FALES = 1000 : 47291
2.070779234225839% : 97.92922076577416%
```



## data_summary / PROT
各xmlデータにおける出現タンパク質名，およびその出現回数をcsv形式，2列のテーブルとして格納している．例えば\data_summary\PROT\aimed_bioc_prot.csvの一行目と二行目は以下のようになっているが，これはaimed内において(MIP)-1 alpha　というタンパク質名が42回出現，.CDC37が18回出現したことを意味する．これらのデータは，タンパク質名の種別一覧リストを入手することで，手動での表記ゆれ対応等が可能かどうかを確認する目的で作成した．

| (MIP)-1 alpha      | 42      | 
| .CDC37      | 18       |


## data_query
このディレクトリの内容物については，Pythonモジュールbiothings_clientを利用して構築を行った．mygeneは，キーワード
## data_query / PROT
各xmlデータにおける以下の情報をそれぞれまとめた4列のcsvを格納．

+ 出現プロテイン一覧(protein)，
+ 出現回数(appearances)，
+ クエリを投げたときのヒット数(hits)，
+ 最大スコアを持つクエリの総数（max_score_hits）

##  data_query / QUERY / all
data_query/PROTでまとめてある出現タンパク質名一覧ごとにクエリを投げ，得られた結果をjson形式にまとめたもの．Proteins_NER\data_query\QUERY\all\aimed_bioc\0_.CDC37.jsonの場合，aimedデータにおける.CDC37というタンパク質名をクエリとして得られる結果を格納している．

## data_query / QUERY / best_score
allとほぼデータ構造は同じで，同様クエリを投げた結果．ただし検索スコアが最も高い結果のみを残し，あとはカットしている．

## data_query / summary.txt

5種類すべてのデータにおいて，出現するタンパク質を用いた検索を行った結果どれくらいの割合でクエリに結果が返ってきたのかを総合的にまとめた表．機械的な検索のみでどの程度反応が返ってくるのかを総合的に判断する目的で作成．結果として多くの場合に何らかのクエリ結果が存在することが判明した．このため，計画を進め，最終的なデータ構築まで実際に実装を行った．


| データ名 | 単一結果 | 複数結果 | 結果無し | 検索エラー | 合計 | 
| -------- | -------: | -------: | -------: | ---------: | ---: | 
| amied    | 642      | 407      | 85       | 4          | 1138 | 
| bioinfer | 439      | 530      | 77       | 6          | 1052 | 
| hprd50   | 120      | 67       | 2        | 0          | 189  | 
| iepa     | 59       | 54       | 14       | 3          | 130  | 
| lll      | 28       | 71       | 19       | 3          | 121  | 

![可視化グラフ](https://github.com/TRMT-Yuka/Protein_Named_Entity_Recognition_Project/blob/main/README_img/bar_graph_1.png)


## Generative_Model
論文内にあった[著者のgitリポジトリ](https://github.com/duttaprat/PPI_Generative)より．BCLLおよびILDについて，著者らが手動でアノテーションしたと思われるデータが格納されている．本プロジェクトで自動化コードを生成後，その整合性の確認に使用予定．

## data_final
先行研究を再現するべく各出現プロテインごとにクエリを投げ情報取得を試みた結果を取得し，五つのデータセットごとにcsvにまとめたもの．項目は以下の通り．

+ surface　
+ symbol
+ _id
+ entrezgene
+ ensembl_id
+ pdb_id
+ name
	
構築手順は以下の通り．
（１）データセット内のプロテインを取得し，surfaceに格納
（２）biothings_clientモジュールを用い，各プロテイン名をクエリとした場合の結果をメソッドqueryにより得る．ヒットした結果のうち，max_scoreに該当するものだけを選択．
（３）max_scoreの結果から，フィールドsymbol,entrezgeneを取得．entrezgeneが存在しない項目についてはそれ以降の項目は”No_Data”の文字を入力
（４）フィールドentrezgeneが存在するものに関して，getgineメソッドを用い遺伝子情報を得る．
得られた遺伝子情報からフィールド_id，entrezgene，ensembl/gene，pdb，nameを取得し+ _id，entrezgen

