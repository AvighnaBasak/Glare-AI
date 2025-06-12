# utils/palette_extractor.py

from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def extract_dominant_colors(image_path, num_colors=5):
    """
    Extract `num_colors` dominant colors from an image and return them as hex codes.
    """
    image = Image.open(image_path).convert('RGB')
    image = image.resize((200, 200))  # Resize for faster processing

    pixels = np.array(image).reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors, n_init='auto', random_state=42)
    kmeans.fit(pixels)

    dominant_colors = kmeans.cluster_centers_.astype(int)
    hex_colors = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in dominant_colors]
    return hex_colors

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def palette_distance(p1, p2):
    """
    Compute average Euclidean distance between two palettes of equal length.
    """
    rgb1 = [hex_to_rgb(c) for c in p1]
    rgb2 = [hex_to_rgb(c) for c in p2]
    total = 0
    for a, b in zip(rgb1, rgb2):
        total += sum((x-y)**2 for x,y in zip(a,b))**0.5
    return total / len(p1)

def find_similar_palettes(input_palette, palettes_db, top_n=3):
    """
    Given input_palette (list of hex strings),
    return the top_n palettes from palettes_db most similar by color distance.
    """
    scored = []
    for pal in palettes_db:
        if len(pal) == len(input_palette):
            d = palette_distance(input_palette, pal)
            scored.append((pal, d))
    scored.sort(key=lambda x: x[1])
    # return only the palette lists, not distances
    return [pal for pal, _ in scored[:top_n]]
