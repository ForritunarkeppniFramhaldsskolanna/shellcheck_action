import json
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

json_string = sys.stdin.read()

annotation_list = json.loads(json_string)

#{"file":"scripts/check_accepted.sh","line":29,"endLine":29,"column":38,"endColumn":59,"level":"error","code":2068,"message":"Double quote array expansions to avoid re-splitting elements.","fix":null}

for annotation in annotation_list:
    file_name = quote(annotation[FILE])
    line = annotation[LINE]
    end_line = annotation[END_LINE]
    column = annotation[COLUMN]
    end_column = annotation[END_COLUMN]
    level = annotation[LEVEL]
    code = annotation[CODE]
    message = annotation[MESSAGE]
    print(f"::error file={file_name},line={line},endLine={end_line},column={column},endColumn={end_column}::CS{code}: {message}")

if len(annotation_list) > 0:
    sys.exit(1)
