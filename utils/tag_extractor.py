# utils/tag_extractor.py

import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from transformers import CLIPProcessor, CLIPModel
import requests

device = "cuda" if torch.cuda.is_available() else "cpu"

# --- BLIP for rich captions ---
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(device)

# --- CLIP for style‐tag similarity ---
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)

known_tags = [
    "Brutalist", "Y2K", "Corporate Memphis", "Vaporwave", "Cyberpunk",
    "Bauhaus", "Dadaism", "Minimalist", "Swiss Design", "Memphis Milano",
    "Pop Art", "Art Deco", "Modernist", "Vintage", "Flat Design",
    "Skeuomorphic", "Surrealism", "Gothic", "Synthwave", "Futuristic"
]

# Precompute text embeddings for tags
def _compute_tag_embeddings(tags):
    inputs = clip_processor(text=tags, return_tensors="pt", padding=True).to(device)
    with torch.no_grad():
        feats = clip_model.get_text_features(**inputs)
    return feats / feats.norm(p=2, dim=-1, keepdim=True)

tag_text_embeddings = _compute_tag_embeddings(known_tags)


def generate_blip_caption(image_path: str) -> str:
    """Rich natural-language description via BLIP."""
    img = Image.open(image_path).convert('RGB')
    inputs = blip_processor(img, return_tensors="pt").to(device)
    out = blip_model.generate(**inputs, max_new_tokens=30)
    return blip_processor.decode(out[0], skip_special_tokens=True)


def extract_clip_caption(image_path: str, top_k: int = 5) -> str:
    """Top-K style tags by CLIP similarity."""
    img = Image.open(image_path).convert('RGB')
    inputs = clip_processor(images=img, return_tensors="pt").to(device)
    with torch.no_grad():
        img_feat = clip_model.get_image_features(**inputs)
    img_feat = img_feat / img_feat.norm(p=2, dim=-1, keepdim=True)

    sims = (img_feat @ tag_text_embeddings.T).squeeze(0)  # (num_tags,)
    topk = sims.topk(top_k).indices.cpu().tolist()
    tags = [known_tags[i] for i in topk]
    return ", ".join(tags)


def query_llama3_style_tags(caption: str) -> str:
    """Refine tags via your local LLaMA 3 Ollama server."""
    prompt = f"""
You are a design assistant. Given this description of an artwork:
"{caption}"

Select the 4–6 most relevant style tags from the following list:
{', '.join(known_tags)}

Return ONLY the tags as a comma-separated list.
    """.strip()

    resp = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    if resp.ok:
        return resp.json().get("response", "").strip()
    raise RuntimeError(f"Ollama API error: {resp.status_code} {resp.text}")
