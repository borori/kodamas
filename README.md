# kodamas


File event driven Shell Executer.

It is created as a development tool intended to be used when you want to automatically execute the intended Shell when updating target files.

## Venefit
- easy installation 
  - privilege are not require for installation
  - less dependency (need python and libc)
  - clear code
  - aim to work with python 2.7 or higher
- easy useful
  - less configuration


## Installation

This is not distributing to PyPI, only github.

simple way
```sh
pip install --user git+https://github.com/borori/kodamas
```
another way 
```sh
# git clone or download zip
cd {kodamas directory}
pip install --user --upgrade .
```
```sh
# git clone or download zip
export PYTHONPATH={absolute kodamas directory}
{kodamas directory}/bin/kodamas -s ... -m ...
```

## Usage
```sh
usage: kodamas [-h] [-m MONITOR] [-s SHELL]

optional arguments:
  -h, --help            show this help message and exit
  -m MONITOR, --monitor MONITOR
                        Write the absolute path to the file or directory whose
                        change you want to detect
  -s SHELL, --shell SHELL
                        The Shell you want to execute when changing the files
```
e.g.
```sh
kodamas -m /tmp/file.c -s 'gcc /tmp/file.c -o sample'
kodamas -m /tmp -s 'cd /tmp && make && make test'
```

## License

Note Content distributed under the [MIT License](http://opensource.org/licenses/MIT).