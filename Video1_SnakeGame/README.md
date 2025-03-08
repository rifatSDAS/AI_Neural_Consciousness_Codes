# Project Snake Game

## Description

This is a project for Neural Consciousness YourTube channel Video 1.

The project compares these four Large Language Models (LLMs)

1. `o3-mini-high` from OpenAI
2. `DeepSeek-R1` from DeepSeek
3. `Grok 3` from xAI
4. `Claude 3.7 Sonnet` from Anthropic

The task is to create a `Snake Game`.

## Prompt for LLMs

``` Create a simple snake game in Python. Use Pygame. Add scoring. Increase snake moving speed dynamically as it grows. Restart when snake hit the edge. Snake is green, food is red, and background is black color. Set game window 800x600 pixels. ```

## Code Test Environment

* VS Code IDS (Windows 10 OS)
* Python virtual environment

## Python Virtual Environment Setup

* Open VS Code IDE and create a project, e.g., SnakeGame.
* Open a new terminal in the project directory and run this
command

For Windows
``` python -m venv .venv ```
OR
``` py -3 -m venv .venv ```

For Linux/macOS
``` python3 -m venv .venv ```

> Here the virtual environment name is `.venv`.

* Activate virtual environment
For Windows
``` .\.venv\Scripts\activate ```

For Linus/macOS
``` source .venv/bin/activate ```

> [For more details on "Python environments in VS Code"](https://code.visualstudio.com/docs/python/environments)

* Install necessary libraries using `pip`
``` pip install pygame ```
