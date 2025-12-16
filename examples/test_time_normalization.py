from eegcanon.pipeline import load_eeg

edf_path = r"D:\CognitiveCore_projects\mne_dataset\test_edf\S001R01.edf"

eeg = load_eeg(edf_path, target_fs=256)

print("CanonicalEEG")
print("Data shape:", eeg.data.shape)
print("Channels:", eeg.channels)
print("Sampling rate:", eeg.sampling_rate)

print("\nWarnings:")
for w in eeg.warnings:
    print("-", w)

print("\nProvenance:")
for k, v in eeg.provenance.items():
    print(f"{k}: {v}")
