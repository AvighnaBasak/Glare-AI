# utils/font_suggester.py

from utils.fonts_db import FONTS

# Map your style tags (lowercased) to font categories
TAG_TO_CATEGORY = {
    # Clean & Modern Styles
    "modern": "google",
    "clean": "google",
    "minimalist": "google",
    "simple": "google",
    "flat": "google",
    "professional": "google",
    "corporate": "google",
    
    # Retro / Vintage / Display
    "retro": "display",
    "vintage": "display",
    "nostalgic": "display",
    "pop art": "display",
    "psychedelic": "display",
    "bold": "display",
    "funky": "display",

    # Futuristic / Tech
    "cyberpunk": "cyberpunk",
    "futuristic": "cyberpunk",
    "techno": "cyberpunk",
    "sci-fi": "cyberpunk",
    "digital": "cyberpunk",
    "glitch": "cyberpunk",

    # Y2K Aesthetic
    "y2k": "y2k",
    "chrome": "y2k",
    "plastic": "y2k",
    "matrix": "y2k",
    "holographic": "y2k",

    # Grunge / Punk
    "grunge": "grunge",
    "punk": "grunge",
    "distressed": "grunge",
    "raw": "grunge",
    "metal": "grunge",

    # Nature / Soft / Hand-drawn
    "handwritten": "display",
    "hand-drawn": "display",
    "organic": "display",
    "natural": "display",
    "flowy": "display",
    "script": "display",
    "feminine": "display",

    # Gothic / Dark / Baroque
    "gothic": "gothic",
    "dark": "gothic",
    "vampire": "gothic",
    "baroque": "gothic",
    "ornate": "gothic",

    # Artistic / Decorative
    "art deco": "decorative",
    "art nouveau": "decorative",
    "aesthetic": "decorative",
    "whimsical": "decorative",

    # Default / Fallback
    "system": "system",
}


def suggest_fonts_from_tags(tags, max_results=8):
    """
    Given comma-separated style tags, suggest up to max_results fonts.
    Prioritizes fonts whose category matches any tag.
    """
    tags = [t.strip().lower() for t in tags.split(',') if t.strip()]
    # collect categories to suggest
    categories = { TAG_TO_CATEGORY.get(tag) for tag in tags if TAG_TO_CATEGORY.get(tag) }
    if not categories:
        categories = {"google"}  # default

    # select fonts in those categories
    suggestions = [name for name, cat in FONTS if cat in categories]

    # dedupe while preserving order
    seen = set()
    uniq = []
    for f in suggestions:
        if f not in seen:
            seen.add(f)
            uniq.append(f)
    return uniq[:max_results]
