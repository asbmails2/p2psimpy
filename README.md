
== Env Depencies ==

Used IDE: vscode, plugin python

=== Instal pipenv

pipenv easy the process of managing python dependencies

PIP> $ pip install pyenv
MACOS brew>  $ brew install pipenv 

== Install dependencies 

$ pyenv install 
$ pipenv install
$ pipenv shell
# (p2psimpy env) % pipenv install flake8 pytest pytest-cov
(p2psimpy env) % pipenv install --dev

==  Run 

Select the exec shel 
$ pipenv shell

Execute Simulation
$ python run.py

== Test
 $ pytest -v --cov


== Linter 

 $ flake8 --statistics

== Dependency

=== Add New Dependency
$ pipenv install [name]

=== Add New Dev Dependency
$ pipenv install [name] --dev