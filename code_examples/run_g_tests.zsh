#!/bin/zsh

# Run unittest discovery with coverage
coverage run -m unittest discover -s generated_tests -p "test_generated*.py"

# Generate coverage reports
echo "Generating coverage reports..."
coverage report
coverage html