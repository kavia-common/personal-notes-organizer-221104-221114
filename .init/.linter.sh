#!/bin/bash
cd /home/kavia/workspace/code-generation/personal-notes-organizer-221104-221114/backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

