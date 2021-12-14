
import argparse
import os

parser = argparse.ArgumentParser(description='Generating Alignment Pairs.')
parser.add_argument('--output', type=str, default='allpair.aln')
parser.add_argument('-f', '--fatcat', type=str, required=True, help='FATCAT installation path')
parser.add_argument('-d1', '--dir1', type=str, required=True, help='Relative path to the path of the 1st pdb batch')
parser.add_argument('-d2', '--dir2', type=str, required=True, help='Relative path to the path of the 2nd pdb batch')
args = parser.parse_args()

os.environ['FATCAT'] = args.fatcat
pair_path = 'allpair.list'
pairs = []
cwd = os.path.abspath(os.getcwd())

for p1 in os.listdir(args.dir1):
	for p2 in os.listdir(args.dir2):
		p1_full = os.path.join(args.dir1, p1).rsplit('.', 1)[0]
		p2_full = os.path.join(args.dir2, p2).rsplit('.', 1)[0]
		pairs.append('{} {}'.format(p1_full, p2_full))

f = open(pair_path, 'w')
f.write('\n'.join(pairs))

fatcat_batch_script = os.path.join(args.fatcat, 'FATCATMain', 'FATCATQue.pl')
fatcat_batch_command = '{} timeused {} -i {} -q > {}'.format(fatcat_batch_script, pair_path, cwd, args.output)
os.system(fatcat_batch_command)
