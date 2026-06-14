import torch
from datasets import load_dataset
import math
import regex as re
import tiktoken

import time

import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets
from torchvision.transforms import v2
import torch.nn as nn
from torch.nn import functional as F

import matplotlib.pyplot as plt





def gets_stats(get_token):
    count = {}

    for i in range(len(get_token) - 1):
        if tuple(get_token[i:i + 2]) not in count.keys():
            count[tuple(get_token[i:i + 2])] = 1
        else:
            count[tuple(get_token[i:i + 2])] += 1
    return count
            

if __name__ == "__main__":
    print("Main Start")
    
    if
    
    ds = load_dataset(
        "roneneldan/TinyStories",
        split="train",
        cache_dir="/data/TinyStories"
    )
    print(ds)
    
    print("DS Rows: ", ds.num_rows/100)

    data_range = math.floor((ds.num_rows)/100)
    
    longest = 0
    word = ""
    tokens = []
    infinity = math.inf

    for i in range(data_range):
        if "text" not in ds[i]:
            print(ds[i])
            
        else:   
            if len(ds[i]["text"]) > longest:
                longest = len(ds[i]["text"])
                word = ds[i]["text"]   
            if len(ds[i]["text"]) < infinity:
                infinity = len(ds[i]["text"])
                
    print(f"Shortest Word: {infinity}")
    longest_tokens = list(map(int, word.encode("utf-8")))
    print(longest_tokens)

    k = gets_stats(longest_tokens)      
    gets_stats("Hello World")


