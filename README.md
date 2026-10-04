# DecodeLabs Project 4 - Image or Text Recognition

## Project Overview

This project implements a basic text recognition pipeline using
OpenCV and Tesseract OCR.

The pipeline processes a visual input, extracts readable text,
and checks the OCR confidence against the required 80% threshold.

## Toolkit Used

- OpenCV (`cv2`) - image processing and preprocessing
- pytesseract - OCR / text recognition
- Tesseract OCR - OCR engine

## Recognition Pipeline

Image Input
→ Grayscale
→ Gaussian Blur
→ Adaptive Thresholding
→ Tesseract OCR
→ Extracted Text
→ Confidence Check
→ Output

## Pre-processing

The image is processed using:

1. Grayscale conversion
2. Gaussian Blur
3. Adaptive Thresholding

These steps prepare the image for OCR.

## Validation Conditions

### 1. Library Integration

OpenCV and pytesseract are integrated into the recognition pipeline.

### 2. Pre-processing Integrity

The pipeline includes:

- Grayscale conversion
- Gaussian Blur
- Adaptive Thresholding

### 3. Accuracy Benchmarking

The minimum required OCR confidence is 80%.

Test result:

**Average OCR Confidence: 93.82%**

**Validation Result: PASS**

### 4. Visual Confirmation

The extracted text is displayed in the terminal and the processed
image is saved as:

`processed_image.png`

## Sample Input

The sample input image is:

`sample_text.png`

## How to Run

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1