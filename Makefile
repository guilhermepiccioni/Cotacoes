.PHONY: venv
venv:
	pip install virtualenv && virtualenv venv

.PHONY: build
build:
	pip install -r requeriments.txt

.PHONY: new_price
new_price:
	python price_all.py

.PHONY: history_price
history_price:
	cd History_price && python view_all_files.py
