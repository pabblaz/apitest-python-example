# API Testing Example with Behave

This project contains API testing examples using the backend_lib.

## Requirements

- Python 3.11
- pip
- Git

## Installation

1. Clone both repositories:

```bash
# Clone the backend_lib repository
git clone https://github.com/pabblaz/backend-lib.git
cd backend_lib

# Install backend_lib in development mode
pip install -e .

# Go back and clone this example repository
cd ..
git clone https://github.com/pabblaz/apitest-python-example.git
cd apitest-python-example
```

2. Create a virtual environment:
```bash
python -m venv ENV/ve
source ve/bin/activate  # On Windows: ve\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the tests

To run the tests, from the project root folder:

```bash
behave
```

## Project Structure

- `features/`: Contains Behave feature files and step definitions
  - `api_test.feature`: Test scenarios definition
  - `steps/`: Python step implementations

## Development Notes

### Local Development with backend_lib

Since `backend_lib` is a local dependency, you need to install it in development mode. This means:

1. The `backend_lib` repository must be cloned and installed first
2. Any changes made to `backend_lib` will be immediately reflected in this project
3. You don't need to reinstall `backend_lib` after making changes to it

If you need to update `backend_lib`:
```bash
cd path/to/backend_lib
git pull
pip install -e .
```

## Troubleshooting

If you encounter any issues with the `backend_lib` dependency:

1. Make sure you have installed `backend_lib` in development mode using `pip install -e .`
2. Verify that both repositories are in the correct Python environment
3. Check that the `backend_lib` installation was successful by running:
```bash
pip list | grep backend-framework
```

You should see the package listed with its version number.