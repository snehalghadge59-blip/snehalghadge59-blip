import sys
import io
import cv2
import numpy as np
from PIL import Image

def prep_photo(input_path, output_path="data/source-prepped.png"):
    try:
        from rembg import remove
        with open(input_path, "rb") as f:
            input_bytes = f.read()
        output_bytes = remove(input_bytes)
        img = Image.open(io.BytesIO(output_bytes)).convert("RGBA")
        white_bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        composite = Image.alpha_composite(white_bg, img).convert("L")
        img_np = np.array(composite)
    except Exception as e:
        print(f"Rembg fallback: {e}")
        img = Image.open(input_path).convert("L")
        img_np = np.array(img)

    # Boost local contrast with CLAHE
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(img_np)
    
    import os
    os.makedirs("data", exist_ok=True)
    cv2.imwrite(output_path, enhanced)
    print(f"Successfully prepped photo -> {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prep_photo(sys.argv[1])
    else:
        print("Usage: python scripts/prep_photo.py <photo_path>")
