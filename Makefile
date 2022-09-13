.PHONY: venv
venv:
	pip install virtualenv && virtualenv venv

.PHONY: build
build:
	pip install -r requirements.txt

.PHONY: trade
trade:
	python3 main.py

.PHONY: history_trades
history_trades:
	cd History_price && python view_all_files.py
