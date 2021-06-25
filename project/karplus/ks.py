"""
ks.py

Uses the Karplus String algorithm to generate musical notes 
in a pentatonic scale.

Author: Mahesh Venkitachalam
"""

import sys, os
import time, random 
import wave, argparse, pygame 
import numpy as np
from collections import deque
from matplotlib import pyplot as plt

# show plot of algorithm in action?
g_show_plot = False

# notes of a Pentatonic Minor scale
# piano C4-E(b)-F-G-B(b)-C5
pm_notes = {'C4': 262, 'Eb': 311, 'F': 349, 'G':391, 'Bb':466}


# write out WAVE file
def write_wave(fname, data):
    # open file 
    file = wave.open(fname, 'wb')
    # WAV file parameters 
    n_channels = 1
    sample_width = 2
    frame_rate = 44100
    n_frames = 44100
    # set parameters
    file.setparams((n_channels, sample_width, frame_rate, n_frames,
                    'NONE', 'noncompressed'))
    file.writeframes(data)
    file.close()


# generate note of given frequency
def generate_note(freq):
    n_samples = 44100
    sample_rate = 44100
    N = int(sample_rate/freq)
    # initialize ring buffer
    buf = deque([random.random() - 0.5 for i in range(N)])
    # plot of flag set 
    if g_show_plot:
        axline, = plt.plot(buf)
    # init sample buffer
    samples = np.array([0]*n_samples, 'float32')
    for i in range(n_samples):
        samples[i] = buf[0]
        avg = 0.995*0.5*(buf[0] + buf[1])
        buf.append(avg)
        buf.popleft()  
        # plot of flag set 
        if g_show_plot:
            if i % 1000 == 0:
                axline.set_ydata(buf)
                plt.draw()
      
    # samples to 16-bit to string
    # max value is 32767 for 16-bit
    samples = np.array(samples * 32767, 'int16')
    return samples.tostring()


# play a wav file
class NotePlayer:

    # constr
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 2048)
        pygame.init()
        # dictionary of notes
        self.notes = {}

    # add a note
    def add(self, fileName):
        self.notes[fileName] = pygame.mixer.Sound(fileName)

    # play a note
    def play(self, fileName):
        try:
            self.notes[fileName].play()
        except:
            print(fileName + ' not found!')

    def play_random(self):
        """play a random note"""
        index = random.randint(0, len(self.notes)-1)
        note = list(self.notes.values())[index]
        note.play()


# main() function
def main():
    # declare global var
    global g_show_plot

    parser = argparse.ArgumentParser(description="Generating sounds with Karplus String Algorithm.")
    # add arguments
    parser.add_argument('--display', action='store_true', required=False)
    parser.add_argument('--play', action='store_true', required=False)
    parser.add_argument('--piano', action='store_true', required=False)
    args = parser.parse_args()

    # show plot if flag set
    if args.display:
        g_show_plot = True
        plt.ion()

    # create note player
    n_player = NotePlayer()

    print('creating notes...')
    for name, freq in list(pm_notes.items()):
        file_name = name + '.wav'
        if not os.path.exists(file_name) or args.display:
            data = generate_note(freq)
            print('creating ' + file_name + '...')
            write_wave(file_name, data)
        else:
            print('fileName already created. skipping...')
        
        # add note to player
        n_player.add(name + '.wav')
        
        # play note if display flag set
        if args.display:
            n_player.play(name + '.wav')
            time.sleep(0.5)
    
    # play a random tune
    if args.play:
        while True:
            try: 
                n_player.play_random()
                # rest - 1 to 8 beats
                rest = np.random.choice([1, 2, 4, 8], 1, 
                                        p=[0.15, 0.7, 0.1, 0.05])
                time.sleep(0.25*rest[0])
            except KeyboardInterrupt:
                exit()

    # random piano mode
    if args.piano:
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.KEYUP):
                    print("key pressed")
                    n_player.play_random()
                    time.sleep(0.5)


# call main
if __name__ == '__main__':
    main()
