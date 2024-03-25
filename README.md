# query-ner
The QueryNER dataset, developed by Brandeis University and eBay.

## Query segmentation dataset

In order to prepare the QueryNER dataset, it is necessary to download the original raw queries from the Amazon ESCI dataset and apply the QueryNER offsets in order to generate data in the BIO CONLL-style format.

To do this, use the following commands:

`conda create -n queryner python=3.8 -y`
`conda activate queryner`
`pip install -r requirements.txt`
`./prepare_dataset.sh`

The resulting train / dev / test split files will be in the `queryner_data` directory.