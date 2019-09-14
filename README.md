# BiMPM: Bilateral Multi-Perspective Matching for Natural Language Sentences

## Updates (Sep, 2019)
* This repository is orginated from zhiguowang/BiMPM
* Convert code to python3

## Description

## Requirements
* python 3.6
* tensorflow 1.5

## Data format
Both the train and test sets require a tab-separated format.
Each line in the train (or test) file corresponds to an instance, and it should be arranged as
> label	sentence#1	sentence#2 instanceID	

For more details about the data format, you can download the [SNLI](https://drive.google.com/file/d/1CxjKsaM6YgZPRKmJhNn7WcIC3gISehcS/view?usp=sharing) and the [Quora Question Pair](https://drive.google.com/file/d/0B0PlTAo--BnaQWlsZl9FZ3l1c28/view?usp=sharing) datasets used in our [paper](https://arxiv.org/pdf/1702.03814.pdf).


## Training
You can find the training script at BiMPM/src/SentenceMatchTrainer.py

First, edit the configuration file at ${workspace}/BiMPM/configs/snli.sample.config (or ${workspace}/BiMPM/configs/quora.sample.config ).
You need to change the "train\_path", "dev\_path", "word\_vec\_path", "model\_dir", "suffix" to your own setting.

Second, launch job using the following command line
> python  ${workspace}/BiMPM/SentenceMatchTrainer.py --config\_path ${workspace}/BiMPM/configs/snli.sample.config


## Testing
You can find the testing script at BiMPM/src/SentenceMatchDecoder.py
> python  ${workspace}/BiMPM/src/SentenceMatchDecoder.py --in\_path ${your\_path\_to}/dev.tsv --word\_vec\_path ${your\_path\_to}/wordvec.txt --out\_path ${your\_path\_to}/result.json --model\_prefix ${model\_dir}/SentenceMatch.${suffix}

Where "model\_dir" and "suffix" are the variables set in your configuration file.

The output file is a json file with the follwing format.

```javascript
{
    { 
        "ID": "instanceID",
        "truth": label,
        "sent1": sentence1,
        "sent2": sentence2,
        "prediction": prediciton,
        "probs": probs_for_all_possible_labels
    },
    { 
        "ID": "instanceID",
        "truth": label,
        "sent1": sentence1,
        "sent2": sentence2,
        "prediction": prediciton,
        "probs": probs_for_all_possible_labels
    }
}
```
