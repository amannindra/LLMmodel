from datasets import load_dataset

ds = load_dataset("HuggingFaceTB/smollm-corpus", "cosmopedia-v2", split="train", num_proc=16)
print(ds[0])