from eegcanon.io.load_edf import load_edf
import mne

# Use the same MNE sample dataset
sample_path = mne.datasets.sample.data_path()
edf_path = r"D:\CognitiveCore_projects\mne_dataset\test_edf\S001R01.edf"

signal, metadata = load_edf(edf_path)

print("Signal shape:", signal.shape)
print("Sampling rate:", metadata["sfreq"])
print("Number of channels:", metadata["nchan"])
print("First 5 channels:", metadata["ch_names"][:5])
print("Duration (sec):", metadata["duration_sec"])