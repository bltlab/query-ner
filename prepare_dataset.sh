#! /bin/bash
set -euo pipefail

echo "Downloading Amazon ESCI dataset"
curl -LJO https://github.com/amazon-science/esci-data/raw/main/shopping_queries_dataset/shopping_queries_dataset_examples.parquet


mkdir -p queryner_data
echo "Assembling the dataset from offset annotation"
python assemble_dataset.py shopping_queries_dataset_examples.parquet offset-splits queryner_data