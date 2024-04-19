from openai_chatbot_demo_packages.utils import updates_telegram_openai as Updates
import time

# Main function
def main():
    print("Starting bot...")
    offset = 0

    # Infinite loop to get the updates
    while True:
        updates = Updates.get_updates(offset)
        if updates:
            for update in updates:
                offset = update["update_id"] +1
                
                chat_id = update["message"]["chat"]['id']
                
                message = update["message"]
                id = message["from"]["id"]
                username = message["from"]["first_name"]
                user_message = update["message"]["text"]

                GPT = Updates.get_openai_response(user_message)
                Updates.send_messages(chat_id, GPT)

                print(f"Usuario: {username} ({id})")
                print(f"Received message: {user_message}")
                print(f"Send message: {GPT}")
                print("---")
        else:
            time.sleep(1)

if __name__ == '__main__':
    main()
