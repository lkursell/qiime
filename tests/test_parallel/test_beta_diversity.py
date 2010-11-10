#!/usr/bin/env python
# File created on 20 Oct 2010
from __future__ import division

__author__ = "Greg Caporaso"
__copyright__ = "Copyright 2010, The QIIME project"
__credits__ = ["Greg Caporaso"]
__license__ = "GPL"
__version__ = "1.2.0"
__maintainer__ = "Greg Caporaso"
__email__ = "gregcaporaso@gmail.com"
__status__ = "Release"
 

from cogent.util.unit_test import TestCase, main
from qiime.parallel.beta_diversity import assemble_distance_matrix
from qiime.parse import parse_distmat_to_dict

class ParallelBetaDiversityTests(TestCase):
    
    def setUp(self):
        """ """
        self.dm_comp1 = dm_comp1.split('\n')
        self.dm_comp2 = dm_comp2.split('\n')
        self.dm_comp3 = dm_comp3.split('\n')
        self.dm_comp4 = dm_comp4.split('\n')
        self.expected = expected.split('\n')
    
    def test_assemble_distance_matrix(self):
        """ assemble_distance_matrix functions as expected for a non-symmetric dm
        """
        actual = parse_distmat_to_dict(assemble_distance_matrix(
         [self.dm_comp1,self.dm_comp2,self.dm_comp3,self.dm_comp4]).split('\n'))
        exp = parse_distmat_to_dict(self.expected)
        self.assertEqual(actual,exp)
        
dm_comp1 = """	PC.354	PC.355	PC.356	PC.481	PC.593	PC.607	PC.634	PC.635	PC.636
PC.354	0.0	0.9999	0.637204555763	0.596124964451	0.59620370837	0.736037238732	0.790494137353	0.70551354446	0.758236466255
PC.355	0.623372333874	0.0	0.613486299912	0.631198829777	0.672502144191	0.766682588739	0.732473435165	0.738434734323	0.687363838411"""

dm_comp2 = """	PC.354	PC.355	PC.356	PC.481	PC.593	PC.607	PC.634	PC.635	PC.636
PC.356	0.637204555763	0.613486299912	0.0	0.691902878696	0.742922266508	0.740684448418	0.78590671873	0.723519724117	0.754301399992
PC.481	0.596124964451	0.631198829777	0.691902878696	0.0	0.668731241507	0.690956885033	0.652257003318	0.652311676944	0.661223123598"""

dm_comp3 = """	PC.354	PC.355	PC.356	PC.481	PC.593	PC.607	PC.634	PC.635	PC.636
PC.593	0.59620370837	0.672502144191	0.742922266508	0.668731241507	0.0	0.74048244192	0.760255173866	0.761741286862	0.751777287666
PC.607	0.736037238732	0.766682588739	0.740684448418	0.690956885033	0.74048244192	0.0	0.73093223871	0.688768250911	0.729047763792"""

dm_comp4 = """	PC.354	PC.355	PC.356	PC.481	PC.593	PC.607	PC.634	PC.635	PC.636
PC.634	0.790494137353	0.732473435165	0.78590671873	0.652257003318	0.760255173866	0.73093223871	0.0	0.583577161959	0.596033900207
PC.635	0.70551354446	0.738434734323	0.723519724117	0.652311676944	0.761741286862	0.688768250911	0.583577161959	0.0	0.6271222318
PC.636	0.758236466255	0.687363838411	0.754301399992	0.661223123598	0.751777287666	0.729047763792	0.596033900207	0.6271222318	0.0"""

expected = """	PC.354	PC.355	PC.356	PC.481	PC.593	PC.607	PC.634	PC.635	PC.636
PC.354	0.0	0.9999	0.637204555763	0.596124964451	0.59620370837	0.736037238732	0.790494137353	0.70551354446	0.758236466255
PC.355	0.623372333874	0.0	0.613486299912	0.631198829777	0.672502144191	0.766682588739	0.732473435165	0.738434734323	0.687363838411
PC.356	0.637204555763	0.613486299912	0.0	0.691902878696	0.742922266508	0.740684448418	0.78590671873	0.723519724117	0.754301399992
PC.481	0.596124964451	0.631198829777	0.691902878696	0.0	0.668731241507	0.690956885033	0.652257003318	0.652311676944	0.661223123598
PC.593	0.59620370837	0.672502144191	0.742922266508	0.668731241507	0.0	0.74048244192	0.760255173866	0.761741286862	0.751777287666
PC.607	0.736037238732	0.766682588739	0.740684448418	0.690956885033	0.74048244192	0.0	0.73093223871	0.688768250911	0.729047763792
PC.634	0.790494137353	0.732473435165	0.78590671873	0.652257003318	0.760255173866	0.73093223871	0.0	0.583577161959	0.596033900207
PC.635	0.70551354446	0.738434734323	0.723519724117	0.652311676944	0.761741286862	0.688768250911	0.583577161959	0.0	0.6271222318
PC.636	0.758236466255	0.687363838411	0.754301399992	0.661223123598	0.751777287666	0.729047763792	0.596033900207	0.6271222318	0.0"""

if __name__ == "__main__":
    main()