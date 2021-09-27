# MTDsites
Sequence-based protein binding site prediction through multiple-task deep neural networks

This is the standalone code for our paper: [To improve the predictions of binding residues with DNA, RNA, carbohydrate, and peptide via multiple-task deep neural networks](https://https://www.biorxiv.org/content/10.1101/2020.02.11.943571v1)

![MTDsites_framework](https://github.com/biomed-AI/MTDsite/blob/master/IMG/MTDsites_framework.png)

## Predict protein binding sites using the pre-trained MTDsites model

**Note:**

**This is a demo for the prediction of the sequence `5fez_A` with its preprocessed feature files. You can directly type `$ sh run.sh 5fez_A`, and then the result file `result.data` will be generated in the current directory.**

If you want to predict your own protein sequence using our pre-trained model, please refer to the steps below:

### Step 1: Prepare your sequence fasta file
We follow the common fasta file format that starts with `>{protein sequence name}`, and then the protein sequence is placed in the next line. This is the fasta of our demo `5fez_A`:

```
>5fez_A
MWSHPQFEKASTGREILEKLERREFTREVLKEALSINDRGFNEALFKLADEIRRKYVGDEVHIRAIIEFSNVCRKNCLYCGLRRDNKNLKRYRMTPEEIVERARLAVQFGAKTIVLQSGEDPYYMPDVISDIVKEIKKMGVAVTLSLGEWPREYYEKWKEAGADRYLLRHETANPVLHRKLRPDTSFENRLNCLLTLKELGYETGAGSMVGLPGQTIDDLVDDLLFLKEHDFDMVGIGPFIPHPDTPLANEKKGDFTLTLKMVALTRILLPDSNIPATTAMGTIVPGGREITLRCGANVIMPNWTPSPYRQLYQLYPGKISVFEKDTASIPSVMKMIELLGRKPGRDWGGRKRVFETV
```

**Note:**

(1) Please make sure the name of the fasta file corresponds to the names of the feature files in `./feature/`.

(2) Please name your fasta file **without** any suffix to advoid unexpected error, such as `5fez_A` instead of `5fez_A.fasta` or `5fez_A.fa`.

### Step 2: Prepare the feature files
**Note:**

(1) We don't integrate the feature generation pipeline in this repository, so please use the recommend softwares (see the table below) to generate the feature files!

(2) We have deployed the feature generation softwares in our server to calculate the features. You can use the web server if your input is small.

(3) **THIS STEP WILL COST MOST OF THE TIME !!** (The sequence with more amino acids will cost longer time, so we recommend you to use the protein sequence less than 1000 amino acids.)

| Software | Version | Input | Output |
| -------- | -------- | -------- | --------|
| [PSI-BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastSearch&PROGRAM=blastp&BLAST_PROGRAMS=psiBlast) | v2.7.1 | 5fez_A | 5fez_A.bla, 5fez_A.pssm |
| [HH-Suite3](https://github.com/soedinglab/hh-suite) | v3.0.3 | 5fez_A | 5fez_A.hhr, 5fez_A.hhm, 5fez_A.a3m |
| [SPIDER3](https://sparks-lab.org/server/spider3/) | v1.0 | 5fez_A, 5fez_A.pssm, 5fez_A.hhm | 5fez_A.spd33 |

Then put `5fez_A.pssm`, `5fez_A.hhm` and `5fez_A.spd33` under the folder `./feature/` (We have already provided these files as an example). Other precautions when using the feature generation softwares should be referred to the corresponding software documents.

### Step 3: Run the predict code
```
$ sh run.sh 5fez_A
```
The prediction results will be stored in `./result.data`.

## The web server of MTDsites
Our platform are freely available for academic use only.

[http://biomed.nscc-gz.cn/server/MTDsite/](http://biomed.nscc-gz.cn/server/MTDsite/)

## Required packages
The code has been tested under Python 3.8.5, with the following packages installed (along with their dependencies):
- torch==1.6.0
- numpy==1.19.1

## Datasets in our paper

See the four directories under `./Dataset` with the binding site data for DNA, RNA, carbohydrate, and peptide. In each directory, the files include training and tested lists, as well as the curated features. The files explain themselves well.

Reference to collectively use the four datasets:

*Z Sun, S Zheng, H Zhao, Zhangming Niu, Yutong Lu, Yi Pan, Yuedong Yang. To improve the predictions of binding residues with DNA, RNA, carbohydrate, and peptide via multiple-task deep neural networks. TCBB (In press) bioRxiv 2020.02.11.943571.*

Please also see original references for the datasets:

Carbohydrate: *Zhao H, Yang Y, Von Itzstein M, et al. Carbohydrate binding protein identification by coupling structural similarity searching with binding affinity prediction[J]. Journal of computational chemistry, 2014, 35(30): 2177-2183.*

Peptide: *Taherzadeh G, Y Zhou, AW Liew, Yuedong Yang. Structure-based prediction of protein-peptide binding regions using Random Forest. Bioinformatics 2018 Feb 1;34(3):477-484.*

DNA/RNA: *Yan J, Kurgan L. DRNApred, fast sequence-based method that accurately predicts and discriminates DNA-and RNA-binding residues. Nucleic acids research, 2017, 45(10): e84-e84.*
