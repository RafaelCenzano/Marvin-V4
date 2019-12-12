init:
	pip3 install -r requirements.txt

test:
	nose2 -v --pretty-assert

run:
	python3 run.py

clean:
	python3 cleaner.py