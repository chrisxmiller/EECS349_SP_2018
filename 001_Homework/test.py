import math
from parse import parse
import ID3
import sys
from node import Node
import random
import copy
import numpy as np

import matplotlib.pyplot as plt


def find_best_attribute_test():
  attributes = [{'handicapped-infants': 'n', 'export-administration-act-south-africa': 'y', 'superfund-right-to-sue': 'y', 'education-spending': 'y', 'duty-free-exports': 'n', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'y', 'physician-fee-freeze': 'y', 'el-salvador-aid': 'y', 'religious-groups-in-schools': 'y', 'mx-missile': 'n', 'synfuels-corporation-cutback': '?', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'y', 'adoption-of-the-budget-resolution': 'n', 'Class': 'republican'}, 
                {'handicapped-infants': 'n', 'export-administration-act-south-africa': '?', 'superfund-right-to-sue': 'y', 'education-spending': 'y', 'duty-free-exports': 'n', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'y', 'el-salvador-aid': 'y', 'religious-groups-in-schools': 'y', 'mx-missile': 'n', 'synfuels-corporation-cutback': 'n', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'y', 'adoption-of-the-budget-resolution': 'n', 'Class': 'republican'}, 
                {'handicapped-infants': '?', 'export-administration-act-south-africa': 'n', 'superfund-right-to-sue': 'y', 'education-spending': 'n', 'duty-free-exports': 'n', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': '?', 'el-salvador-aid': 'y', 'religious-groups-in-schools': 'y', 'mx-missile': 'n', 'synfuels-corporation-cutback': 'y', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'y', 'adoption-of-the-budget-resolution': 'y', 'Class': 'democrat'}, 
                {'handicapped-infants': 'n', 'export-administration-act-south-africa': 'y', 'superfund-right-to-sue': 'y', 'education-spending': 'n', 'duty-free-exports': 'n', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'n', 'el-salvador-aid': '?', 'religious-groups-in-schools': 'y', 'mx-missile': 'n', 'synfuels-corporation-cutback': 'y', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'n', 'adoption-of-the-budget-resolution': 'y', 'Class': 'democrat'}, 
                {'handicapped-infants': 'y', 'export-administration-act-south-africa': 'y', 'superfund-right-to-sue': 'y', 'education-spending': '?', 'duty-free-exports': 'y', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'n', 'el-salvador-aid': 'y', 'religious-groups-in-schools': 'y', 'mx-missile': 'n', 'synfuels-corporation-cutback': 'y', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'y', 'adoption-of-the-budget-resolution': 'y', 'Class': 'democrat'}, 
                {'handicapped-infants': 'n', 'export-administration-act-south-africa': 'y', 'superfund-right-to-sue': 'y', 'education-spending': 'n', 'duty-free-exports': 'y', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'n', 'el-salvador-aid': 'y', 'religious-groups-in-schools': 'y', 'mx-missile': 'n', 'synfuels-corporation-cutback': 'n', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'y', 'adoption-of-the-budget-resolution': 'y', 'Class': 'democrat'}, 
                {'handicapped-infants': 'n', 'export-administration-act-south-africa': 'y', 'superfund-right-to-sue': '?', 'education-spending': 'n', 'duty-free-exports': 'y', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'y', 'el-salvador-aid': 'y', 'religious-groups-in-schools': 'y', 'mx-missile': 'n', 'synfuels-corporation-cutback': 'n', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'y', 'adoption-of-the-budget-resolution': 'y', 'Class': 'democrat'}, 
                {'handicapped-infants': 'n', 'export-administration-act-south-africa': 'y', 'superfund-right-to-sue': 'y', 'education-spending': 'n', 'duty-free-exports': '?', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'y', 'el-salvador-aid': 'y', 'religious-groups-in-schools': 'y', 'mx-missile': 'n', 'synfuels-corporation-cutback': 'n', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'y', 'adoption-of-the-budget-resolution': 'n', 'Class': 'republican'}, 
                {'handicapped-infants': 'n', 'export-administration-act-south-africa': 'y', 'superfund-right-to-sue': 'y', 'education-spending': 'y', 'duty-free-exports': 'n', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'y', 'el-salvador-aid': 'y', 'religious-groups-in-schools': 'y', 'mx-missile': 'n', 'synfuels-corporation-cutback': 'n', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'y', 'adoption-of-the-budget-resolution': 'n', 'Class': 'republican'}, 
                {'handicapped-infants': 'y', 'export-administration-act-south-africa': '?', 'superfund-right-to-sue': 'n', 'education-spending': 'n', 'duty-free-exports': '?', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'n', 'el-salvador-aid': 'n', 'religious-groups-in-schools': 'n', 'mx-missile': 'y', 'synfuels-corporation-cutback': 'n', 'anti-satellite-test-ban': 'y', 'water-project-cost-sharing': 'y', 'crime': 'n', 'adoption-of-the-budget-resolution': 'y', 'Class': 'democrat'}, 
                {'handicapped-infants': 'n', 'export-administration-act-south-africa': 'n', 'superfund-right-to-sue': 'y', 'education-spending': '?', 'duty-free-exports': 'n', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'y', 'el-salvador-aid': 'y', 'religious-groups-in-schools': 'n', 'mx-missile': 'n', 'synfuels-corporation-cutback': '?', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'y', 'adoption-of-the-budget-resolution': 'n', 'Class': 'republican'}, 
                {'handicapped-infants': 'n', 'export-administration-act-south-africa': '?', 'superfund-right-to-sue': 'y', 'education-spending': '?', 'duty-free-exports': '?', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'y', 'el-salvador-aid': 'y', 'religious-groups-in-schools': 'y', 'mx-missile': 'n', 'synfuels-corporation-cutback': 'y', 'anti-satellite-test-ban': 'n', 'water-project-cost-sharing': 'y', 'crime': 'y', 'adoption-of-the-budget-resolution': 'n', 'Class': 'republican'}, 
                {'handicapped-infants': 'n', 'export-administration-act-south-africa': '?', 'superfund-right-to-sue': 'y', 'education-spending': 'n', 'duty-free-exports': '?', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'n', 'physician-fee-freeze': 'n', 'el-salvador-aid': 'n', 'religious-groups-in-schools': 'n', 'mx-missile': 'y', 'synfuels-corporation-cutback': 'n', 'anti-satellite-test-ban': 'y', 'water-project-cost-sharing': 'y', 'crime': 'n', 'adoption-of-the-budget-resolution': 'y', 'Class': 'democrat'}, 
                {'handicapped-infants': 'y', 'export-administration-act-south-africa': '?', 'superfund-right-to-sue': 'n', 'education-spending': '?', 'duty-free-exports': 'y', 'aid-to-nicaraguan-contras': 'n', 'immigration': 'y', 'physician-fee-freeze': 'n', 'el-salvador-aid': 'n', 'religious-groups-in-schools': 'y', 'mx-missile': '?', 'synfuels-corporation-cutback': 'y', 'anti-satellite-test-ban': 'y', 'water-project-cost-sharing': 'y', 'crime': 'n', 'adoption-of-the-budget-resolution': 'y', 'Class': 'democrat'}]
  assert(ID3.findBestAttribute(attributes) == 'adoption-of-the-budget-resolution')
  print "Passed test: find_best_attribute_test()\n"



data = parse('house_votes_84.data')


find_best_attribute_test()
a = [1,2,3,4,5,6,7]
random.shuffle(a)
print a
print a[1]
random.shuffle(a)
print a
print a[1]
a[1]