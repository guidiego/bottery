def telegram_response(
    chat_id,
    text,
    reply_markup,
    parse_mode='Markdown',
):
    return {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': parse_mode,
        'reply_markup': reply_markup,
    }

def reply_keyboard_markup(buttons, *args, **kw):
    selective = kw.get('selective')
    resize_keyboard = kw.get('resize_keyboard')
    data = {
        'keyboard': buttons,
        'one_time_keyboard': kw.get('one_time_keyboard', True),
    }

    if selective:
        data['selective'] = selective

    if resize_keyboard:
        data['resize_keyboard'] = resize_keyboard

    return data


def keyboard_button(text, *args, **kw):
    request_contact = kw.get('request_contact')
    request_location = kw.get('request_location')
    data = { 'text': text }

    if request_contact:
        data['request_contact'] = request_contact

    if request_location:
        data['request_location'] = request_location

    return data