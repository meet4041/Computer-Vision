# Text Detection

This folder contains a small OCR experiment for extracting text from images and comparing two OCR approaches:

- `Tesseract OCR`
- `EasyOCR`

The implementation is written in the notebook [`Main.ipynb`](c:\Users\BAPS\Desktop\Computer Vision\Text Detection\Main.ipynb), and the sample dataset is stored in `data.zip`.

## Files

- `Main.ipynb` - main notebook for setup, OCR, and basic evaluation
- `data.zip` - zipped image dataset used by the notebook

## What the Notebook Does

The notebook follows this flow:

1. Mounts Google Drive in Google Colab
2. Copies `data.zip` into the Colab runtime
3. Extracts the dataset
4. Installs OCR dependencies
5. Reads text from images using both Tesseract and EasyOCR
6. Compares OCR output with expected text using Jaccard similarity

## Dependencies

The notebook installs and uses:

- `tesseract-ocr`
- `pytesseract`
- `Pillow`
- `easyocr`
- `boto3`

## Dataset Format

The dataset inside `data.zip` contains images such as:

- `a.webp`
- `b.png`
- `c.jpg`
- `d.jpg`

The notebook derives the ground-truth text from each file name by:

- removing the file extension
- replacing `_` with spaces
- converting the text to lowercase

## How to Run

This notebook is currently set up for **Google Colab**.

1. Open `Main.ipynb` in Colab
2. Upload or connect the dataset
3. Run the cells in order
4. Review the OCR outputs and similarity scores

## Notes

- The current evaluation loop stops after the first image because of the `break` statement.
- The printed score is divided by `2`, so you may want to adjust that if you evaluate the full dataset.
- If you want to run this locally instead of Colab, you will need to replace the Google Drive copy step with local file paths.
