# kodamas


File event driven Shell Executer.

It is created as a development tool intended to be used when you want to automatically execute the intended Shell when updating target files.

## Venefit
- easy installation 
  - privilege are not require for installation
  - less dependency (need python and libc)
  - clear code
  - aim to work with python>=2.7,3.5
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
usage: kodamas [-h] -d PATH -s SHELL [-e EXTENSIONS]

optional arguments:
  -h, --help            show this help message and exit
  -d PATH, --dir PATH   (required) Write the absolute path to the directory
                        whose change you want to detect
  -s SHELL, --shell SHELL
                        (required) The Shell you want to execute when changing
                        the files
  -e EXTENSIONS, --ext EXTENSIONS
                        (not required, default=all) Extension List that
                        separated by comma. If the update file extension is
                        included in this option, Shell will be executed.
                        Otherwise not do anything. (e.g. -e py,txt,log
```
(e.g.
```sh
kodamas -d /tmp -s 'gcc /tmp/file.c -o file'
```

## License

Note Content distributed under the [MIT License](http://opensource.org/licenses/MIT).