'''Send commands to the birdinator.'''

import subprocess
import pathlib

from flask import Flask

app = Flask(__name__)

@app.route('/honk')
def honk():
    '''Play a honking sound.'''

    filename = pathlib.Path(
        'sounds/Canadian Geese Honk-SoundBible.com-611844731.mp3')

    if not filename.exists():
        msg = '%s does not exist!' % str(filename)
    else:
        msg = 'The honk command has been sent.'
        subprocess.Popen([
            'cvlc', '--play-and-exit', '--no-loop', str(filename)])

    return {
        'message': msg,
    }

if __name__ == '__main__':
    app.run(debug=True)
