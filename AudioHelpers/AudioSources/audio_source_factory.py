from AudioHelpers.AudioSources.audio_source_type import AudioSourceType
from AudioHelpers.AudioSources.ytdl_source import YTDLSource


class AudioSourceFactory:
    @staticmethod
    def provide_source(source_type):
        if source_type is AudioSourceType.SOURCE_YOUTUBE:
            return YTDLSource
        if source_type is AudioSourceType.SOURCE_UNKNOWN:
            return None
