# Generate vendor MO tables SQL
#
# python generate_vendor_mo_tables.py ericsson ericsson_bulkcm_parser.cfg
#
#

import sys
import os 

vendor = sys.argv[1]
param_file = sys.argv[2]

schema = "{}_cm".format(vendor)

f = open(param_file, "r")

for line in f:
	mo_name = line.split(":")[0]
	print("CREATE TABLE {}.\"{}\" ( id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, load_datetime timestamp DEFAULT CURRENT_TIMESTAMP, data jsonb NOT NULL); ".format(schema, mo_name))