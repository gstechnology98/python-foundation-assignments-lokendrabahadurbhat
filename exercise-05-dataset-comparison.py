# Exercise 5: Dataset Comparison

dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}


# 1. All unique dataset names (Union)
all_datasets = dataset_a.union(dataset_b)

# 2. Datasets found in both groups (Intersection)
common_datasets = dataset_a.intersection(dataset_b)

# 3. Datasets only in dataset_a (Difference)
only_in_a = dataset_a.difference(dataset_b)

# 4. Datasets only in dataset_b (Difference)
only_in_b = dataset_b.difference(dataset_a)

# Display each result clearly
print(f"Dataset A: {dataset_a}")
print(f"Dataset B: {dataset_b}")
print("-" * 40)
print(f"All Unique Datasets: {all_datasets}")
print(f"Datasets in Both Groups: {common_datasets}")
print(f"Datasets Only in Dataset A: {only_in_a}")
print(f"Datasets Only in Dataset B: {only_in_b}")