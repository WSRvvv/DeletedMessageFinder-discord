# ChatComparer

**ChatComparer** is a Python script designed to compare two chat histories from Discord stored in JSON files and identify deleted messages. The results can be exported in JSON, CSV, or TXT formats.

## Features

- Compare messages between two JSON files.
- Detect deleted messages including various types of content such as links, images, videos, files, and attachments.
- Identify messages present in the first file but missing in the second file.
- Export results to JSON, CSV, or TXT formats.
- Includes debug information to help troubleshoot issues.

## Prerequisites

1. **DiscordChatExporter**:
   The chat files must be exported using [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter). This tool allows you to export chat histories from Discord in JSON format, which is required for the `MessageComparer` script to work.

   - Follow the instructions on the [DiscordChatExporter GitHub page](https://github.com/Tyrrrz/DiscordChatExporter) to export your chat histories.

2. **Python**:
   Make sure you have the latest python installed on your system. The script is compatible with Windows, did not tested in linux/Macos.

## Usage
```python
python compare-chat.py 
```

### notice/warning : 
1. **Update File Paths**:
   Edit the script to provide the correct paths to your JSON files exported from DiscordChatExporter. Replace the placeholders with the paths to your files:|

   ```python
   before_file = r'C:\path\to\first_save.json'
   after_file = r'C:\path\to\second_save.json'
   output_file = r'C:\path\to\deleted_messages.json'

 ``output_file`` is the path where you want to save the deleted messages. Choose the path where you want the file to be exported.

 ``before_file`` This is the first save of the conversation, before any messages were deleted.

 ``after_file`` This is the second save of the conversation, after one or more messages have been deleted. 

It is only useful if a message that was present in the first save has been deleted in the second save. 
For example, if a message was deleted in 2023, you can only detect it if you have a first save that contains the deleted message. 
You can then compare it with a new save to see which messages were deleted, no need to manually search for it.

