from eegcanon.torch.dataset import EEGDataset

dataset = EEGDataset(
    data_dir="examples",   # contains dummy_eeg.csv
    target_fs=256,
)

print("Dataset size:", len(dataset))

X, eeg = dataset[0]

print("Tensor shape:", X.shape)
print("Channels:", eeg.channels)
print("Sampling rate:", eeg.sampling_rate)
print("Provenance:", eeg.provenance)