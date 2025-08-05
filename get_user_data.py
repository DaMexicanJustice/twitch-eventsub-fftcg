import requests

def get_profile_image(user_id, access_token, client_id):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-Id": client_id
    }
    response = requests.get(f"https://api.twitch.tv/helix/users?id={user_id}", headers=headers)
    data = response.json()
    if "data" in data and data["data"]:
        return data["data"][0]["profile_image_url"]
    return None