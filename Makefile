init:
	pip3 install -r requirements.txt

upgrade:
	pip3 install --upgrade -r requirements.txt

test:
	pytest

clean:
	pystarter clean

run: clean test
	python3 run.py
	$(MAKE) clean