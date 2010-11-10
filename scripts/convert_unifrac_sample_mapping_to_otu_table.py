#! /usr/bin/env python

__author__ = "Cathy Lozupone"
__copyright__ = "Copyright 2010, The QIIME project"
__credits__ = ["Catherine Lozupone"]
__license__ = "GPL"
__version__ = "1.2.0"
__maintainer__ = "Cathy Lozupone"
__email__ = "lozupone@colorado.edu"
__status__ = "Release"

from qiime.parse import parse_sample_mapping, sample_mapping_to_otu_table
from optparse import make_option
from qiime.util import parse_command_line_parameters


script_info={}
script_info['brief_description']="""Convert a UniFrac sample mapping file to an OTU table"""
script_info['script_description']="""This script allows users that have already created sample mapping (environment) files for use with the Unifrac web interface to use QIIME. QIIME records this data in an OTU table."""
script_info['script_usage']=[]
script_info['script_usage'].append(("""Example:""","""Convert a sample_mapping.txt file into an OTU table (e.g. otu_table.txt): ""","""convert_unifrac_sample_mapping_to_otu_table.py -i sample_mapping.txt -o otu_table.txt"""))
script_info['output_description']="""The result of this script is an OTU table."""
script_info['required_options']=[\
    make_option('-i', '--sample_mapping_fp', dest='sample_mapping_fp',\
        help='path to the sample mapping file'),
    make_option('-o', '--output_fp', dest='output_fp', \
        help='path to output file')]

script_info['version'] = __version__

def main():
    option_parser, opts, args = parse_command_line_parameters(**script_info)

    sample_mapping_fp = opts.sample_mapping_fp
    output_fp = opts.output_fp
    verbose = opts.verbose
    
    sample_mapping_file = open(sample_mapping_fp, 'U')
    result = sample_mapping_to_otu_table(sample_mapping_file)
    of = open(output_fp, 'w')
    of.write('\n'.join(result))
    of.close()

if __name__ == "__main__":
    main()

