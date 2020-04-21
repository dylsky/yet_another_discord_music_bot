from AudioHelpers.AudioSources.audio_source_type import AudioSourceType
from urllib.parse import urlparse


class AudioSourceIdentifier:
    @staticmethod
    def identify_source(search):

        YOUTUBE_DOMAIN_NAMES = ["www.youtube.com", "youtu.be"]
        YANDEXMUSIC_DOMAIN_NAMES = ["music.yandex.ru"]
        BANDCAMP_DOMAIN_NAMES = []
        SOUNDCLOUD_DOMAIN_NAMES = []
        SPOTIFY_DOMAIN_NAMES = []
        parsed_url = urlparse(search)

        if any(parsed_url.netloc in s for s in YOUTUBE_DOMAIN_NAMES):
            return AudioSourceType.SOURCE_YOUTUBE

        if any(parsed_url.netloc in s for s in YANDEXMUSIC_DOMAIN_NAMES):
            return AudioSourceType.SOURCE_YANDEXMUSIC

        if any(parsed_url.netloc in s for s in BANDCAMP_DOMAIN_NAMES):
            return AudioSourceType.SOURCE_BANDCAMP

        if any(parsed_url.netloc in s for s in SOUNDCLOUD_DOMAIN_NAMES):
            return AudioSourceType.SOURCE_SOUNDCLOUD

        if any(parsed_url.netloc in s for s in SPOTIFY_DOMAIN_NAMES):
            return AudioSourceType.SOURCE_SPOTIFY

        return AudioSourceType.SOURCE_UNKNOWN
