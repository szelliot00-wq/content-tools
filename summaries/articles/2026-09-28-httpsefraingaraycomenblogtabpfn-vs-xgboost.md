# TabPFN and TabICL vs. tuned XGBoost: the model that doesn't train won 14/14

Source: https://efraingaray.com/en/blog/tabpfn-vs-xgboost/

## Summary
The author ran a hands-on benchmark comparing two tabular foundation models (TabICL and TabPFN) against tuned XGBoost across 14 datasets from the Grinsztajn benchmark, all trimmed to 3,000 rows. The core finding is that TabICL — a model that never trains on the target data, processing it as context in a single forward pass — beat tuned XGBoost on all 14 datasets by AUC, while completing inference in under a second versus up to 27 seconds for hyperparameter search. The article also documents three practical stumbles encountered along the way: a silent PyTorch GPU fallback, OpenML API downtime, and a new account/license barrier in TabPFN's current release.

## Key takeaways
- **TabICL won 14/14 datasets on AUC** against tuned XGBoost, with a mean AUC advantage of +0.0114 — consistent, though the margin (~0.01) is small in absolute terms.
- **The cost model is inverted**: fitting is nearly free for foundation models while prediction is the expensive step, the opposite of tree-based models. TabICL resolved datasets in ~0.8s vs. up to 27s for tuned XGBoost.
- **The advantage holds at scale**: testing on up to 32,000 rows, TabICL's lead over XGBoost grew to +0.030, not collapsed as expected — though a single dataset was used for this sweep.
- **Width, not length, is the breaking point**: the 419-column Bioresponse dataset caused TabPFN to degrade significantly and slowed TabICL; column count strains attention costs more than row count.
- **TabPFN's latest version (8.x) now requires account registration** to download weights, making it no longer freely installable. The author used 2.2.1 as a workaround; TabICL (BSD licensed) has no such barrier.
- **PyTorch can silently fall back to CPU** if the installed CUDA build version doesn't match the driver — worth verifying with `torch.cuda.is_available()` before any GPU benchmark.
- **Practical recommendation**: use TabICL for binary classification on tables with 1,000–30,000 rows and under ~100 columns when iteration speed matters; avoid it for very wide tables, production without a GPU, or lightweight deployable artifacts.