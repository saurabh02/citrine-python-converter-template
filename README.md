# citrine-python-converter-template

This is a template for defining converters in python.  It can also be used to guide retrofitting of existing converters.

## Usage

This converter is in the form of a dummy example.
To use it, you'll need to edit some of the files.
There are no templating magicks (at this point).
Let's just go through the files:

### `super_fun_converter`

This directory name is the name of the converter package.
Its good practice to pick a descriptive name, but anything will do.
This should also be the name of your repository.
It is helpful (but not strictly required) if the name doesn't conflict with any existing packages on [PyPI](https://pypi.python.org/pypi).

This directory contains the converter

### `converter.py`

This is a example module that contains a convert method.
You can change the name of the module by renaming the file.
Just be sure it contains a `convert` method that takes keyword arguments.

### `description.yaml`

This file contains a description of the converter that is used when constructing a UI for it.
The main block is list of arguments, giving their name and type along with a description of the argument
and whether it is required or optional.
The example file contains additional information about specifying types.

### `setup.py`

This file describes your converter package.
Change the `name` to whatever you renamed `super_fun_converter` to above.
Also, change the `url` to point to your repository or website.
The `author` and `author_email` fields are optional, but suggested.
`install_requires` should list the external packages your converter uses without version numbers.
Finally, change the `super_fun = ...` line in `entry_points` to name your converter and point to its location.
For example, if you wanted to call the converter `qbox` and it was located in the `qbox_converter` module of `hutch_qbox_converter`
then `entry_points` would read:
```
entry_points={
    'citrine.dice.converter': [
        'qbox = hutch_qbox_converter.qbox_converter',
    ],
}
```

### `requirements.txt`

This file lists all of the python packages needed to run the converter with exact version numbers.
They are automatically installed.

### `Dockerfile`

This file describes the docker container, almost exclusively by inheriting from `citrine-executor-python:latest`.
You shouldn't need to edit this file.

## `convert()` method

what we've just done is define an `extension` that can be used in Citrination's data ingest pipeline
and [command line importer](https://github.com/CitrineInformatics/pif-importer).
The extension is used by calling a method called `convert` with [keyword arguments](https://docs.python.org/3.6/glossary.html#term-argument).
There will always be a keyword argument `files` that is a list of strings.
These are the files that are to be converted into a PIF.
`convert` should return either a PIF or a list of PIFs.
