# WiGLE Mocker
A Python script to convert manual entries to WiGLE compliant format

Purpose of this script is to convert few manually gathered networks to WiGLE format - it fills missing columns with placeholder values and adds the pre-header.

## Usage

WiGLE Mocker can be used in two ways - either in a shell colon, or with input and output files as arguments.

from help:
```
usage: WiGLE_Mocker.py [-h] [-i INPUTFILE] [-o OUTPUTFILE] [-d DELIMITER] [-e ENCODING]

WiGLE Mocker (c) 2021 eda-abec

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        Input CSV file. Must have MAC,CurrentLatitude,CurrentLongitude
                        columns. If not set, input is read from stdin
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        Output CSV file in WiGLE format. If not set, output is written to
                        stdout
  -d DELIMITER, --delimiter DELIMITER
                        Delimiter for output file, like comma (default), semicolon, or
                        anything else
  -e ENCODING, --encoding ENCODING
                        Encoding of the input file.

Example: python3 WiGLE_Mocker.py -i locations.csv -o WigleWifi_mock.csv
Or in a colon: cat locations.csv | python3 WiGLE_Mocker.py > WigleWifi_mock.csv
```

## Input
A .csv file with these columns, specified on file's first line:
```
MAC,CurrentLatitude,CurrentLongitude
```
The MAC address can be either in lowercase or uppercase.

## Output
A .csv file in [WiGLE format](https://api.wigle.net/csvFormat.html). `latin-1` encoded, with following pre-header:
```
WigleWifi-1.4,appRelease=1,model=PC,release=1,device=PC,display=yes,board=desk,brand=new
```


## TODOs
- check for entries in real WiGLE CSV and throw warning if it already contains the network

## Acknowledgements
Author: [eda-abec](https://github.com/eda-abec)\
Date: 01/2021
