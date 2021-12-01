import argparse, json

parser = argparse.ArgumentParser(allow_abbrev=False)
parser.add_argument('--hyp', type=str, metavar='N',
                    help='hypothesis output file', default='wmt20-zh-en_test-converter.jsonl')
args = parser.parse_args()

def jsonl2txt(hyp):
    outputs = []
    with open(hyp, 'r') as f_in:
        for line in f_in:
            outputs.append(json.loads(line.strip())['hyp'])
    with open(hyp.replace('.jsonl', '.txt'), 'wt') as fout:
        fout.write('\n'.join(outputs))

if __name__ == '__main__':
    jsonl2txt(args.hyp)
