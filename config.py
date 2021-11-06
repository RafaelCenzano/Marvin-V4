import os
import platform

import deepspeech

'''
Config file containing Config class
'''

class ConfigException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Config(object):

    # Porcupine Config
    PORCUPINE_LIBRARY     = 'porcupine/libpv_porcupine.dylib'
    PORCUPINE_MODEL       = 'porcupine/porcupine_params.pv'
    PORCUPINE_KEYWORD     = ['porcupine/terminator.ppn']
    PORCUPINE_SENSITIVITY = [0.7]

    OS_TYPE         = platform.system()
    OS_VERSION      = platform.release()
    FULL_OS_VERSION = platform.version()
    OS_PLATFORM     = platform.platform()

    MAC = False
    LINUX = False
    WINDOWS = False

    if OS_TYPE == 'Darwin':
        MAC = True
    elif OS_TYPE == 'Linux':
        LINUX = True
    elif OS_TYPE == 'Windows':
        WINDOWS = True
    else:
        raise ConfigException(f'Operating System: {FULL_OS_VERSION}, not supported')

    SR = deepspeech.Model('deepspeech-0.7.4-models.pbmm')
    SR.enableExternalScorer('deepspeech-0.7.4-models.scorer')
