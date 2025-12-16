from eegcanon.io.load_file import load_file
from eegcanon.infer.channels import normalize_channel_names
from eegcanon.infer.montage import map_to_10_20
from eegcanon.infer.sampling import check_sampling_rate

# Your real EDF path
edf_path = r"D:\CognitiveCore_projects\mne_dataset\test_edf\S001R01.edf"

signal, metadata = load_file(edf_path)

# Step 5 cleanup
clean_names = normalize_channel_names(metadata["ch_names"])

# Step 6A: 10–20 mapping
mapped_signal, mapped_channels, ch_warnings = map_to_10_20(
    signal, clean_names
)

# Step 6B: sampling sanity
sfreq, fs_warnings = check_sampling_rate(metadata["sfreq"])

print("Mapped signal shape:", mapped_signal.shape)
print("Mapped channels:", mapped_channels)
print("Sampling rate:", sfreq)

print("\nWarnings:")
for w in ch_warnings + fs_warnings:
    print("-", w)