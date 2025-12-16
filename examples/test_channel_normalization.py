from eegcanon.io.load_file import load_file
from eegcanon.infer.channels import normalize_channel_names

# Use your real EDF path
edf_path = r"D:\CognitiveCore_projects\mne_dataset\test_edf\S001R01.edf"

signal, metadata = load_file(edf_path)

raw_names = metadata["ch_names"]
clean_names = normalize_channel_names(raw_names)

print("RAW → CLEAN (first 10)")
for r, c in zip(raw_names[:10], clean_names[:10]):
    print(f"{r}  -->  {c}")

print("\nCounts equal:",
      len(raw_names) == len(clean_names))