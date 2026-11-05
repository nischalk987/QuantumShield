# Installation

QuantumShield currently provides a minimal, dependency-light Python package.
Simulator, decoder, and research dependencies will be introduced as their
interfaces are implemented and tested.

## Supported Python versions

The package metadata declares Python 3.10–3.13. The initial runtime package
uses only the Python standard library, so there are no scientific-library
version constraints yet. These are the declared support range; validate each
version in CI before publishing a release.

## Windows (PowerShell)

```powershell
git clone https://github.com/nischalk987/QuantumShield.git
cd QuantumShield
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pip check
python -c "import quantumshield; print(quantumshield.__version__)"
python -m pytest
```

If PowerShell blocks activation, use an approved execution policy or activate
from Command Prompt:

```bat
.venv\Scripts\activate.bat
```

## Linux

```bash
git clone https://github.com/nischalk987/QuantumShield.git
cd QuantumShield
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pip check
python -c "import quantumshield; print(quantumshield.__version__)"
python -m pytest
```

## Public version API

```python
import quantumshield

print(quantumshield.__version__)  # 0.1.0
```

`quantumshield.__version__` is the documented version API. No CLI entry point
is installed yet; it will be added with real CLI functionality rather than
pointing to a placeholder.

## Maintainer checks

Run from the repository root in a clean virtual environment:

```bash
python -m pip install -e ".[dev]"
python -m pip check
python -c "import quantumshield; assert quantumshield.__version__ == '0.1.0'"
python -m pytest
```
