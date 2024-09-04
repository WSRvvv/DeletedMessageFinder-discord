import json
import csv

def load_messages(file_path):
    print(f"[DEBUG] Loading messages from {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"[DEBUG] Successfully loaded {len(data['messages'])} messages from {file_path}")
    except Exception as e:
        print(f"[ERROR] Failed to load messages from {file_path}: {e}")
        return {}
    
    messages = {
        msg['id']: {
            'content': msg['content'],
            'author': msg['author']['name'],
            'timestamp': msg['timestamp'],
            'attachments': msg.get('attachments', []),
            'embeds': msg.get('embeds', [])
        }
        for msg in data['messages']
    }
    return messages

def compare_conversations(before_file, after_file):
    print(f"[DEBUG] Comparing conversations: {before_file} vs {after_file}")
    before_messages = load_messages(before_file)
    after_messages = load_messages(after_file)

    deleted_messages = [
        msg for msg_id, msg in before_messages.items()
        if msg_id not in after_messages
    ]
    
    print(f"[DEBUG] Found {len(deleted_messages)} deleted messages")
    return deleted_messages

def export_to_json(deleted_messages, output_file):
    print(f"[DEBUG] Exporting deleted messages to JSON file: {output_file}")
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(deleted_messages, file, ensure_ascii=False, indent=4)
        print(f"[DEBUG] Successfully exported deleted messages to {output_file}")
    except Exception as e:
        print(f"[ERROR] Failed to export to JSON: {e}")

def export_to_csv(deleted_messages, output_file):
    print(f"[DEBUG] Exporting deleted messages to CSV file: {output_file}")
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['content', 'author', 'timestamp', 'attachments', 'embeds'])
            for msg in deleted_messages:
                attachments = ", ".join([attachment['url'] for attachment in msg['attachments']])
                embeds = ", ".join([embed['url'] if 'url' in embed else 'N/A' for embed in msg['embeds']])
                writer.writerow([msg['content'], msg['author'], msg['timestamp'], attachments, embeds])
        print(f"[DEBUG] Successfully exported deleted messages to {output_file}")
    except Exception as e:
        print(f"[ERROR] Failed to export to CSV: {e}")

def export_to_txt(deleted_messages, output_file):
    print(f"[DEBUG] Exporting deleted messages to TXT file: {output_file}")
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for msg in deleted_messages:
                file.write(f"Deleted message: {msg['content']} (from {msg['author']}) at {msg['timestamp']}\n")
                if msg['attachments']:
                    for attachment in msg['attachments']:
                        file.write(f"  Attached file: {attachment['url']}\n")
                if msg['embeds']:
                    for embed in msg['embeds']:
                        file.write(f"  Embedded link: {embed['url'] if 'url' in embed else 'N/A'}\n")
        print(f"[DEBUG] Successfully exported deleted messages to {output_file}")
    except Exception as e:
        print(f"[ERROR] Failed to export to TXT: {e}")

before_file = r'YOU NEED TO PUT THE FIRST SAVE OF THE CHAT HERE (ONLY JSON IS SUPPORTED)'
after_file = r'The second save is only useful if a Discord message was deleted in an earlier conversation (ONLY JSON IS SUPPORTED)'

print("[DEBUG] Starting comparison of conversations")
deleted_messages = compare_conversations(before_file, after_file)

output_format = input("Do you want to use json, csv, or txt format? ").strip().lower()
output_file = r'(change it to you own way)D:_Account\Downloads\deleted_messages.' + output_format

if output_format == 'json':
    export_to_json(deleted_messages, output_file)
elif output_format == 'csv':
    export_to_csv(deleted_messages, output_file)
elif output_format == 'txt':
    export_to_txt(deleted_messages, output_file)
else:
    print("[ERROR] Unsupported output format. Please use 'json', 'csv', or 'txt'.")
