from abc import ABC, abstractmethod

from .model import MediaFormat
from .processor import FLACAudioProcessor,MP3AudioProcessor
from .player import FLACPlayer, MP3Player
from .decoder import FLACDecoder, MP3Decoder


class AudioFactory(ABC):
    @abstractmethod
    def create_audio_decoder(self,*args):
        pass
    @abstractmethod
    def create_audio_processor(self,*args):
        pass
    @abstractmethod
    def create_audio_player(self,*args):
        pass
    @abstractmethod
    def supports_format(self):
        pass

class FLACAudioFactory(AudioFactory):
    def create_audio_decoder(self,*args):
        return FLACDecoder(*args)
    def create_audio_processor(self,*args):
        return FLACAudioProcessor(*args)
    def create_audio_player(self,*args):
        return FLACPlayer(*args)
    def supports_format(self):
        return MediaFormat.FLAC

class MP3AudioFactory(AudioFactory):

    def create_audio_decoder(self,*args):
        return MP3Decoder(*args)
    def create_audio_processor(self,*args):
        return MP3AudioProcessor(*args)
    def create_audio_player(self,*args):
        return MP3Player(*args)
    def supports_format(self):
        return MediaFormat.MP3
