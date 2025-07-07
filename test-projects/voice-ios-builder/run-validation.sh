#!/bin/bash

echo "🚀 Building Voice iOS Builder package..."
swift build

if [ $? -eq 0 ]; then
    echo "✅ Build successful"
    echo ""
    echo "🔄 Running integration validation..."
    
    # Add the build directory to the library path so Swift can find our modules
    export DYLD_LIBRARY_PATH=.build/debug:$DYLD_LIBRARY_PATH
    
    # Run our validation script with the built modules
    swift -I .build/debug -L .build/debug validate-integration.swift
    
    echo ""
    echo "🎯 Integration validation complete!"
else
    echo "❌ Build failed - cannot run validation"
    exit 1
fi