#source https://github.com/hassaku/colab-a11y-utils

from pydub import AudioSegment
from pydub.generators import Sine, Pulse, Square, Sawtooth, Triangle, WhiteNoise
from IPython.display import Audio, display

from tqdm.notebook import tqdm as original_tqdm


class InvisibleAudio(Audio):
    def _repr_html_(self):
        audio = super()._repr_html_()
        audio = audio.replace('<audio', f'<audio onended="this.parentNode.removeChild(this)"')
        return f'<div style="display:none">{audio}</div>'


def set_sound_notification():
    def sound_notification_before(*args):
        sound = Triangle(440).to_audio_segment(duration=50).apply_gain(-10).fade_in(20).fade_out(20)
        display(InvisibleAudio(data=sound.export().read(), autoplay=True))

    def sound_notification_after(file_mp3="/content/colab_utils/utils/soundtrack_harry_potter.mp3",*args):
        sound=AudioSegment.from_mp3(file_mp3)
        display(InvisibleAudio(data=sound.export().read(), autoplay=True))

    # get_ipython().events.register('pre_run_cell', sound_notification_before)
    sound_notification_after()

