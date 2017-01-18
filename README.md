# Pyerror   

Free Error Detection Library In Python




- [Overview](#overview)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)


## Overview

We developed pyerror on Windows but it also run in Linux and Mac-OSX.
pyerror is written in Python3, in order to run it, you will need a python interpereter.
this version of library support this methods :

- Parity-Even
- Parity-Odd
- Repeat
- Hamming
- Checksum
- CRC3
- CRC8
- CRC16
- CRC32



## Dependencies

- [Download](https://www.python.org/downloads/) And Install Last Version Of Python 

## Installation

- [Download](https://github.com/sepandhaghighi/pyerror/archive/v1.1.zip) Pyerror

- Just Unzip It !

## Usage

- `import pyerror`

- create an error detection object `object=pyerror.error_detect("Message String","Method",flag=2)`
* method argument in this object is string


- run generator algorithm on object `error_detect_object=pyerror.convert_gen(object)`
- You can access modified string `error_detect_object.str`

- run detection algorithm on object  `pyerror.convert_det(error_detect_object)`


  Find final result about error in message!!



##License

Please refer to the LICENSE file.

