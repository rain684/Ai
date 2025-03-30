import requests

while True:
    mode = input("Choose Mode (llama - deepseek - blackbox - chatgpt - wormgpt - evilgpt)\n\n")
    user_message = input("- Enter your msg: ")

    if user_message.lower() == 'exit':
        exit("\nThe conversation has ended ")

    url = "https://dev-apis-xyz.pantheonsite.io/wp-content/apis/freeAi.php"
    params = {"prompt": user_message, "model": mode}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        print("\n- API Response: " + response.text + "\n")
    except requests.exceptions.RequestException as e:
        print("\n⚠️ Error: API request failed!\n", str(e))
