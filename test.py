import eegcanon
from eegcanon.pipeline import load_eeg

print(eegcanon.__version__ if hasattr(eegcanon, "__version__") else "import ok")