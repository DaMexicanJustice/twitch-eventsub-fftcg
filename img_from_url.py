from PIL import Image
import requests
from io import BytesIO

def fetch_image_from_url(url: str, target_size: tuple[int, int]) -> Image.Image | None:
    """
    Fetches an image from a URL, converts it to RGBA, and resizes it to match target size.
    
    Args:
        url (str): The URL of the image to fetch.
        target_size (tuple): Desired (width, height) for the image.
    
    Returns:
        Image.Image: The processed image if successful.
        None: If the request fails or the image can't be opened.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content)).convert("RGBA")
        image = image.resize(target_size, Image.LANCZOS)
        return image
    except requests.RequestException as e:
        print(f"❌ Failed to fetch image: {e}")
    except IOError as e:
        print(f"❌ Failed to open image: {e}")
    return None