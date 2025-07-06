#!/bin/bash
# Validate all prompts in the framework

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROMPTS_DIR="$SCRIPT_DIR/../prompts"
VALIDATOR="$SCRIPT_DIR/validate_prompt.py"

echo "🔍 Validating all prompts in Claude Code framework..."
echo "=================================================="

# Check if validator exists
if [ ! -f "$VALIDATOR" ]; then
    echo "❌ Error: Validator script not found at $VALIDATOR"
    exit 1
fi

# Check if prompts directory exists
if [ ! -d "$PROMPTS_DIR" ]; then
    echo "❌ Error: Prompts directory not found at $PROMPTS_DIR"
    exit 1
fi

# Run validation
echo "📂 Validating prompts in: $PROMPTS_DIR"
echo

# Run the validator with color output
python3 "$VALIDATOR" "$PROMPTS_DIR" --verbose

# Capture exit code
EXIT_CODE=$?

echo
echo "=================================================="

if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ All prompts validated successfully!"
else
    echo "❌ Validation failed. Please fix the errors above."
fi

# Additional checks
echo
echo "📊 Prompt Statistics:"
echo "-------------------"

# Count prompts by category
for category in queries features reviews patterns templates; do
    count=$(find "$PROMPTS_DIR/$category" -name "*.json" 2>/dev/null | wc -l)
    printf "%-12s: %d prompts\n" "$category" "$count"
done

# Count total prompts
total=$(find "$PROMPTS_DIR" -name "*.json" -not -path "*/archived/*" | grep -v prompt-schema.json | wc -l)
echo "-------------------"
echo "Total active : $total prompts"

# Count archived prompts
archived=$(find "$PROMPTS_DIR/archived" -name "*.json" 2>/dev/null | wc -l)
echo "Archived     : $archived prompts"

exit $EXIT_CODE