import json
import os

# Folder containing your notebooks
NOTEBOOK_DIR = "."  # Current folder, change if needed

for filename in os.listdir(NOTEBOOK_DIR):
    if filename.endswith(".ipynb"):
        path = os.path.join(NOTEBOOK_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        # Check metadata.widgets
        if "widgets" in nb.get("metadata", {}):
            # Option A: Add empty state
            nb["metadata"]["widgets"]["state"] = {}

            # Option B: Remove widgets completely (uncomment if preferred)
            # nb["metadata"].pop("widgets", None)

        # Save the notebook
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print(f"Processed notebook: {filename}")

print("All notebooks fixed for GitHub rendering!")
