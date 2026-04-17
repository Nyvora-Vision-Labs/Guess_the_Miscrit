#!/usr/bin/env python3
"""
Miscrit Silhouette Generator
Takes each Miscrit image, removes background, fills character solid black,
and saves as a silhouette PNG with transparent background.

Requirements:
    pip install Pillow rembg

Usage:
    python silhouette_miscrits.py
    python silhouette_miscrits.py --input my_folder --output my_output
"""

import argparse
import os
from pathlib import Path

from PIL import Image
import numpy as np

try:
    from rembg import remove
    REMBG_AVAILABLE = True
except ImportError:
    REMBG_AVAILABLE = False
    print("Warning: rembg not found. Install with: pip install rembg")
    print("Falling back to alpha-channel-only mode (works if images already have transparency).\n")


def remove_background(img: Image.Image) -> Image.Image:
    """Remove background using rembg (AI-based) or fallback to existing alpha."""
    if REMBG_AVAILABLE:
        return remove(img)
    else:
        # Fallback: if image already has alpha, use it; otherwise just convert
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        return img


def make_silhouette(img: Image.Image, shadow_color=(0, 0, 0)) -> Image.Image:
    """
    Given an RGBA image (background removed), fill all non-transparent
    pixels with solid black (or any shadow_color), keeping alpha intact.
    """
    img = img.convert("RGBA")
    data = np.array(img)

    # Unpack only the RGB values from the shadow_color tuple
    r, g, b = shadow_color

    # Where alpha > threshold, set to the shadow color; preserve the original alpha channel
    threshold = 10
    mask = data[:, :, 3] > threshold

    data[mask, 0] = r
    data[mask, 1] = g
    data[mask, 2] = b
    # data[mask, 3] remains unchanged, preserving the original transparency/edges

    return Image.fromarray(data, "RGBA")


def process_folder(input_dir: str, output_dir: str):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    supported = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif"}
    images = [f for f in input_path.iterdir() if f.suffix.lower() in supported]

    if not images:
        print(f"No images found in '{input_dir}'")
        return

    print(f"Found {len(images)} images. Processing...\n")

    success, failed = 0, 0

    for i, img_path in enumerate(sorted(images), 1):
        out_file = output_path / (img_path.stem + "_silhouette.png")
        print(f"[{i}/{len(images)}] {img_path.name} → {out_file.name}", end="  ")

        try:
            img = Image.open(img_path).convert("RGBA")

            # Step 1: Remove background
            img_no_bg = remove_background(img)

            # Step 2: Fill character with black
            silhouette = make_silhouette(img_no_bg)

            # Step 3: Save as PNG (preserves transparency)
            silhouette.save(out_file, "PNG")
            print("✓")
            success += 1

        except Exception as e:
            print(f"✗ ERROR: {e}")
            failed += 1

    print(f"\nDone! {success} succeeded, {failed} failed.")
    print(f"Silhouettes saved to: {output_path.resolve()}")


def main():
    parser = argparse.ArgumentParser(description="Convert Miscrit images to silhouettes")
    parser.add_argument(
        "--input", "-i",
        default="images_scraped_from_miscripedia",
        help="Input folder with Miscrit images (default: images_scraped_from_miscripedia)"
    )
    parser.add_argument(
        "--output", "-o",
        default="miscrits_silhouettes",
        help="Output folder for silhouette PNGs (default: miscrits_silhouettes)"
    )
    args = parser.parse_args()

    print("=== Miscrit Silhouette Generator ===\n")
    process_folder(args.input, args.output)


if __name__ == "__main__":
    main()