import os
import cv2
import pytesseract

# Tesseract OCR engine path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Input image
IMAGE_PATH = "sample_text.png"

# Minimum confidence required by Project 4
MIN_CONFIDENCE = 80.0


def recognize_text(image_path):
    """Pre-process image and extract text with OCR confidence."""

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(
            f"Could not read image: {image_path}"
        )

    # 1. Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 3. Adaptive Thresholding
    thresholded = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # Save processed image for visual confirmation
    cv2.imwrite("processed_image.png", thresholded)

    # OCR with word-level confidence data
    data = pytesseract.image_to_data(
        thresholded,
        config="--psm 6",
        output_type=pytesseract.Output.DICT
    )

    recognized_words = []
    confidence_values = []

    for i, text in enumerate(data["text"]):
        text = text.strip()

        try:
            confidence = float(data["conf"][i])
        except (ValueError, TypeError):
            continue

        if text and confidence >= 0:
            recognized_words.append(text)
            confidence_values.append(confidence)

    extracted_text = " ".join(recognized_words)

    if confidence_values:
        average_confidence = sum(confidence_values) / len(confidence_values)
    else:
        average_confidence = 0.0

    return extracted_text, average_confidence


def main():
    print("=" * 60)
    print("DecodeLabs Project 4 - Basic Text Recognition")
    print("=" * 60)

    if not os.path.exists(IMAGE_PATH):
        print(f"\nInput image not found: {IMAGE_PATH}")
        print("Please place a clear text image in the project folder.")
        return

    text, confidence = recognize_text(IMAGE_PATH)

    print("\nExtracted Text:")
    print("-" * 60)
    print(text if text else "No readable text detected.")

    print("\nAverage OCR Confidence:")
    print(f"{confidence:.2f}%")

    print("\nValidation Result:")
    if confidence >= MIN_CONFIDENCE:
        print("PASS - Confidence is at least 80%.")
    else:
        print("WARNING - Confidence is below 80%.")

    print("\nProcessed image saved as: processed_image.png")


if __name__ == "__main__":
    main()