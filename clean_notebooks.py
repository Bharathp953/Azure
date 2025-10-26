import json
import os

# Folder containing your notebooks
NOTEBOOK_DIR = "."  # current folder, change if needed

for filename in os.listdir(NOTEBOOK_DIR):
    if filename.endswith(".ipynb"):
        path = os.path.join(NOTEBOOK_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        # Remove 'widgets' key from metadata entirely
        if "widgets" in nb.get("metadata", {}):
            nb["metadata"].pop("widgets", None)

        # Save the notebook
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)

        print(f"Cleaned notebook: {filename}")

print("All notebooks cleaned for GitHub rendering!")
