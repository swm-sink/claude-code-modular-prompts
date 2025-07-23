"""
Context Window Optimizer

Real context window optimization with measurable compression techniques
and performance tracking.
"""

import re
import json
import time
from typing import Dict, Any, Optional, List, Tuple, Set
from datetime import datetime
from dataclasses import dataclass
from collections import Counter
import hashlib


@dataclass
class CompressionResult:
    """Results from context compression operation"""
    original_length: int
    compressed_length: int
    compression_ratio: float
    compression_time_seconds: float
    technique_used: str
    tokens_saved: int
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "original_length": self.original_length,
            "compressed_length": self.compressed_length,
            "compression_ratio": self.compression_ratio,
            "compression_time_seconds": self.compression_time_seconds,
            "technique_used": self.technique_used,
            "tokens_saved": self.tokens_saved
        }


class ContextWindowOptimizer:
    """Real context window optimization with measurable results"""
    
    def __init__(self):
        self.compression_history: List[CompressionResult] = []
        self.whitespace_pattern = re.compile(r'\s+')
        self.comment_patterns = [
            re.compile(r'#.*$', re.MULTILINE),  # Python/shell comments
            re.compile(r'//.*$', re.MULTILINE),  # C/JS style comments
            re.compile(r'/\*.*?\*/', re.DOTALL),  # Multi-line comments
        ]
        self.redundancy_cache: Dict[str, str] = {}
    
    def estimate_token_count(self, text: str) -> int:
        """Rough token count estimation (4 chars ≈ 1 token for English)"""
        # More accurate estimation based on common patterns
        word_count = len(text.split())
        char_count = len(text)
        
        # Weighted average: words are roughly 1.3 tokens, chars are roughly 0.25 tokens
        estimated_tokens = int((word_count * 1.3) + (char_count * 0.25)) // 2
        return max(estimated_tokens, char_count // 4)  # Minimum fallback
    
    def compress_whitespace(self, text: str) -> str:
        """Compress excessive whitespace while preserving structure"""
        # Replace multiple spaces with single spaces
        compressed = self.whitespace_pattern.sub(' ', text)
        
        # Remove trailing/leading whitespace on lines
        lines = compressed.split('\n')
        lines = [line.strip() for line in lines]
        
        # Remove empty lines but preserve single line breaks
        result_lines = []
        prev_empty = False
        
        for line in lines:
            if not line:
                if not prev_empty:
                    result_lines.append('')
                prev_empty = True
            else:
                result_lines.append(line)
                prev_empty = False
        
        return '\n'.join(result_lines)
    
    def remove_comments(self, text: str) -> str:
        """Remove comments while preserving code structure"""
        result = text
        for pattern in self.comment_patterns:
            result = pattern.sub('', result)
        return result
    
    def compress_repeated_patterns(self, text: str, min_length: int = 10, min_occurrences: int = 3) -> Tuple[str, Dict[str, str]]:
        """Identify and compress repeated patterns"""
        # Find repeated substrings
        patterns = {}
        lines = text.split('\n')
        
        # Look for repeated lines
        line_counts = Counter(lines)
        replacements = {}
        placeholder_counter = 1
        
        for line, count in line_counts.items():
            if count >= min_occurrences and len(line) >= min_length:
                placeholder = f"__PATTERN_{placeholder_counter}__"
                replacements[placeholder] = line
                patterns[line] = placeholder
                placeholder_counter += 1
        
        # Apply replacements
        compressed_lines = []
        for line in lines:
            if line in patterns:
                compressed_lines.append(patterns[line])
            else:
                compressed_lines.append(line)
        
        return '\n'.join(compressed_lines), replacements
    
    def intelligent_summarization(self, text: str, target_ratio: float = 0.7) -> str:
        """Intelligent text summarization to reduce context size"""
        lines = text.split('\n')
        total_lines = len(lines)
        target_lines = int(total_lines * target_ratio)
        
        if target_lines >= total_lines:
            return text
        
        # Score lines by importance
        line_scores = []
        
        for i, line in enumerate(lines):
            score = 0
            line_clean = line.strip()
            
            # Skip empty lines initially
            if not line_clean:
                score = -10
            
            # Prefer lines with keywords
            keywords = ['def ', 'class ', 'import ', 'from ', 'if ', 'return ', 'error', 'warning']
            for keyword in keywords:
                if keyword in line_clean.lower():
                    score += 5
            
            # Prefer lines with structured data
            if any(char in line_clean for char in ['{', '}', '[', ']', ':', '=']):
                score += 2
            
            # Penalize very short or very long lines
            if len(line_clean) < 10:
                score -= 2
            elif len(line_clean) > 200:
                score -= 1
            
            line_scores.append((score, i, line))
        
        # Sort by score and keep top lines
        line_scores.sort(key=lambda x: x[0], reverse=True)
        selected_indices = sorted([x[1] for x in line_scores[:target_lines]])
        
        # Reconstruct text with selected lines
        result_lines = [lines[i] for i in selected_indices]
        
        # Add summary note
        removed_count = total_lines - len(result_lines)
        if removed_count > 0:
            summary_note = f"\n# [CONTEXT OPTIMIZER] Removed {removed_count} less relevant lines for efficiency\n"
            result_lines.insert(0, summary_note)
        
        return '\n'.join(result_lines)
    
    def compress_json_data(self, text: str) -> str:
        """Compress JSON data within text"""
        # Find JSON blocks
        json_pattern = re.compile(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', re.MULTILINE | re.DOTALL)
        
        def compress_json_match(match):
            json_str = match.group(0)
            try:
                # Parse and reformat compactly
                data = json.loads(json_str)
                return json.dumps(data, separators=(',', ':'))
            except (json.JSONDecodeError, ValueError):
                return json_str  # Return original if parsing fails
        
        return json_pattern.sub(compress_json_match, text)
    
    def optimize_context(self, text: str, technique: str = "comprehensive", target_ratio: float = 0.7) -> CompressionResult:
        """Optimize context window with specified technique.
        
        Refactored for improved maintainability and testability.
        """
        start_time = time.time()
        original_metrics = self._calculate_original_metrics(text)
        
        compressed = self._apply_compression_technique(text, technique, target_ratio, original_metrics['length'])
        
        result = self._create_compression_result(
            original_metrics, compressed, technique, start_time
        )
        
        self.compression_history.append(result)
        return result
    
    def _calculate_original_metrics(self, text: str) -> dict:
        """Calculate original text metrics."""
        return {
            'length': len(text),
            'tokens': self.estimate_token_count(text)
        }
    
    def _apply_compression_technique(self, text: str, technique: str, target_ratio: float, original_length: int) -> str:
        """Apply the specified compression technique to the text."""
        technique_methods = {
            "whitespace_only": self._compress_whitespace_only,
            "remove_comments": self._compress_remove_comments,
            "pattern_compression": self._compress_patterns,
            "json_compression": self._compress_json,
            "intelligent_summary": lambda t: self.intelligent_summarization(t, target_ratio),
            "comprehensive": lambda t: self._compress_comprehensive(t, target_ratio, original_length)
        }
        
        compression_method = technique_methods.get(technique, lambda t: t)
        return compression_method(text)
    
    def _compress_whitespace_only(self, text: str) -> str:
        """Apply whitespace-only compression."""
        return self.compress_whitespace(text)
    
    def _compress_remove_comments(self, text: str) -> str:
        """Apply comment removal compression."""
        return self.compress_whitespace(self.remove_comments(text))
    
    def _compress_patterns(self, text: str) -> str:
        """Apply pattern compression."""
        compressed = self.compress_whitespace(text)
        compressed, _ = self.compress_repeated_patterns(compressed)
        return compressed
    
    def _compress_json(self, text: str) -> str:
        """Apply JSON compression."""
        return self.compress_json_data(self.compress_whitespace(text))
    
    def _compress_comprehensive(self, text: str, target_ratio: float, original_length: int) -> str:
        """Apply comprehensive compression with multiple techniques."""
        compressed = self.compress_whitespace(text)
        compressed = self.remove_comments(compressed)
        compressed = self.compress_json_data(compressed)
        compressed, _ = self.compress_repeated_patterns(compressed)
        
        if len(compressed) > original_length * target_ratio:
            compressed = self.intelligent_summarization(compressed, target_ratio)
        
        return compressed
    
    def _create_compression_result(self, original_metrics: dict, compressed: str, technique: str, start_time: float) -> CompressionResult:
        """Create compression result from metrics."""
        compression_time = time.time() - start_time
        compressed_length = len(compressed)
        compressed_tokens = self.estimate_token_count(compressed)
        
        compression_ratio = compressed_length / original_metrics['length'] if original_metrics['length'] > 0 else 1.0
        tokens_saved = max(0, original_metrics['tokens'] - compressed_tokens)
        
        return CompressionResult(
            original_length=original_metrics['length'],
            compressed_length=compressed_length,
            compression_ratio=compression_ratio,
            compression_time_seconds=compression_time,
            technique_used=technique,
            tokens_saved=tokens_saved
        )
    
    def adaptive_compression(self, text: str, context_limit: int) -> Tuple[str, CompressionResult]:
        """Adaptively compress text to fit within context limit"""
        estimated_tokens = self.estimate_token_count(text)
        
        if estimated_tokens <= context_limit:
            # No compression needed
            result = CompressionResult(
                original_length=len(text),
                compressed_length=len(text),
                compression_ratio=1.0,
                compression_time_seconds=0.0,
                technique_used="none_needed",
                tokens_saved=0
            )
            return text, result
        
        # Calculate required compression ratio
        required_ratio = context_limit / estimated_tokens
        
        # Try different compression techniques in order of preference
        techniques = [
            ("whitespace_only", 1.0),
            ("remove_comments", 1.0),
            ("json_compression", 1.0),
            ("pattern_compression", 1.0),
            ("intelligent_summary", required_ratio * 0.9),  # Aim slightly under target
            ("comprehensive", required_ratio * 0.8)
        ]
        
        for technique, target_ratio in techniques:
            result = self.optimize_context(text, technique, target_ratio)
            # result.compressed_length is already an integer, pass it directly
            compressed_tokens = result.compressed_length // 4  # Simple approximation
            
            if compressed_tokens <= context_limit:
                # Reconstruct the compressed text
                compressed_text = self.optimize_context(text, technique, target_ratio)
                return self._reconstruct_compressed_text(text, technique, target_ratio), result
        
        # If all techniques fail, use aggressive summarization
        aggressive_ratio = context_limit / estimated_tokens * 0.5
        result = self.optimize_context(text, "intelligent_summary", aggressive_ratio)
        compressed_text = self.intelligent_summarization(text, aggressive_ratio)
        
        return compressed_text, result
    
    def _reconstruct_compressed_text(self, text: str, technique: str, target_ratio: float) -> str:
        """Reconstruct compressed text for given technique"""
        if technique == "whitespace_only":
            return self.compress_whitespace(text)
        elif technique == "remove_comments":
            return self.compress_whitespace(self.remove_comments(text))
        elif technique == "pattern_compression":
            compressed = self.compress_whitespace(text)
            compressed, _ = self.compress_repeated_patterns(compressed)
            return compressed
        elif technique == "json_compression":
            return self.compress_json_data(self.compress_whitespace(text))
        elif technique == "intelligent_summary":
            return self.intelligent_summarization(text, target_ratio)
        elif technique == "comprehensive":
            compressed = self.compress_whitespace(text)
            compressed = self.remove_comments(compressed)
            compressed = self.compress_json_data(compressed)
            compressed, _ = self.compress_repeated_patterns(compressed)
            if len(compressed) > len(text) * target_ratio:
                compressed = self.intelligent_summarization(compressed, target_ratio)
            return compressed
        else:
            return text
    
    def get_compression_statistics(self) -> Dict[str, Any]:
        """Get comprehensive compression statistics"""
        if not self.compression_history:
            return {"error": "No compression history available"}
        
        total_compressions = len(self.compression_history)
        total_original_length = sum(r.original_length for r in self.compression_history)
        total_compressed_length = sum(r.compressed_length for r in self.compression_history)
        total_tokens_saved = sum(r.tokens_saved for r in self.compression_history)
        total_time = sum(r.compression_time_seconds for r in self.compression_history)
        
        # Calculate averages
        avg_compression_ratio = sum(r.compression_ratio for r in self.compression_history) / total_compressions
        avg_compression_time = total_time / total_compressions
        
        # Technique usage statistics
        technique_counts = Counter(r.technique_used for r in self.compression_history)
        
        # Best and worst compressions
        best_compression = min(self.compression_history, key=lambda x: x.compression_ratio)
        worst_compression = max(self.compression_history, key=lambda x: x.compression_ratio)
        
        return {
            "total_compressions": total_compressions,
            "total_characters_processed": total_original_length,
            "total_characters_saved": total_original_length - total_compressed_length,
            "total_tokens_saved": total_tokens_saved,
            "average_compression_ratio": avg_compression_ratio,
            "average_compression_time_seconds": avg_compression_time,
            "total_compression_time_seconds": total_time,
            "technique_usage": dict(technique_counts),
            "best_compression": {
                "ratio": best_compression.compression_ratio,
                "technique": best_compression.technique_used,
                "tokens_saved": best_compression.tokens_saved
            },
            "worst_compression": {
                "ratio": worst_compression.compression_ratio,
                "technique": worst_compression.technique_used
            }
        }
    
    def benchmark_compression_techniques(self, sample_texts: List[str]) -> Dict[str, Dict[str, float]]:
        """Benchmark different compression techniques on sample texts"""
        techniques = ["whitespace_only", "remove_comments", "json_compression", 
                     "pattern_compression", "intelligent_summary", "comprehensive"]
        
        results = {}
        
        for technique in techniques:
            technique_results = []
            
            for text in sample_texts:
                result = self.optimize_context(text, technique)
                technique_results.append(result)
            
            if technique_results:
                avg_ratio = sum(r.compression_ratio for r in technique_results) / len(technique_results)
                avg_time = sum(r.compression_time_seconds for r in technique_results) / len(technique_results)
                total_tokens_saved = sum(r.tokens_saved for r in technique_results)
                
                results[technique] = {
                    "average_compression_ratio": avg_ratio,
                    "average_time_seconds": avg_time,
                    "total_tokens_saved": total_tokens_saved,
                    "samples_tested": len(technique_results)
                }
        
        return results
    
    def clear_history(self):
        """Clear compression history"""
        self.compression_history.clear()
        self.redundancy_cache.clear()
    
    def export_compression_report(self) -> Dict[str, Any]:
        """Export comprehensive compression performance report"""
        stats = self.get_compression_statistics()
        
        report = {
            "report_timestamp": datetime.now().isoformat(),
            "compression_statistics": stats,
            "methodology": {
                "token_estimation": "4 characters ≈ 1 token (weighted average with word count)",
                "whitespace_compression": "Replace multiple whitespace with single, trim lines",
                "comment_removal": "Remove Python/C/JS style comments",
                "pattern_compression": "Identify and compress repeated patterns (min 3 occurrences)",
                "json_compression": "Parse and reformat JSON compactly",
                "intelligent_summarization": "Score and select most important lines",
                "comprehensive": "Sequential application of all techniques"
            },
            "performance_notes": [
                "All measurements are based on actual text processing",
                "Token estimates are approximations - actual LLM token counts may vary",
                "Compression ratios reflect real character and estimated token reduction",
                "Processing times are measured for actual operations"
            ]
        }
        
        return report


# Global optimizer instance
context_optimizer = ContextWindowOptimizer()


# Convenience functions
def optimize_text(text: str, technique: str = "comprehensive", target_ratio: float = 0.7) -> Tuple[str, Dict[str, Any]]:
    """Convenience function to optimize text and return result with metrics"""
    result = context_optimizer.optimize_context(text, technique, target_ratio)
    compressed_text = context_optimizer._reconstruct_compressed_text(text, technique, target_ratio)
    return compressed_text, result.to_dict()


def adaptive_optimize(text: str, context_limit: int) -> Tuple[str, Dict[str, Any]]:
    """Convenience function for adaptive compression"""
    compressed_text, result = context_optimizer.adaptive_compression(text, context_limit)
    return compressed_text, result.to_dict()


def get_compression_stats() -> Dict[str, Any]:
    """Convenience function to get compression statistics"""
    return context_optimizer.get_compression_statistics()


def benchmark_techniques(sample_texts: List[str]) -> Dict[str, Dict[str, float]]:
    """Convenience function to benchmark compression techniques"""
    return context_optimizer.benchmark_compression_techniques(sample_texts)


def export_performance_report() -> Dict[str, Any]:
    """Convenience function to export performance report"""
    return context_optimizer.export_compression_report()