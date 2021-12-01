import argparse, json, jsonlines

parser = argparse.ArgumentParser(allow_abbrev=False)
parser.add_argument('--src', type=str, metavar='N',
                    help='source file', default='wmt20-zh-en/source/wmt20-zh-en_src.jsonl')
parser.add_argument('--hyp', type=str, metavar='N',
                    help='hypothesis output file', default='wmt20-zh-en_test-converter.txt')
args = parser.parse_args()

def text2jsonl(src, hyp):
    outputs = []
    with open(src, 'r') as f_src:
        with open(hyp, 'r') as f_hyp:
            for src_sent, hyp_sent in zip(f_src, f_hyp):
                src_sent = json.loads(src_sent.strip())
                hyp_sent = hyp_sent.strip()
                output = {}
                output['seg_id'] = src_sent['seg_id']
                output['set_id'] = src_sent['set_id']
                output['hyp'] = hyp_sent
                outputs.append(output)
    with jsonlines.open(hyp.replace('.txt', '.jsonl'), 'w') as fout:
        fout.write_all(outputs)

if __name__ == '__main__':
    text2jsonl(args.src, args.hyp)
