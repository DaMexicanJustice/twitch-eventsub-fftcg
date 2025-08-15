from flask import Flask, request, jsonify, Response, send_file, render_template
import hmac
import hashlib
import json
from dotenv import load_dotenv
import os
import create_img  # Assuming this contains your bot logic
import get_user_data
import time

load_dotenv()
TWITCH_SECRET = os.getenv('my_secret')

app = Flask(__name__)

@app.route("/card")
def serve_card():
    card_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "card.png")
    if not os.path.exists(card_path):
        return "Card image not found.", 404
    return send_file(card_path, mimetype="image/png")

@app.route('/webhook', methods=['POST'])
def webhook():
    print("reached")
    # Verify signature
    message_id = request.headers.get('Twitch-Eventsub-Message-Id')
    timestamp = request.headers.get('Twitch-Eventsub-Message-Timestamp')
    message_signature = request.headers.get('Twitch-Eventsub-Message-Signature')
    body = request.data.decode('utf-8')
    hmac_message = message_id + timestamp + body

    if TWITCH_SECRET is None:
        print("⚠️ TWITCH_SECRET is not set! Check your .env file.")
        return 'Server misconfiguration', 500

    my_signature = 'sha256=' + hmac.new(
        TWITCH_SECRET.encode(), hmac_message.encode(), hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(my_signature, message_signature):
        return 'Invalid signature', 403

    payload = json.loads(body)

    # Handle challenge during subscription
    if payload['subscription']['type'] == 'channel.channel_points_custom_reward_redemption.add':
        if payload['subscription']['status'] == 'webhook_callback_verification_pending':
            if payload.get("challenge"):
                return Response(payload["challenge"], status=200, mimetype="text/plain")

    # Actual event
    if payload['subscription']['type'] == 'channel.channel_points_custom_reward_redemption.add':
        event = payload['event']
        username = event['user_name']
        user_id = payload['event']['user_id']
        reward = event['reward']['title']
        print(f"✅ {username} redeemed: {reward}")
        generate_user_card(user_id, username)

    return '', 204

def generate_user_card(user_id, username):
    print(f"Generating card for user ID: {user_id}")
    access_token = os.getenv("access_token")
    client_id = os.getenv("client_id")
    profile_image_url = get_user_data.get_profile_image(user_id, access_token, client_id)
    return create_img.generate_card(profile_image_url, username)

if __name__ == '__main__':
    import payload  # auto-register when deployed
    # Then start Flask
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))