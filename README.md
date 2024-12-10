### **README.md**

# Random Forest Classifier for Pitch Type Prediction

This folder/repository contains the resources and script required to predict missing `pitch_type` values in a baseball dataset using a Random Forest Classifier.

## Files in the Folder

- **`rf_classifier.py`**:
  Python script that:
  1. Trains a Random Forest Classifier on the dataset.
  2. Predicts missing `pitch_type` values.
  3. Saves the updated dataset with predictions.

- **`requirements.txt`**:
  A list of Python dependencies required to run the script.

- **`data.csv`**:
  Input dataset with `pitch_type` values partially missing. Replace this with your dataset file.

- **`complete_dataset_updated.csv`**:
  Output dataset with `pitch_type` values filled in after running the script.

---

## Prerequisites

Make sure you have Python installed (>=3.7).

---

## How to Use

1. **Clone or Download the Repository**:
   Clone the folder/repository to your local machine or download the folder.

2. **Install Dependencies**:
   Use the `requirements.txt` file to install the necessary Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Place Your Dataset**:
  Ensure the dataset has the required columns:
   - `"pitch_initial_speed_a"`
   - `"break_x_a"`
   - `"break_z_a"`
   - `"pitch_initial_speed_b"`
   - `"spinrate_b"`
   - `"break_x_b"`
   - `"break_z_b"`
   - `"pitch_type"` (with some missing values)

4. **Run the Script**:
   Execute the `classifier.py` script:
   ```bash
   python classifier.py
   ```

5. **Check the Output**:
   - The updated dataset with predictions will be saved as `predicted_results.csv` in the same directory.

---

## Notes

- The script uses a Random Forest Classifier to predict the missing `pitch_type` values based on the provided features.
- The predictions are mapped to their corresponding pitch type names (e.g., `Fastball`, `Curveball`) instead of numeric labels.

---

## Contact

If you have any questions or issues, feel free to contact amujral@ucsd.edu.
