"""
xGrep: Filename and Content Change Stager

Recursively searches a directory for filenames and content that match a specific pattern and records the suggested changes. 
Specifically designed for updating "twitter" to "x"

Author: DJ @ DeepAI
Year: 2023
License: MIT

Usage:
    Simply run this script in the directory of interest. It will output a file 
    `detected_changes.json` with details on the detected changes.
"""

import os
import regex as re
from dataclasses import dataclass, field
from typing import List, Dict
import json

@dataclass
class Change:
    filename: str
    new_filename: str = None
    content_changes: List[str] = field(default_factory=list)

    def to_json(self) -> str:
        return json.dumps(self, default=self._serialize, indent=4)

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str, object_hook=cls._deserialize)
        return cls(**data)

    @staticmethod
    def _serialize(obj):
        """Custom JSON encoder for Change class"""
        if isinstance(obj, Change):
            return obj.__dict__
        raise TypeError(f"Object of type '{obj.__class__.__name__}' is not JSON serializable")

    @staticmethod
    def _deserialize(dct):
        """Custom JSON decoder for Change class"""
        return Change(**dct)


pattern = re.compile(r'(?<=\b|[-_])twitter(?=\b|[-_])')

def detect_changes(root_dir: str) -> Dict[str, Change]:
    changes = {}

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            change = Change(filename=full_path)

            # Check filename for targets
            new_filename = pattern.sub("x", filename)
            if filename != new_filename:
                change.new_filename = os.path.join(dirpath, new_filename)

            # Check file content for targets
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.readlines()
                for line in content:
                    if pattern.search(line):
                        change.content_changes.append(line.strip())

            if change.new_filename or change.content_changes:
                changes[full_path] = change

    return changes

def write_changes_to_file(changes: Dict[str, Change], output_file: str):
    """Write staged changes to a JSON file"""
    with open(output_file, 'w') as file:
        json.dump(changes, file, default=Change._serialize, indent=4)

def read_changes_from_file(input_file: str) -> Dict[str, Change]:
    """Read staged changes from a JSON file and return a dictionary of Change objects"""
    with open(input_file, 'r') as file:
        data = json.load(file)
        return {k: Change.from_json(json.dumps(v)) for k, v in data.items()}


if __name__ == "__main__":
    root_dir = "."
    changes = detect_changes(root_dir)
    output_file = "staged_changes.json"

    write_changes_to_file(changes, output_file)
    print(f"Detected changes written to {output_file}")
