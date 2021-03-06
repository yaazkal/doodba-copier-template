"""Template migration scripts.

This file is executed through invoke by copier when updating child projects.
"""
import shutil
from pathlib import Path

from invoke import task


@task
def from_doodba_scaffolding_to_copier(c):
    print("Removing remaining garbage from doodba-scaffolding.")
    shutil.rmtree(Path(".vscode", "doodba"), ignore_errors=True)
    garbage = (
        Path(".travis.yml"),
        Path(".vscode", "doodbasetup.py"),
        Path("odoo", "custom", "src", "private", ".empty"),
    )
    for path in garbage:
        try:
            path.unlink()
        except FileNotFoundError:
            pass
    # When using Copier >= 3.0.5, this file didn't get properly migrated
    editorconfig_file = Path(".editorconfig")
    editorconfig_contents = editorconfig_file.read_text()
    editorconfig_contents = editorconfig_contents.replace(
        "[*.yml]", "[*.{code-snippets,code-workspace,json,md,yaml,yml}{,.jinja}]", 1
    )
    editorconfig_file.write_text(editorconfig_contents)
