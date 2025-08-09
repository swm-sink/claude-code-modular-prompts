#!/bin/bash
# Cleanup root directory documentation debt
# Keeps only essential files in root, archives the rest

echo "================================================"
echo "Root Directory Cleanup Script"
echo "================================================"
echo ""

# Create archive directories if they don't exist
mkdir -p docs/archive/planning
mkdir -p docs/archive/guides  
mkdir -p docs/archive/reports
mkdir -p docs/archive/legacy

# Count files before cleanup
BEFORE_COUNT=$(ls *.md 2>/dev/null | wc -l)
echo "Files in root before cleanup: $BEFORE_COUNT"
echo ""

# Define essential files to keep in root
ESSENTIAL_FILES=(
    "README.md"
    "CLAUDE.md"
    "LICENSE.md"
    "PROJECT-STATE-VERIFICATION.md"
    "PROJECT-FINALIZATION-CHECKLIST.md"
    "INTEGRATION-ACHIEVEMENT.md"
    "INTEGRATION-GUIDE.md"
    "QUICKSTART.md"
    "claude.todos.yaml"
)

echo "Keeping essential files in root:"
for file in "${ESSENTIAL_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✓ $file"
    fi
done
echo ""

# Move different categories of files to appropriate archives
echo "Moving files to archive directories..."

# Move guides
for file in *GUIDE*.md; do
    if [[ ! " ${ESSENTIAL_FILES[@]} " =~ " ${file} " ]] && [ -f "$file" ]; then
        mv "$file" docs/archive/guides/ 2>/dev/null && echo "  → Moved $file to guides archive"
    fi
done

# Move reports
for file in *REPORT*.md *VALIDATION*.md *ASSESSMENT*.md; do
    if [[ ! " ${ESSENTIAL_FILES[@]} " =~ " ${file} " ]] && [ -f "$file" ]; then
        mv "$file" docs/archive/reports/ 2>/dev/null && echo "  → Moved $file to reports archive"
    fi
done

# Move legacy/historical documents
for file in *LEGACY*.md *DEPRECATED*.md *OLD*.md *ARCHIVE*.md; do
    if [[ ! " ${ESSENTIAL_FILES[@]} " =~ " ${file} " ]] && [ -f "$file" ]; then
        mv "$file" docs/archive/legacy/ 2>/dev/null && echo "  → Moved $file to legacy archive"
    fi
done

# Move remaining non-essential markdown files
for file in *.md; do
    # Skip if it's an essential file
    SKIP=false
    for essential in "${ESSENTIAL_FILES[@]}"; do
        if [ "$file" = "$essential" ]; then
            SKIP=true
            break
        fi
    done
    
    if [ "$SKIP" = false ] && [ -f "$file" ]; then
        mv "$file" docs/archive/planning/ 2>/dev/null && echo "  → Moved $file to planning archive"
    fi
done

echo ""

# Count files after cleanup
AFTER_COUNT=$(ls *.md 2>/dev/null | wc -l)
echo "Files in root after cleanup: $AFTER_COUNT"
echo "Files archived: $((BEFORE_COUNT - AFTER_COUNT))"
echo ""

# Show what remains in root
echo "Current root directory markdown files:"
ls -la *.md 2>/dev/null || echo "  No markdown files in root"
echo ""

# Summary of archive directories
echo "Archive summary:"
echo "  Planning documents: $(ls docs/archive/planning/*.md 2>/dev/null | wc -l) files"
echo "  Guides: $(ls docs/archive/guides/*.md 2>/dev/null | wc -l) files"
echo "  Reports: $(ls docs/archive/reports/*.md 2>/dev/null | wc -l) files"
echo "  Legacy: $(ls docs/archive/legacy/*.md 2>/dev/null | wc -l) files"
echo ""

echo "================================================"
echo "Cleanup Complete!"
echo "================================================"