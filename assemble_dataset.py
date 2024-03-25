import json
import os
from argparse import ArgumentParser
from typing import Dict, Optional

import pandas as pd


EXAMPLE_ID = 'example_id'
QUERY = "query"
LABELS = "labels"

def assemble_file(filename: str, offsets_dir: str, outdir: str, id_to_query_map: Dict[int, str]):
    offset_path = os.path.join(offsets_dir, f"{filename}.jsonl")
    outpath = os.path.join(outdir, f"{filename}.txt")

    with open(outpath, 'w', encoding='utf8') as outfile, open(offset_path, 'r', encoding='utf8') as infile:
        for line in infile:
            fields = json.loads(line.strip())
            idx = int(fields[EXAMPLE_ID])
            labels = fields[LABELS]
            query = id_to_query_map.get(idx, None)
            if query is None:
                raise ValueError(f"No query found for example id: {idx}")
            tokens = query.strip().split()
            assert len(tokens) == len(labels), f"Mismatch in queries and tokens\n{idx}\n{tokens}\n{labels}"
            for token, label in zip(tokens, labels):
                print(f"{token}\t{label}", file=outfile)
            print(file=outfile)


def assemble_dataset():
    parser = ArgumentParser()
    parser.add_argument("esci_path")
    parser.add_argument("offsets_dir")
    parser.add_argument("out_dir")
    args = parser.parse_args()

    id_to_query_map = read_parquet_to_id_map(args.esci_path)

    print("Building training dataset...")
    assemble_file('train', args.offsets_dir, args.out_dir, id_to_query_map)
    print("Building dev dataset...")
    assemble_file('dev', args.offsets_dir, args.out_dir, id_to_query_map)
    print("Building test dataset...")
    assemble_file('test', args.offsets_dir, args.out_dir, id_to_query_map)


def read_parquet_to_id_map(esci_path: str, product_locale: Optional[str] = None):
    print("Reading ESCI dataset and building id to query mapping...")
    df_examples = pd.read_parquet(esci_path)
    id_to_query_map = {}
    for i in df_examples.index:
        exampleid = df_examples[EXAMPLE_ID][i]
        query = df_examples[QUERY][i]
        if product_locale: # us, jp, es
            if df_examples["product_locale"][i] != product_locale:
                continue
        id_to_query_map[exampleid] = query
    return id_to_query_map


if __name__ == "__main__":
    assemble_dataset()