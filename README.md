# Bidimensional Leaderboards: Generate and Evaluate Language Hand in Hand


<p align="center">
<a href="https://nlp.cs.washington.edu/billboard/">
<img src="https://github.com/jungokasai/billboard/blob/master/figs/billboard.png" height="300" alt="billboard">
</a>
</p>

## Introduction
We propose a generalization of leaderboards, [**bi**dimensiona**l** **l**eader**boards** (Billboards)](https://nlp.cs.washington.edu/billboard), that simultaneously drives progress in language generation tasks and their evaluation. We accept two types of submissions:

* **Generator developers** submit output text. A Billboard computes all metric scores.
* **Metric developers** submit an executable program. A Billboard computes correlations with the human judgments, updates the ensemble metric, and measures how much it overrates machine over human generations.


**Anonymous submissions** are allowed!!

## Submit 
Submission guides and examples are available [here](https://github.com/jungokasai/billboard/tree/master/submissions/).

## Scoring Results
Scoring results for all past public submissions are available [here](https://github.com/jungokasai/billboard/tree/master/results/).
We have `generator-name||metric-name.csv` files from the Cartesian product between the generators and metrics: each contains instance-level scores.

## Citations
### Bidimesional Leaderboards
```
@misc{kasai2021billboard,
    title   = {Bidimensional Leaderboards: Generate and Evaluate Language Hand in Hand},
    author  = {Jungo Kasai and Keisuke Sakaguchi and Ronan Le Bras and Lavinia Dunagan and Jacob Morrison and Alexander R. Fabbri and Yejin Choi and Noah A. Smith},
    year    = {2021},
    url     = {}, 
}
```
### MSCOCO Captioning Evaluations and THumB 1.0 Protocol
```
@misc{kasai2021thumb,
    title   = {Transparent Human Evaluation for Image Captioning},
    author  = {Jungo Kasai and Keisuke Sakaguchi and Lavinia Dunagan and Jacob Morrison and Ronan Le Bras and Yejin Choi and Noah A. Smith},
    year    = {2021},
    url     = {https://arxiv.org/abs/2111.08940}, 
}
```
### CNNDM Summarization Evaluations
```
@article{fabbri2021summeval,
    title   = {{SummEval}: Re-evaluating Summarization Evaluation},
    author  = {Fabbri, Alexander R and Kry{\'s}ci{\'n}ski, Wojciech and McCann, Bryan and Xiong, Caiming and Socher, Richard and Radev, Dragomir},
    journal = {TACL},
    year    = {2021},
    url     = {https://arxiv.org/abs/2007.12626},
}
```
### WMT20 ZH-EN/EN-DE Machine Translation Evaluations
```
@misc{freitag2021experts,
      title={Experts, Errors, and Context: A Large-Scale Study of Human Evaluation for Machine Translation}, 
      author={Markus Freitag and George Foster and David Grangier and Viresh Ratnakar and Qijun Tan and Wolfgang Macherey},
      year={2021},
      url={https://arxiv.org/abs/2104.14478},
}
```
<p align="center">
<a href="https://allenai.org/">
<img src="https://github.com/jungokasai/THumB/blob/master/figs/ai2_logo.png" height="100" alt="AI2 Logo" style="padding-right:160">
</a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.cs.washington.edu/research/nlp">
<img src="https://github.com/jungokasai/THumB/blob/master/figs/uwnlp_logo.png" height="100" alt="UWNLP Logo">
</a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.salesforce.com/">
<img src="https://raw.githubusercontent.com/Yale-LILY/SummEval/master/assets/logo-salesforce.svg" height="70" alt="Salesforce Logo">
</a>
</p>
