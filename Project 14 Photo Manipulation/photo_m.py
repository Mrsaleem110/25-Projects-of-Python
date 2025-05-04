from PIL import Image, ImageEnhance, ImageFilter

# User input
image_path = input("Image ka naam daalein (e.g. image.jpg): ")

try:
    # Load image
    image = Image.open(image_path)

    # Get user preferences
    brightness_factor = float(input("Brightness factor daalein (default 1.0, zyada bright = >1): "))
    contrast_factor = float(input("Contrast factor daalein (default 1.0, zyada contrast = >1): "))
    blur_radius = float(input("Blur level daalein (0 for no blur, 2 for slight blur): "))

    # Apply Brightness
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)

    # Apply Contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)

    # Apply Blur
    if blur_radius > 0:
        image = image.filter(ImageFilter.GaussianBlur(radius=blur_radius))

    # Save edited image
    output_path = "edited_" + image_path
    image.save(output_path)

    print(f"✅ Image edited successfully! Saved as {output_path}")

except FileNotFoundError:
    print("❌ File nahi mili! Sahi naam likho (e.g. image.jpg)")

except Exception as e:
    print("❌ Error:", e)
