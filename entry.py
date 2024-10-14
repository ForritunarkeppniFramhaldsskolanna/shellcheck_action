#!/usr/bin/env python3
import glob
import json
import shlex
import subprocess
import sys

from urllib.parse import quote

FILE = "file"
LINE = "line"
END_LINE = "endLine"
COLUMN = "column"
END_COLUMN = "endColumn"
LEVEL = "level"
CODE = "code"
MESSAGE = "message"
FIX = "fix"

# Exit code 3 means could not parse output of shellcheck
# Exit code 2 means wrong usage
# Exit code 1 means some errors were found (there is output)
# Exit code 0 means all good

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(f"Usage: {sys.argv[0]} '<files>' '[shellcheck_args]'")
        sys.exit(2)

    files = []
    for token in shlex.split(sys.argv[1]):
        files.extend(glob.glob(token))
    
    if len(files) == 0:
        print("Warning: No files specified.")
        sys.exit(0)

    shellcheck_args = sys.argv[2] if len(sys.argv) > 2 else ''

    command = ['shellcheck'] + files + shlex.split(shellcheck_args) + ['--format=json']
    process = subprocess.run(command, capture_output=True)
    json_string = process.stdout
    try:
        annotation_list = json.loads(json_string)
    except json.JSONDecodeError as e:
        print(e)
        sys.exit(3)

    for annotation in annotation_list:
        file_name = quote(annotation[FILE])
        line = annotation[LINE]
        end_line = annotation[END_LINE]
        column = annotation[COLUMN]
        end_column = annotation[END_COLUMN]
        level = annotation[LEVEL]
        code = annotation[CODE]
        message = annotation[MESSAGE]
        print(f"::error file={file_name},line={line},endLine={end_line},column={column},endColumn={end_column}::SC{code} ({level}): {message}")

    if len(annotation_list) > 0:
        sys.exit(1)
