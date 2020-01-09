[![Build Status](https://travis-ci.org/lesunb/p2psimpy.svg?branch=master)](https://travis-ci.org/lesunb/p2psimpy)
[![codecov](https://codecov.io/gh/lesunb/p2psimpy/branch/master/graph/badge.svg)](https://codecov.io/gh/lesunb/p2psimpy)

Env Depencies
=============
python 3, pip

Used IDE: vscode, plugin python

Instal pipenv
============= 

pipenv easy the process of managing python dependencies

PIP
```console
$ pip install pyenv
```

Alternatively, macOS brew
```console
$ brew install pipenv 
```


Install dependencies
====================

Inside the project folder (after clone)

```console
$ pyenv install 3.8.0
$ pipenv install
$ pipenv shell
# (p2psimpy env) % pipenv install flake8 pytest pytest-cov
(p2psimpy env) % pipenv install --dev
```

Run
===

Select the exec shel 

```console
$ pipenv shell
```

Execute Simulation

```console
$ python run.py
```

Test
====

Tests should be put on /tests folder and are executed with the following command.

```console
 $ pytest -v --cov .
```

Linter
======

```console
 $ flake8 --statistics
```

Dependency
==========

Add New Dependency
------------------

```console
$ pipenv install [name]
```

Add New Dev Dependency
----------------------

```console
$ pipenv install [name] --dev
```
