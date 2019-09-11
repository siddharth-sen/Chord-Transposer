import pandas as pd
import numpy as np
import re

all_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
key = ({value: key for key, value in enumerate(all_notes, start=1)})
print(key)


def cleaner(*args) :
    return list(set([re.match('([A-Z]{1}[\W]{0,1})', chord).group() for chord in args]))


def scale_changer(chords, capo_fret=0, original_scale='C', new_scale='C') :
    """
    This function converts the chords at the current fret (capo or not) of a given scale into chords of the desired scale.
    
    Input:
        chords (list): current chords of the song
        capo_fret (int): fret at which capo is present. Default = 0
        original_scale (str): Original scale of the song. Default = 'C'
        new_scale (str): Desired scale for the song. Default = 'C'
    """

    all_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    key = ({value: key for key, value in enumerate(all_notes, start=1)})
    
    original_chords = chords
    clean_chords = [cleaner(chord)[0] for chord in chords]
    
    steps = capo_fret + (key[new_scale] - key[original_scale])

    new_notes = []
    for note in clean_chords :
        if key[note]+steps <= 0 :
            new_notes.append(key[note]+steps + 12)
        elif key[note]+steps > 12 :
            new_notes.append(key[note]+steps - 12)
        else : new_notes.append(key[note]+steps)

    t_chords = dict(zip(original_chords, [index for note in new_notes for index in key.keys() if key[index] == note]))
    
    for index, value in t_chords.items() :
        if re.search('([a-z0-9]+)', index) :
            t_chords[index] = value+re.search('([a-z0-9]+)', index).group()
    
    print('====================\n', 'Output: The new chords after converting the scale from', original_scale, ', to the new scale', new_scale, 'are:\n')
    for index, value in t_chords.items() :
        print(index, ' ---> ', value)
        
        

"""Hey Jude - Beatles"""

chords = ['D', 'A', 'G', 'D7', 'Bm', 'Em']
scale_changer(chords, capo_fret=3, original_scale='F', new_scale='C')

