init:
	pip3 install -r requirements.txt

test:
	pytest

clean:
	pystarter clean

run: clean test
	python3 run.py
	$(MAKE) clean