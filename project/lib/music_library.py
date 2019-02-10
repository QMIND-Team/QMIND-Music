"""
A library for all music-related functions
"""
import os
import glob
from music21 import note, stream, converter
import math

# Takes an mp3 song as input and outputs a midi file
def convert_mp3_to_midi(song_path, midi_path):
    pass


# Takes a midi song as an input and outputs an array of features
def get_song_features(midi_path):
    majors = dict([("Ab", 4),("A", 3),("Bb", 2),("B", 1),("C", 0),("Db", -1),("D", -2),("Eb", -3),("E", -4),("F", -5),("Gb", 6),("G", 5)])
    minors = dict([("Ab", 1),("A", 0),("Bb", -1),("B", -2),("C", -3),("Db", -4),("D", -5),("Eb", 6),("E", 5),("F", 4),("Gb", 3),("G", 2)])

    score = converter.parse('cut_to_the_feeling.mid')

    #Finding key and changing it to C major / A minor
    key = score.analyze('key')
    print(key.tonic.name, key.mode)
    if key.mode == "major":
            halfSteps = majors[key.tonic.name]
            
    elif key.mode == "minor":
            halfSteps = minors[key.tonic.name]
        
    newscore = score.transpose(halfSteps)

    #Putting midi pitch, note name (number from 1 to 12), and duration in an array of dictionaries
    output_notes = []
    final_arr = [0]* 60
    offset = 0
    for note in newscore.flat.notes:
        new_note = note.pitch.midi
        output_notes.append({
            'note': (note.pitch.midi-20)%12,
            'real_note': (note.pitch.midi),
            'duration': math.ceil(note.seconds*2)/2
        })

    #Changing all non-diatonic notes to 0
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

