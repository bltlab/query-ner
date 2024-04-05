#! /bin/bash
set -euo pipefail

if ! test -f shopping_queries_dataset_examples.parquet;
then
  echo "Downloading Amazon ESCI dataset"
  curl -LJO https://github.com/amazon-science/esci-data/raw/main/shopping_queries_dataset/shopping_queries_dataset_examples.parquet
fi

mkdir -p individual_annotations
echo "Assembling the annotations from offset annotation for each individual annotator"
python assemble_dataset.py shopping_queries_dataset_examples.parquet individual_annotator_offsets \
individual_annotations --individual-annotators