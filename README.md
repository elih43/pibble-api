# Pibble API

A simple REST API for serving images, built with FastAPI and deployed on Render.

**Base URL:** `pibble.hernalabs.cloud`

---

## Endpoints

### List all images

```
GET /pibble
```

Returns a list of all available images with their IDs and filenames.

**Response**

```json
{
  "count": 3,
  "images": [
    { "id": 0, "filename": "cat.jpg" },
    { "id": 1, "filename": "dog.png" },
    { "id": 2, "filename": "bird.webp" }
  ]
}
```

---

### Get image by ID

```
GET /pibble/{id}
```

Returns the image file for the given ID. IDs are zero-indexed and correspond to the list returned by `GET /pibble`.

**Path Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | The ID of the image |

**Response**

Returns the image file directly with the appropriate `Content-Type` header (e.g. `image/jpeg`, `image/png`).

**Error Responses**

| Status | Description |
|--------|-------------|
| `404` | Image with the given ID does not exist |

---

### Get a random image

```
GET /pibble/random
```

Returns a randomly selected image file.

**Response**

Returns the image file directly with the appropriate `Content-Type` header.

**Error Responses**

| Status | Description |
|--------|-------------|
| `404` | No images available |

---

## Supported Formats

`.jpg` `.jpeg` `.png` `.gif` `.webp`

---

## Running Locally

**1. Clone the repo**

```bash
git clone https://github.com/elih43/pibble-api.git
cd pibble-api
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Add images**

Drop image files into the `images/` directory.

**4. Start the server**

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

---

## Adding Images

Place image files in the `images/` directory and commit them to `main`. Render will automatically redeploy.

```bash
cp my-image.jpg images/
git add images/my-image.jpg
git commit -m "add image"
git push
```

---

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com)
- [Uvicorn](https://www.uvicorn.org)
- Deployed on [Render](https://render.com)
