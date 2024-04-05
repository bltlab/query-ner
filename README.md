# queryner
## Query segmentation dataset


To create the dataset from offsets, use the following commands:

`conda create -yn queryner python=3.8`

`conda activate queryner`

`pip install -r requirements.txt`

`./prepare_dataset.sh`

The resulting train / dev / test split files will be in the `queryner_data` directory.

To create the create the files with individual annotatations from each of the three annotators on the test set,
run 

`./assemble_individual_annotators.sh`

The resulting annotation files will be in the `individual_annotations` directory.

These scripts will download the original raw queries from the Amazon ESCI dataset and apply the 
QueryNER offsets in order to generate data in the BIO CONLL-style format.
