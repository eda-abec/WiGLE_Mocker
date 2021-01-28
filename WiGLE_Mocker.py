#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import csv
import sys


parser = argparse.ArgumentParser (
    description = "WiGLE Mocker (c) 2021 eda-abec",
    epilog = "Example: python3 %(prog)s -i locations.csv -o WigleWifi_mock.csv \
    Or in a colon: cat locations.csv | python3 %(prog)s > WigleWifi_mock.csv"
)

parser.add_argument(
    "-i", "--inputfile",
    type = str,
    #nargs = "+",
    help = "Input CSV file. Must have MAC,CurrentLatitude,CurrentLongitude columns. If not set, input is read from stdin"
)

parser.add_argument(
    "-o", "--outputfile",
    type = str,
    help = "Output CSV file in WiGLE format. If not set, output is written to stdout"
)

parser.add_argument(
    "-d", "--delimiter",
    type = str,
    default = ",",
    help = "Delimiter for output file, like comma (default), semicolon, or anything else"
)

parser.add_argument(
    "-e", "--encoding",
    type = str,
    default = "utf-8",
    help = "Encoding of the input file."
)

args = parser.parse_args()







# you are welcome to fill this with your own nonsense :)
foo_header = "WigleWifi-1.4,appRelease=1,model=PC,release=1,device=PC,display=yes,board=desk,brand=new"

header = "MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,CurrentLatitude,CurrentLongitude,AltitudeMeters,AccuracyMeters,Type"


if args.inputfile != None:
    infile = open(args.inputfile, encoding=args.encoding)
else:
    infile = sys.stdin

APs = []

reader =  csv.DictReader(infile, delimiter=',')
for read_row in reader:
    write_row = dict()
    
    write_row["MAC"]              = read_row["MAC"].lower()
    write_row["CurrentLatitude"]  = read_row["CurrentLatitude"]
    write_row["CurrentLongitude"] = read_row["CurrentLongitude"]
    
    # some foo values
    write_row["SSID"]           = ""
    write_row["AuthMode"]       = "[WPS]"
    write_row["FirstSeen"]      = ""
    write_row["Channel"]        = ""
    write_row["RSSI"]           = "-1"
    write_row["AltitudeMeters"] = ""
    write_row["AccuracyMeters"] = ""
    write_row["Type"]           = "WIFI"
    
    APs.append(write_row)



if args.outputfile != None:
    outfile = open(args.outputfile, 'w', encoding="latin-1")
else:
    outfile = sys.stdout


outfile.write(foo_header + "\n")
writer = csv.DictWriter(outfile, header.split(","), delimiter=args.delimiter)
writer.writeheader()
writer.writerows(APs)



infile.close()
outfile.close()
