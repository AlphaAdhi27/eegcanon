from eegcanon.pipeline import load_eeg

eeg = load_eeg("examples/dummy_eeg.csv")

features = eeg.extract_features(
    feature_list=["psd", "bandpower", "hjorth"],
    window=1.0,
    overlap=0.5,
)

print("Feature matrix shape:", features.shape)
print("First feature vector (truncated):", features[0][:10])
