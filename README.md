# Photoshop Convert

psdconvert is a Python package for efficiently converting photoshop files into another image format.

_Photoshop is an essential tool for many projects, often times we find ourselves working on a large number of files that are must be saved in a smaller format (such as .png).  psdconvert simplifies this process by converting psd files without the overhead of a GUI._


### How it works

PSD Convert is built with the psd_tools package and the PSDImage class as the method for creating objects from photoshop files.  The ConvertPSD method accepts the source file path and the destination file path (new file name and file type is part of this arg) as arguments and saves the newly converted file to the specified destination.  The BatchConvertPSD method accepts a directory containing photoshop files as the source and an existing directory as the destination.  ConvertPSD is the driver of the BatchConvertPSD class.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Upgrade to the latest version of pip

```
pip install --upgrade pip
```

### Installing

Create a virtual development environment and install the latest version of psdconvert from PyPi or github

PyPi distribution

```
pip install psdconvert
```

GitHub distribution

```
pip install git+git://github.com/mrstephenneal/psdconvert.git
```
or

```
pip install git+https://github.com/mrstephenneal/psdconvert.git
```

## Example Usage

Outlined below are basic uses of the four main classes of the PSD Convert python package.

* ConvertPSD - Converts PSD file into another image format
* BatchConvertPSD - Converts directory of PSD files into another image format

### ConvertPSD class

This class converts a singular PSD file into another format.  Is also used in conjunction with the BatchConvertPSD cass.

Same directory example

```python
old_file = 'test.psd'
new_file = 'test.png'
ConvertPSD(old_file, new_file)
```

New directory example

```python
old_file = 'psds/test.psd'
new_file = 'pngs/test.png'
ConvertPSD(old_file, new_file)
```

### BatchConvertPSD class

This class converts a folder full of PSD file into another format, new files are saved to the destination folder.

Example

```python
old_psd_files = 'test/psd'
new_png_files = 'test/png'
BatchConvertPSD(old_psd_files, new_png_files)
```

## Built With

* [docopt](https://docopt.org) - Pythonic argument parser, that will make you smile
* [Pillow](https://python-pillow.org) - Python Imaging Library
* [psd_tools](https://python-pillow.org) - Python package for working with Adobe Photoshop files
* [tqdm](https://github.com/tqdm/tqdm) - A fast, extensible progress bar for Python

## Contributing

Please read [CONTRIBUTING.md](https://github.com/mrstephenneal/psdconvert/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/dirutility/tags). 

## Authors

* **Stephen Neal** - *Initial work* - [StephenNeal](https://github.com/mrstephenneal)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details