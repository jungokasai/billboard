# Instructions for Billboard Submissions
Please use our google form to submit. You can choose the **anonymous** submission option!

## Generator Submission
**[Generator submission form](https://forms.gle/NngKH8PamMhiZ5ZF7)**

Upload a file: `task-name_your-generator-name.jsonl`.
| Key |  |
| ------ | ------ |
| `seg_id` | instance (segmentation) ID |
| `set_id` | ID within the test set (`0-#samples`) |
| hyp | output text |

All past public submissions are in this repository.

* [wmt20-zh-en](https://github.com/jungokasai/billboard/tree/master/submissions/wmt20-zh-en/generators)
* [wmt20-en-de](https://github.com/jungokasai/billboard/tree/master/submissions/wmt20-en-de/generators)
* [cnndm](https://github.com/jungokasai/billboard/tree/master/submissions/cnndm/generators)
* [mscoco](https://github.com/jungokasai/billboard/tree/master/submissions/mscoco/generators)

We also provide [a simple Python script](txt2jsonl.py) that converts a text file to our jsonl format.

## Metric Submission
**[Metric submission form](https://forms.gle/5baVF8bDxhfab8dQ6)**

Share a Github repository link with environment information (e.g., Dockerfile, requirements.txt).
The repository should have `run.sh` that takes as input `source-file.jsonl`, `generator-output.jsonl`, and `reference-file.jsonl`. It then returns `output_scores.txt` that contains one score for each instance per line.

```bash
sh run.sh source-file.jsonl generator-output.jsonl reference-file.jsonl output_scores.txt
```
You can find example repositories below.
* [BLEU](https://github.com/jungokasai/billboard_BLEU)
* [COMET-QE](https://github.com/jungokasai/billboard_COMET-QE)
* [BERTScore](https://github.com/jungokasai/billboard_BERTScore)
* [CLIPScore](https://github.com/jungokasai/billboard_CLIPScore)

You can confirm this works once your environment is set up:
```bash
git clone git@github.com:jungokasai/billboard_BLEU.git
cd billboard_BLEU
sh run.sh samples/wmt20-zh-en_src.jsonl samples/wmt20-zh-en_test-metric.jsonl samples/wmt20-zh-en_refs.jsonl output_scores.txt 
```
`output_scores.txt` should look like this (five lines for five test examples):
```
53.24221584015077
53.472657515726326
71.29598200562626
60.130625227752795
100.00000000000004
```
