#!/usr/bin/env python
from distutils.core import setup
import py2exe

setup(
    name = 'gmbox',
    description = 'gmbox windows binary',
    version = '0.0.1',
    console = [
        'cli.py'
    ],
    windows = [
        {
            'script':'mainwin.py',
            'icon_resources':[(1,'../pixbufs/gmbox.ico')],
        }
    ],
    options = {
        'py2exe': {
            'packages' : 'encodings',
            'includes' : 'cairo, pango, pangocairo, atk, gobject',
            'dist_dir' : 'gmbox',
        }
    },
    data_files=[
        ('data',[
            '../data/config.xml.sample']),
        ('pixbufs',[
            '../pixbufs/gmbox.ico',
            '../pixbufs/gmbox.png',
            '../pixbufs/media-audiofile.png',
            '../pixbufs/media-next.png',
            '../pixbufs/media-pause.png',
            '../pixbufs/media-play.png',
            '../pixbufs/media-previous.png',
            '../pixbufs/systray.png']),
    ]
)
