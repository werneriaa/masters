#!/bin/zsh

# Run unittest discovery with coverage
coverage run -m unittest discover -s final_tests -p "test_final*.py"

# Generate coverage reports
echo "Generating coverage reports..."
coverage report
coverage html