import torch
# Initialize the Hugging Face NER pipeline with GPU support (device=0 for GPU)
device = 0 if torch.cuda.is_available() else -1  # Automatically choose GPU if available, otherwise fallback to CPU
print(device)