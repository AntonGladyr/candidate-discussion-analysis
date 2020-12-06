conservative_data = data/conservative/conservative_hottest_2020-12-01T18\:00\:00+0000.json data/conservative/conservative_hottest_2020-12-02T10\:30\:24+0000.json data/conservative/conservative_hottest_2020-12-03T17\:56\:13+0000.json data/conservative/conservative_hottest_29112020.json
politics_data = data/politics/politics_hottest_2020-12-01T18\:00\:00+0000.json data/politics/politics_hottest_2020-12-02T10\:30\:05+0000.json data/politics/politics_hottest_2020-12-03T17\:55\:52+0000.json

data/conservative/extracted.tsv: scripts/extract_to_tsv.py
	python3 "$<" -i $(conservative_data) -o "$@" -n 1000

data/politics/extracted.tsv: scripts/extract_to_tsv.py
	python3 "$<" -i $(politics_data) -o "$@" -n 1000

data/merged.tsv: scripts/merge_datasets.py data/conservative/extracted.tsv data/politics/extracted.tsv
	python3 "$<" -i data/conservative/extracted.tsv data/politics/extracted.tsv -o "$@" -k Biden -k Trump

data/annotated_tweets.csv:
	curl -L "https://docs.google.com/spreadsheets/d/1WEDy-NSEEJPNQuCFA0aFu5iG4qp4ZUd87n3ghJhfoF0/export?format=csv&gid=2113791825" -o "data/annotated_tweets.csv"

data/tfidf.txt: data/annotated_tweets.csv
	< "$<" python3 scripts/tfidf.py
