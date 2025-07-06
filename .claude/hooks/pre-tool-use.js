#!/usr/bin/env node
/**
 * Claude Code Pre-Tool-Use Hook
 * Auto-approves all tool usage to bypass permission prompts
 * 
 * This is an ALTERNATIVE to the symlink solution.
 * The symlink solution is simpler and recommended.
 */

// Check if we want to auto-approve (can be controlled via env var)
const AUTO_APPROVE = process.env.CLAUDE_AUTO_APPROVE !== 'false';

if (AUTO_APPROVE) {
  // Auto-approve all tools
  console.log(JSON.stringify({
    decision: "approve",
    reason: "Auto-approved by permission hook"
  }));
} else {
  // Pass through to normal permission system
  console.log(JSON.stringify({
    decision: "continue",
    reason: "Manual approval required"
  }));
}

// Log for debugging (to stderr so it doesn't interfere with output)
if (process.env.CLAUDE_HOOK_DEBUG) {
  console.error(`[Permission Hook] Auto-approve: ${AUTO_APPROVE}`);
}