# Bad Apple!!.SVG

Bad Apple playing in SVG format in real time right in the browser!

(**Try it!**)[https://buzzbyte.github.io/BadApple.SVG]

## How I did it

I simply downloaded the original video, encoded it to 15 FPS and converted it
to a monochrome bitmap image sequence with FFMPEG, then used
[Potrace](http://potrace.sourceforge.net) to convert the frames to single-path
SVG files. I then wrote a script (`process_svgs.py`) to extract the path data
from each SVG file, append it to a list, and save it as a JSON file for
Javascript to handle.

The animation is done by using a `requestAnimationFrame` loop iterating through
each frame and updating the SVG with the path data for each frame at 15 FPS.
The loop uses the audio's timing to ensure it syncs properly.

## but why tho?

Why not?
