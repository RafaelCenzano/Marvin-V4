# Marvin Version 4.0.0

Python virtual assistant. Version 4.0.0

![alt text](https://img.shields.io/github/license/Marvin-Virtual-Assistant/Marvin-V4.svg)
![alt text](https://img.shields.io/github/stars/Marvin-Virtual-Assistant/Marvin-V4.svg)
![alt text](https://img.shields.io/github/forks/Marvin-Virtual-Assistant/Marvin-V4.svg)
![alt text](https://img.shields.io/github/issues/Marvin-Virtual-Assistant/Marvin-V4.svg)

## Setup

Clone the repository and enter it

```
git clone https://github.com/Marvin-Virtual-Assistant/Marvin-V4.git
cd Marvin-V4
```

## Requirements

[Use a virtualenv to create an isolated enviorment](https://virtualenv.pypa.io/en/latest/)

Run the make command to install requirements

```
make
```

or with pip manually

```
pip3 install -r requirements.txt
```

Fix for installing [pocketsphinx](https://github.com/bambocher/pocketsphinx-python/issues/28)

## Running the program

Marvin virtual assistant runs a flask frontend and once you run the firsy command it will open and run any needed proccess for you and let you get started immediately.

```
make run
```

or with python manually

```
python3 run.py
```

<!-- DO NOT REMOVE - contributor_list:start -->
<!-- DO NOT REMOVE - contributor_list:end -->

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
