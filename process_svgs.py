"""
Simple script to extract path data from a sequence of SVGs in a directory and
save them to a JSON file.

Usage:
    python process_svgs.py path/to/input/directory/*.svg
    python process_svgs.py path/to/input/directory/*.svg -o path/to/output/file.json

"""

import os, sys
import json
import argparse
from glob import glob
from xml.dom import minidom

def extract_path_data(svg_file):
    """ Extracts the `d` attribute from the path tag in an SVG file """
    doc = minidom.parse(svg_file)
    paths = doc.getElementsByTagName('path')
    if not paths or len(paths) <= 0:
        return None
    return paths[0].getAttribute('d')

def extract_svgs(glob_path):
    """ Extract path data from each SVG file in a directory """
    path_data = []
    files = glob(glob_path)
    total = len(files)
    for i, svg_file in enumerate(files):
        path_data.append(extract_path_data(svg_file))
        show_progress(i, total)
    return path_data

def process_svgs(in_dir, out_dir):
    out_dir = os.path.abspath(out_dir)
    with open(out_dir, 'w') as fp:
        json.dump(extract_svgs(in_dir), fp)
    
    sys.stdout.write(f'\rSaved to: {out_dir}\r\n')
    sys.stdout.flush()

def show_progress(current, total):
    """ Displays nicely formatted progress in stdout """
    percent = int(100.0*current/total)
    totdigit = len(str(total))
    sys.stdout.write(f'\rProcessed: {current:>{totdigit}}/{total} - {percent:>3}%')
    sys.stdout.flush()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extracts path data from SVG files in a directory and saves them to a JSON file.")
    parser.add_argument("input", help="The input path to directory containing SVG files (glob format)")
    parser.add_argument("-o", "--output", default="pathdata.json", help="The output path for the resulting JSON file")
    args = parser.parse_args()

    process_svgs(args.input, args.output)