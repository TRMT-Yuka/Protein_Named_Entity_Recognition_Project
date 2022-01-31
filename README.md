# Proteins_NER
Project on NER of Proteins.


以下は作成順です


### data_original
	外部サイトよりダウンロードしたプロテイン固有表現のxml形式データ5種類を格納


### data_summary
#### TF
	ダウンロードした状態のオリジナルデータは二つのタンパク質に同一（true）か非同一（false）のいずれかのラベルがついた状態
	本ディレクトリには各ラベルの割合を格納．

#### PROT
	各xmlデータにおける
	・出現プロテイン一覧
	・出現回数
	をそれぞれまとめたcsvを格納


### data_query
#### PROT
	各xmlデータにおける
		・出現プロテイン一覧(protein)，
		・出現回数(appearances)，
		・クエリを投げたときのヒット数(hits)，
		・最大スコアを持つクエリの総数（max_score_hits）
	をそれぞれまとめたcsvを格納

#### QUERY
all

	PROTでまとめてある出現プロテイン一覧ごとにクエリを投げ，得られた結果をjson形式にまとめたもの

best_score

	all同様クエリを投げた結果．ただし検索スコアが最も高い結果のみ

summary.txt
	タンパク質を用いての検索の結果どれくらいの割合でクエリに結果が返ってきたのか

| データ名 | 単一結果 | 複数結果 | 結果無し | 検索エラー | 合計 | 
| -------- | -------: | -------: | -------: | ---------: | ---: | 
| amied    | 642      | 407      | 85       | 4          | 1138 | 
| bioinfer | 439      | 530      | 77       | 6          | 1052 | 
| hprd50   | 120      | 67       | 2        | 0          | 189  | 
| iepa     | 59       | 54       | 14       | 3          | 130  | 
| lll      | 28       | 71       | 19       | 3          | 121  | 

![可視化グラフ](https://github.com/TRMT-Yuka/Proteins_NER/blob/main/README_img/bar_graph_1.png)

momomomomo

### Generative_Model
https://github.com/duttaprat/PPI_Generative
論文内にあったgitの著者リポジトリより

### data_final
先行研究を再現するべく各出現プロテインごとにクエリを投げて情報取得を試みた結果のcsv．


