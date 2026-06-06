# MIT License
#
# Copyright (c) 2026 Irene Hofstetter
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Main entry point."""

import typer

from .commands import ch01
from .commands import ch02

app = typer.Typer(
    name="python101",
    help="A dynamic learning environment and development framework for Python, leveraging Typer for an interactive command-line interface.",
    add_completion=False,
)

app.command(ch01)
app.command(ch02)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Description of the function."""
    if ctx.invoked_subcommand is None:
        print("Hello from python101! (Main Menu)")


def run():
    """Run the Typer app."""
    app()


if __name__ == "__main__":
    run()
