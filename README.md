# german-tbo-release

German Target Based Offensive (TBO) Language dataset .   

## Warning

This dataset contains offensive German language.

# License

## Data License

We are releasing the data under the [CDLA - Permissive - Version 2.0 license](data/LICENSE) with the restriction that the data must not be used to build any system for the purpose of generating the type of offensive language found in this dataset.

## Software License

We are releasing the software under the [Apache 2.0 license](scripts/LICENSE).

# Installation

```
pip install pandas
```

# Data Generation

1. Download original `Germeval-2018` data from here: [Germeval-2018](https://github.com/uds-lsv/GermEval-2018-Data) .
2. Copy or link the training data `germeval2018.training.txt` to the work directory.
3. Anonymize the twitter handles using the `anonymize_twitter_data.py` script:
```
python scripts/anonymize_twitter_data.py germeval2018.training.txt data/germeval2018.training_anonymized.txt
```
4. Create the full annotation data:

```
python scripts/create_full_annotation.py -i data/germeval2018.training_anonymized.txt -t data/german_tbo_anonymized.csv -o data/germeval2018.training_full.txt
```


# MUTED paper

The German TBO dataset is described in the MUTED paper: https://aclanthology.org/2023.emnlp-demo.19/ .

```
@inproceedings{tillmann-etal-2023-muted,
    title = "Muted: Multilingual Targeted Offensive Speech Identification and Visualization",
    author = "Tillmann, Christoph  and
      Trivedi, Aashka  and
      Rosenthal, Sara  and
      Borse, Santosh  and
      Zhang, Rong  and
      Sil, Avirup  and
      Bhattacharjee, Bishwaranjan",
    editor = "Feng, Yansong  and
      Lefever, Els",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-demo.19",
    doi = "10.18653/v1/2023.emnlp-demo.19",
    pages = "229--236",
    abstract = "Offensive language such as hate, abuse, and profanity (HAP) occurs in various content on the web. While previous work has mostly dealt with sentence level annotations, there have been a few recent attempts to identify offensive spans as well. We build upon this work and introduce MUTED, a system to identify multilingual HAP content by displaying offensive arguments and their targets using heat maps to indicate their intensity. MUTED can leverage any transformer-based HAP-classification model and its attention mechanism out-of-the-box to identify toxic spans, without further fine-tuning. In addition, we use the spaCy library to identify the specific targets and arguments for the words predicted by the attention heatmaps. We present the model{'}s performance on identifying offensive spans and their targets in existing datasets and present new annotations on German text. Finally, we demonstrate our proposed visualization tool on multilingual inputs.",
}
```

# Misc

Please direct any questions at  Sara Rosenthal (`sjrosenthal@us.ibm.com`) or Christoph Tillmann (`ctill@us.ibm.com`) . 
