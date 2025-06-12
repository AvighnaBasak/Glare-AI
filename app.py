# app.py

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

from utils.tag_extractor import (
    generate_blip_caption,
    extract_clip_caption,
    query_llama3_style_tags,
)
from utils.palette_extractor import extract_dominant_colors, find_similar_palettes
from utils.palette_db import CURATED_PALETTES
from utils.font_suggester import suggest_fonts_from_tags  # ← new

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    uploaded = False
    caption = clip_tags = llama_tags = ""
    palette = similar_palettes = []
    suggested_fonts = []
    image_path = ""

    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename:
            filename = secure_filename(file.filename)
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(full_path)

            # Generate everything
            caption       = generate_blip_caption(full_path)
            clip_tags     = extract_clip_caption(full_path)
            llama_tags    = query_llama3_style_tags(caption)
            palette       = extract_dominant_colors(full_path)
            similar_palettes = find_similar_palettes(palette, CURATED_PALETTES, top_n=3)

            # **Font suggestions** based on combined tags
            tag_string    = ','.join(filter(None, [clip_tags, llama_tags]))
            suggested_fonts = suggest_fonts_from_tags(tag_string)

            uploaded = True
            image_path = f"/static/uploads/{filename}"

    return render_template(
        'index.html',
        uploaded=uploaded,
        image_path=image_path,
        caption=caption,
        clip_tags=clip_tags,
        llama_tags=llama_tags,
        palette=palette,
        similar_palettes=similar_palettes,
        suggested_fonts=suggested_fonts  # ← pass into template
    )

if __name__ == '__main__':
    print("💡 Starting StyleMimic at http://localhost:5000")
    app.run(debug=True)
