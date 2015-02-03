#!/usr/bin/python3
import sys

def chances_phenotype(dom, het, rec):
	'''Return chances of a descendant with the phenotype'''
	tot = float(dom + het + rec)
	chance = dom/tot +\
	het/tot * dom/(tot-1) +\
	het/tot * (het-1)/(tot-1) * 0.75 +\
	het/tot * rec/(tot-1) * 0.5 +\
	rec/tot * het/(tot-1) * 0.5 +\
	rec/tot * dom/(tot-1)
	
	return "%.5f" %(chance)


if __name__ == '__main__':
	filename = sys.argv[1] if len(sys.argv) > 1 else "./files/rosalind_iprb.txt"
	with open(filename) as stream:
		dominant, hetero, recessive = stream.read().replace('\n', '').split(' ')
		print(chances_phenotype(int(dominant), int(hetero), int(recessive)))