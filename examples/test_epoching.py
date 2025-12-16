from eegcanon.torch.supervised import EEGSupervisedDataset

dataset = EEGSupervisedDataset(
    data_dir="examples",
    labels_csv="examples/labels.csv",
    feature_list=["psd", "bandpower", "hjorth"],
    window=1.0,
    overlap=0.5,
)

X, y = dataset[0]

print("X shape:", X.shape)
print("y:", y)