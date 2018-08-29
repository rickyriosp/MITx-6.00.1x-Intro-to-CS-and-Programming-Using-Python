def decrypt_story():
    story_string = get_story_string()
    text = CiphertextMessage(story_string)
    return text.decrypt_message()
