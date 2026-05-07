import random
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

IMAGES_DIR = Path("images")
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

app = FastAPI(title="Pibble API")


def get_all_images() -> list[Path]:
    return sorted(
        [f for f in IMAGES_DIR.iterdir() if f.suffix.lower() in SUPPORTED_EXTENSIONS]
    )


@app.get("/pibble")
def list_images():
    images = get_all_images()
    return {
        "count": len(images),
        "images": [
            {"id": i, "filename": img.name} for i, img in enumerate(images)
        ],
    }


@app.get("/pibble/random")
def random_image():
    images = get_all_images()
    if not images:
        raise HTTPException(status_code=404, detail="No images found")
    img = random.choice(images)
    return FileResponse(img, media_type=f"image/{img.suffix.lstrip('.').replace('jpg', 'jpeg')}")


@app.get("/pibble/{id}")
def get_image(id: int):
    images = get_all_images()
    if id < 0 or id >= len(images):
        raise HTTPException(status_code=404, detail=f"Image {id} not found")
    img = images[id]
    return FileResponse(img, media_type=f"image/{img.suffix.lstrip('.').replace('jpg', 'jpeg')}")
