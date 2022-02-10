

def extract_youtube_video_code(youtube_video_url):
    try:
        parts, video_code = youtube_video_url.split('?v=')
    except ValueError:
        return None

    other_url_parameters = video_code.find('&')
    has_other_url_parameters = other_url_parameters != -1

    if has_other_url_parameters:
        video_code = video_code[:other_url_parameters]

    return video_code
