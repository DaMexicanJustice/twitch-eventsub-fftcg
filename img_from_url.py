from PIL import Image
import requests
from io import BytesIO

def fetch_image_from_url(url: str) -> Image.Image | None:
    """
    Fetches an image from a URL and returns a Pillow Image object.
    
    Args:
        url (str): The URL of the image to fetch.
    
    Returns:
        Image.Image: The loaded image if successful.
        None: If the request fails or the image can't be opened.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return Image.open(BytesIO(response.content))
    except requests.RequestException as e:
        print(f"❌ Failed to fetch image: {e}")
    except IOError as e:
        print(f"❌ Failed to open image: {e}")
    return None