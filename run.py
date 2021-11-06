from datetime import datetime
import struct

import pyaudio

import config
from marvin import core
from marvin.helpers import listen
from porcupine.porcupine import Porcupine


if __name__ == '__main__':

    '''
     Creates an input audio stream, initializes wake word detection (Porcupine) object, and monitors the audio
     stream for occurrences of the wake word.
    '''

    marvinConfig = config.Config()

    core.speak('Terminator Online')

    porcupine = None
    pa = None
    audio_stream = None

    try:

        # Create Porcupine object
        porcupine = Porcupine(
            library_path=marvinConfig.PORCUPINE_LIBRARY,
            model_file_path=marvinConfig.PORCUPINE_MODEL,
            keyword_file_paths=marvinConfig.PORCUPINE_KEYWORD,
            sensitivities=marvinConfig.PORCUPINE_SENSITIVITY)

        # Create PyAudio Object
        pa = pyaudio.PyAudio()

        while True:
            audio_stream = pa.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length,
                input_device_index=None)

            while True:
                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

                result = porcupine.process(pcm)
                if result:
                    audio_stream.close()
                    print(f'[{datetime.now()}] detected keyword')
                    command = listen.listen()
                    #core.main(command)
                    break


    except KeyboardInterrupt:
        print('Shutting Down ...')

    finally:
        if porcupine is not None:
            print('Stopping Porcupine')
            porcupine.delete()

        if audio_stream is not None:
            print('Stopping audio stream')
            audio_stream.close()

        if pa is not None:
            print('Stopping PyAudio')
            pa.terminate()

