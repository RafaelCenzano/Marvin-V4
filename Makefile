init:
	pip3 install -r requirements.txt

test:
	pytest

update:
	pip install --upgrade tqdm attrs beautifulsoup4 bs4 certifi chardet Click decorator docutils flask flask-wtf idna imageio imageio-ffmpeg importlib-metadata itsdangerous jinja2 lxml markupsafe more-itertools moviepy numpy packaging pafy pillow pip pluggy proglog py pyparsing pystarter pytest requests setuptools six soupsieve urllib3 wcwidth werkzeug wheel wtforms youtube-dl zipp
	pip freeze > requirements.txt

clean:
	pystarter clean

run: clean test
	python3 run.py
	$(MAKE) clean