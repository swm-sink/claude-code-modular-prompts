#!/bin/bash
# reset.sh - Clear consultation state for fresh start
# One of only 5 allowed scripts

set -e

echo "= Claude Context Architect - Reset"
echo "==================================="

echo "This will clear:"
echo "- Consultation session state"
echo "- Generated commands"
echo "- PROJECT-DNA"
echo ""
read -p "Are you sure? (y/N): " confirm

if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
    rm -rf outputs/consultation-sessions/*
    rm -rf outputs/generated-commands/*
    rm -rf outputs/project-dna/*
    echo " Reset complete. Run './scripts/consultation.sh' to start fresh."
else
    echo "L Reset cancelled."
fi