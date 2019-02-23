"""
A library for all functions MIDI-related
"""
import vamp
import librosa
import numpy as np

from os import walk, path, mkdir, listdir
from scipy.signal import medfilt
from midiutil.MidiFile import MIDIFile

"""
Convert from MIDI format to an array of notes
"""


def midi_to_notes(midi, fs, hop, smooth, minduration):

    # smooth midi pitch sequence first
    if (smooth > 0):
        filter_duration = smooth  # in seconds
        filter_size = int(filter_duration * fs / float(hop))
        if filter_size % 2 == 0:
            filter_size += 1
        midi_filt = medfilt(midi, filter_size)
    else:
        midi_filt = midi

    notes = []
    p_prev = 0
    duration = 0
    onset = 0
    for n, p in enumerate(midi_filt):
        if p == p_prev:
            duration += 1
        else:
            # treat 0 as silence
            if p_prev > 0:
                # add note
                duration_sec = duration * hop / float(fs)
                # only add notes that are long enough
                if duration_sec >= minduration:
                    onset_sec = onset * hop / float(fs)
                    notes.append((onset_sec, duration_sec, p_prev))

            # start new note
            onset = n
            duration = 1
            p_prev = p

    # add last note
    if p_prev > 0:
        # add note
        duration_sec = duration * hop / float(fs)
        onset_sec = onset * hop / float(fs)
        notes.append((onset_sec, duration_sec, p_prev))

    return notes


"""
Convert from frequency in Hz to MIDI format
"""


def hz2midi(hz):
    # convert from Hz to midi note
    hz_nonneg = hz.copy()
    idx = hz_nonneg <= 0
    hz_nonneg[idx] = 1
    midi = 69 + 12*np.log2(hz_nonneg/440.)
    midi[idx] = 0

    # round
    midi = np.round(midi)

    return midi


"""
Saves an array of notes as a midi file
"""


def save_midi(outfile, notes, tempo):
    track = 0
    time = 0
    midifile = MIDIFile(1)

    # Add track name and tempo.
    midifile.addTrackName(track, time, "MIDI TRACK")
    midifile.addTempo(track, time, tempo)

    channel = 0
    volume = 100

    for note in notes:
        onset = note[0] * (tempo/60.)
        duration = note[1] * (tempo/60.)
        # duration = 1
        pitch = int(note[2])
        midifile.addNote(track, channel, pitch, onset, duration, volume)

    # And write it to disk.
    binfile = open(outfile, 'wb')
    midifile.writeFile(binfile)
    binfile.close()


"""
Convert all mp3 files to MIDI
"""


def create_midi_files():
    smooth = 0.25
    minduration = 0.1
    fs = 44100
    hop = 128

    # Make the folder if it doesn't already exist
    if not path.isdir('data/song_preview_clips'):
        mkdir('data/song_preview_clips')

    # If files are already in the folder we are done
    if len(listdir('data/song_preview_clips')) != 0:
        return

    for (_, _, filenames) in walk("data/song_preview_clips"):
        for file_name in filenames:
            data, sr = librosa.load(
                f"data/song_preview_clips/{file_name}", sr=fs, mono=True)

            melody = vamp.collect(data, sr, "mtg-melodia:melodia",
                                  parameters={"voicing": 0.2})

            pitch = melody['vector'][1]
            midi_pitch = hz2midi(pitch)

            notes = midi_to_notes(midi_pitch, fs, hop, smooth, minduration)
            save_midi(
                f'data/midi_songs/{file_name.replace(".mp3", ".mid")}', notes, 115)
            print(f"converted {file_name}")
