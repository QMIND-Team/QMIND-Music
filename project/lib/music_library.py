"""
A library for all music-related functions
"""
from os import walk
import glob
from music21 import note, stream, converter
import math


# Takes a midi song as an input and outputs an array of features
def get_song_features(midi_path):
    majors = dict([("A-", 4), ("A", 3), ("B-", 2), ("B", 1), ("C", 0), ("C#", -1), ("D-", -1),
                   ("D", -2), ("E-", -3), ("E", -4), ("F", -5), ("F#", 6), ("G-", 6), ("G", 5), ("G#", 4)])
    minors = dict([("A-", 1), ("A", 0), ("B-", -1), ("B", -2), ("C", -3), ("C#", -4),
                   ("D-", -4), ("D", -5), ("E-", 6), ("E", 5), ("F", 4), ("F#", 3), ("G-", 3), ("G", 2), ("G#", 1)])

    score = converter.parse(midi_path)

    # Finding key and changing it to C major / A minor
    key = score.analyze('key')

    if key.mode == "major":
        halfSteps = majors[key.tonic.name]

    elif key.mode == "minor":
        halfSteps = minors[key.tonic.name]

    newscore = score.transpose(halfSteps)

    # Putting midi pitch, note name (number from 1 to 12), and duration in an array of dictionaries
    output_notes = []
    final_arr = [0] * 60
    for note in newscore.flat.notes:
        output_notes.append({
            'note': (note.pitch.midi-20) % 12,
            'real_note': (note.pitch.midi),
            'duration': math.ceil(note.seconds*2)/2
        })

    # Changing all non-diatonic notes to 0
    counter = 0
    valid_notes = [1, 3, 4, 6, 8, 9, 11]
    for x in output_notes:
        if x['note'] not in valid_notes:
            x['real_note'] = 0
        for i in range(1, int(x['duration']/0.5)):
            if int(counter)+i-1 < 60:
                final_arr[int(counter)+i-1] = x['real_note']
        counter += x['duration']/0.5

    return final_arr


def create_song_features_array():

    song_features_array = []
    # loops through midi files
    for (_, _, filenames) in walk("data/midi_songs"):
        for file_name in filenames:
            # calls the previous function and appends it to final 2d array
            song_features = get_song_features(f"data/midi_songs/{file_name}")
            song_features_array.append(song_features)

    return song_features_array
