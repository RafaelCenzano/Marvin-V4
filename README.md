# Marvin Version 4

Python virtual assistant. Version 4.


## Setup

Clone the repository and enter it

```
git clone https://github.com/Marvin-Virtual-Assistant/Marvin-V4.git
cd Marvin-V4
```

Install and test the program

```
make
```

### Requirements

The command `make` handles installation of requirements

[View the requirements!](requirements.txt)

Use pip to install needed libraries ([Use a virtualenv to create an isolated enviorment](https://virtualenv.pypa.io/en/latest/))

```
pip install -r requirements.txt
```

## Running the tests

Run tests

```
nose2 -v --pretty-assert
```

### What are the tests checking

#### Physics tests

- Kinematic calculations
- Number Processing (sig figs and rounding)

### What happens when a test fails

Report the issue [here](https://github.com/Marvin-Virtual-Assistant/Marvin-V4/issues/new)!

## Authors

* [**Rafael Cenzano**](https://github.com/RafaelCenzano)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
