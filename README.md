# AntropicCourse

## First-time setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install anthropic python-dotenv
```

## Every time you open a new terminal

```bash
source venv/bin/activate
```

You're inside venv when you see `(venv)` at the start of the terminal prompt.

## Deactivate venv

```bash
deactivate
```

## Environment variables

Create a `.env` file in the project root and add your API key:

```
ANTHROPIC_API_KEY=your_api_key_here
```

> Never commit `.env` to git — it contains secret keys.

## Save/restore dependencies

```bash
# Save installed packages to a file
pip freeze > requirements.txt

# Install from file (e.g. after git clone)
pip install -r requirements.txt
```# AntropicCourse
