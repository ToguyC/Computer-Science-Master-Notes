from pathlib import Path
from typing import List

from lib.file_loader import FileLoader

# Those are hardcoded, for easier modularity
MASTER_SEMESTERS = [
    r"Computer Science Master --- Semester 1 \\ Autumn 2024",
    r"Computer Science Master --- Semester 2 \\ Spring 2025",
    r"Computer Science Master --- Semester 3 \\ Autumn 2025",
    r"Computer Science Master --- Semester 4 \\ Spring 2026",
]

class Course:
    def __init__(self, semester: int, name: str, is_summary: bool = False):
        self.semester = semester
        self.name = name
        self.is_summary = is_summary

    def __repr__(self) -> str:
        return f"Course({self.name}, {self.is_bachelor}, {self.semester}, {self.is_summary})"

    @property
    def root_path(self) -> Path:
        diploma = "MA"
        return Path(f"{diploma}{self.semester}/{self.name}") 
    
    @property
    def loader(self) -> FileLoader:
        return FileLoader(self.root_path)
    
    def date(self) -> str:
        names = MASTER_SEMESTERS
        semester = self.semester - 1
        return names[semester]
