# Bad Apple!!.SVG

Bad Apple playing in SVG format right in the browser!

## How it works

I simply downloaded the original video, encoded it to 15 FPS and converted it
to a monochrome image sequence with FFMPEG, then used
[imagetracerjs](jankovicsandras/imagetracerjs) to convert each frame to SVG
paths, added some CSS classes to each path nessesary for animating it, and
wrapped it in SVG format (the code I used is still in the repo).
I let it run (took a few hours to trace all the frames) then saved the output
to an SVG file.

The animation is done by simply showing the path of one frame and hiding the
rest. I iterated through them using a `setTimeout` set for 67 ms
(1/15 * 1000 = 66.6) for each frame.

Currently, it doesn't play audio since it doesn't play all the frames properly
(it skips some frames due to how I encoded it initially), but I can try to fix
that in the future.
