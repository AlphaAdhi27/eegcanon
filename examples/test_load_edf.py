import mne

print("Loading sample EEG data...")

# Load MNE sample EEG file
sample_path = mne.datasets.sample.data_path()
raw_path = sample_path / "MEG" / "sample" / "sample_audvis_raw.fif"

raw = mne.io.read_raw_fif(raw_path, preload=True)

print("EEG loaded successfully")

# Print basic info
print("\n--- BASIC INFO ---")
print(raw.info)

# Sampling rate
sfreq = raw.info["sfreq"]
print(f"\nSampling Rate: {sfreq} Hz")

# Channel names
channels = raw.info["ch_names"]
print(f"\nNumber of channels: {len(channels)}")
print("First 10 channels:", channels[:10])

# Raw signal shape
data = raw.get_data()
print("\nSignal shape (channels x time):", data.shape)