init:
	pip install -r requirements.txt

test:
	nose2 -v --pretty-assert

run:
	python3 run.py