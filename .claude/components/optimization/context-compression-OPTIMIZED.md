# Context Compression

**Purpose**: Intelligent context compression using semantic analysis and hierarchical summarization to reduce token usage while preserving critical information.

**Usage**: 
- Analyze content importance using semantic relevance scoring
- Apply hierarchical summarization techniques to compress lengthy content
- Preserve critical information while reducing token overhead
- Use adaptive compression based on task requirements and context window
- Maintain quality through intelligent content prioritization

**Compatibility**: 
- **Works with**: prompt-optimization, search-ranking, intelligent-summarization
- **Requires**: Large context content requiring compression
- **Conflicts**: None (universal optimization utility)

**Implementation**:
```python
# Intelligent context compression
def compress_context(content, target_reduction=0.5, task_context=None):
    # 1. Semantic Analysis and Priority Scoring
    segments = segment_content(content)
    scores = []
    
    for segment in segments:
        score = calculate_importance_score(segment, task_context)
        scores.append((segment, score))
    
    # 2. Sort by importance and apply compression
    ranked_segments = sorted(scores, key=lambda x: x[1], reverse=True)
    compressed_content = []
    current_tokens = 0
    target_tokens = int(count_tokens(content) * (1 - target_reduction))
    
    # 3. Hierarchical summarization for high-priority content
    for segment, score in ranked_segments:
        segment_tokens = count_tokens(segment)
        
        if current_tokens + segment_tokens <= target_tokens:
            compressed_content.append(segment)
            current_tokens += segment_tokens
        elif score > 80:  # High-priority content gets summarized, not dropped
            summary = hierarchical_summarize(segment, target_length=segment_tokens // 3)
            compressed_content.append(summary)
            current_tokens += count_tokens(summary)
    
    return CompressionResult(
        compressed_content='\n'.join(compressed_content),
        original_tokens=count_tokens(content),
        compressed_tokens=current_tokens,
        compression_ratio=current_tokens / count_tokens(content)
    )

# Importance scoring algorithm
def calculate_importance_score(segment, task_context):
    task_relevance = measure_task_relevance(segment, task_context) * 0.4
    usage_frequency = measure_usage_frequency(segment) * 0.25
    recency = measure_recency(segment) * 0.2
    cross_references = count_cross_references(segment) * 0.1
    user_markers = detect_user_importance_markers(segment) * 0.05
    
    return task_relevance + usage_frequency + recency + cross_references + user_markers
```

**Category**: optimization | **Complexity**: high | **Time**: 4 hours