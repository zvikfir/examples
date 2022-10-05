import json
import requests


def send_message_discord_webhook(env, message):
    """Send message to Discord webhook"""

    if not message:
        raise Exception("No message provided")

    webhook = env.get("DISCORD_WEBHOOK_URL", None)

    if not webhook:
        raise Exception("No Discord webhook URL provided")

    try:
        response = requests.post(
            webhook,
            data=json.dumps({"content": message}),
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()
    except Exception as e:
        print(e)
        return {"success": False, "error": e}

    return {"success": True}
