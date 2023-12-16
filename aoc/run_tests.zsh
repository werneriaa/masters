#!/bin/zsh

# Run unittest discovery with coverage
coverage run -m unittest discover -s tests -p "test_*.py"

# Generate coverage reports
echo "Generating coverage reports..."
coverage report
coverage html