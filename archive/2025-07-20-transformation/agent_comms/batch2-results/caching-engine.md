# Caching Engine Specifications

## 🎯 Overview

The caching engine is the cornerstone of our 90% cost reduction strategy, implementing a sophisticated multi-tier cache that dramatically reduces token usage while maintaining sub-5-second response times.

## 🏗️ Architecture

### Multi-Tier Cache Hierarchy

```
┌─────────────────────────────────────────────────────────┐
│                    L1: Prompt Cache                      │
│              (Hot - 95% hit rate target)                 │
│    Size: 10MB | TTL: 24h | Access: <1ms                │
├─────────────────────────────────────────────────────────┤
│                   L2: Module Cache                       │
│             (Warm - 90% hit rate target)                 │
│    Size: 50MB | TTL: 12h | Access: <5ms                │
├─────────────────────────────────────────────────────────┤
│                  L3: Context Cache                       │
│             (Cool - 85% hit rate target)                 │
│   Size: 100MB | TTL: 6h | Access: <10ms                │
├─────────────────────────────────────────────────────────┤
│                  L4: Results Cache                       │
│             (Cold - 70% hit rate target)                 │
│   Size: 200MB | TTL: 1h | Access: <20ms                │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Implementation Details

### Cache Key Strategy

```python
class CacheKeyGenerator:
    """Deterministic cache key generation for maximum hit rates"""
    
    def __init__(self):
        self.version = "3.0.0"
        self.salt = "claude-modular-2025"
    
    def generate_prompt_key(self, command: str, params: dict) -> str:
        """L1 cache key for prompt templates"""
        normalized = self._normalize_params(params)
        components = [
            "prompt",
            self.version,
            command,
            hashlib.md5(json.dumps(normalized).encode()).hexdigest()[:8]
        ]
        return ":".join(components)
    
    def generate_module_key(self, module: str, context_hash: str) -> str:
        """L2 cache key for module responses"""
        components = [
            "module",
            self.version,
            module.replace("/", "_"),
            context_hash[:8]
        ]
        return ":".join(components)
    
    def generate_context_key(self, project_path: str, command: str) -> str:
        """L3 cache key for context snapshots"""
        project_hash = hashlib.md5(project_path.encode()).hexdigest()[:8]
        components = [
            "context",
            self.version,
            project_hash,
            command
        ]
        return ":".join(components)
    
    def generate_result_key(self, command: str, input_hash: str) -> str:
        """L4 cache key for execution results"""
        components = [
            "result",
            self.version,
            command,
            input_hash[:16]
        ]
        return ":".join(components)
    
    def _normalize_params(self, params: dict) -> dict:
        """Normalize parameters for consistent hashing"""
        return {k: v for k, v in sorted(params.items()) if v is not None}
```

### Cache Storage Backend

```python
class CacheStorage:
    """High-performance cache storage with compression"""
    
    def __init__(self, config: dict):
        self.redis = redis.Redis(
            host=config.get('host', 'localhost'),
            port=config.get('port', 6379),
            db=config.get('db', 0),
            decode_responses=False  # Handle binary data
        )
        self.compressor = lz4.frame.compress
        self.decompressor = lz4.frame.decompress
        self.serializer = msgpack.packb
        self.deserializer = msgpack.unpackb
    
    async def get(self, key: str) -> Optional[Any]:
        """Retrieve and decompress cached value"""
        try:
            compressed = await self.redis.get(key)
            if compressed:
                decompressed = self.decompressor(compressed)
                return self.deserializer(decompressed, raw=False)
            return None
        except Exception as e:
            logger.warning(f"Cache get failed for {key}: {e}")
            return None
    
    async def set(self, key: str, value: Any, ttl: int):
        """Compress and store value with TTL"""
        try:
            serialized = self.serializer(value)
            compressed = self.compressor(serialized)
            compression_ratio = len(compressed) / len(serialized)
            
            # Only cache if compression is beneficial
            if compression_ratio < 0.9:
                await self.redis.setex(key, ttl, compressed)
                logger.debug(f"Cached {key}, compression: {compression_ratio:.2%}")
            else:
                await self.redis.setex(key, ttl, serialized)
                logger.debug(f"Cached {key} uncompressed")
                
        except Exception as e:
            logger.error(f"Cache set failed for {key}: {e}")
    
    async def invalidate_pattern(self, pattern: str):
        """Invalidate all keys matching pattern"""
        cursor = 0
        while True:
            cursor, keys = await self.redis.scan(
                cursor, match=pattern, count=100
            )
            if keys:
                await self.redis.delete(*keys)
            if cursor == 0:
                break
```

### Intelligent Cache Manager

```python
class CacheManager:
    """Intelligent cache orchestration with hit rate optimization"""
    
    def __init__(self):
        self.storage = CacheStorage(CACHE_CONFIG)
        self.key_gen = CacheKeyGenerator()
        self.stats = CacheStatistics()
        self.optimizer = CacheOptimizer()
    
    async def get_or_compute(
        self, 
        cache_level: str,
        key_components: dict,
        compute_func: Callable,
        ttl: Optional[int] = None
    ) -> Tuple[Any, bool]:
        """Get from cache or compute with automatic optimization"""
        
        # Generate appropriate cache key
        key = self._generate_key(cache_level, key_components)
        
        # Try cache first
        cached_value = await self.storage.get(key)
        if cached_value is not None:
            self.stats.record_hit(cache_level, key)
            return cached_value, True
        
        # Cache miss - compute value
        self.stats.record_miss(cache_level, key)
        computed_value = await compute_func()
        
        # Store in cache with appropriate TTL
        cache_ttl = ttl or self._get_ttl_for_level(cache_level)
        await self.storage.set(key, computed_value, cache_ttl)
        
        # Optimize cache if needed
        if self.stats.should_optimize(cache_level):
            await self.optimizer.optimize_level(cache_level, self.stats)
        
        return computed_value, False
    
    def _generate_key(self, level: str, components: dict) -> str:
        """Generate cache key based on level"""
        if level == "L1":
            return self.key_gen.generate_prompt_key(
                components['command'], 
                components['params']
            )
        elif level == "L2":
            return self.key_gen.generate_module_key(
                components['module'],
                components['context_hash']
            )
        elif level == "L3":
            return self.key_gen.generate_context_key(
                components['project_path'],
                components['command']
            )
        elif level == "L4":
            return self.key_gen.generate_result_key(
                components['command'],
                components['input_hash']
            )
    
    def _get_ttl_for_level(self, level: str) -> int:
        """Get TTL in seconds for cache level"""
        ttls = {
            "L1": 86400,  # 24 hours
            "L2": 43200,  # 12 hours  
            "L3": 21600,  # 6 hours
            "L4": 3600,   # 1 hour
        }
        return ttls.get(level, 3600)
```

### Cache Statistics & Monitoring

```python
class CacheStatistics:
    """Real-time cache performance monitoring"""
    
    def __init__(self):
        self.hits = defaultdict(int)
        self.misses = defaultdict(int)
        self.last_optimization = defaultdict(lambda: time.time())
        self.optimization_threshold = 300  # 5 minutes
    
    def record_hit(self, level: str, key: str):
        """Record cache hit"""
        self.hits[level] += 1
        self._update_metrics(level, hit=True)
    
    def record_miss(self, level: str, key: str):
        """Record cache miss"""
        self.misses[level] += 1
        self._update_metrics(level, hit=False)
    
    def get_hit_rate(self, level: str) -> float:
        """Calculate hit rate for cache level"""
        total = self.hits[level] + self.misses[level]
        if total == 0:
            return 0.0
        return self.hits[level] / total
    
    def should_optimize(self, level: str) -> bool:
        """Determine if cache level needs optimization"""
        # Check if enough time has passed
        if time.time() - self.last_optimization[level] < self.optimization_threshold:
            return False
        
        # Check if hit rate is below target
        hit_rate = self.get_hit_rate(level)
        targets = {"L1": 0.95, "L2": 0.90, "L3": 0.85, "L4": 0.70}
        
        return hit_rate < targets.get(level, 0.80)
    
    def _update_metrics(self, level: str, hit: bool):
        """Update prometheus metrics"""
        if hit:
            cache_hits.labels(level=level).inc()
        else:
            cache_misses.labels(level=level).inc()
        
        # Update hit rate gauge
        hit_rate = self.get_hit_rate(level)
        cache_hit_rate.labels(level=level).set(hit_rate)
```

### Cache Optimization Engine

```python
class CacheOptimizer:
    """Automatic cache optimization based on usage patterns"""
    
    async def optimize_level(self, level: str, stats: CacheStatistics):
        """Optimize cache level based on statistics"""
        hit_rate = stats.get_hit_rate(level)
        
        if level == "L1" and hit_rate < 0.95:
            await self._optimize_prompt_cache(stats)
        elif level == "L2" and hit_rate < 0.90:
            await self._optimize_module_cache(stats)
        elif level == "L3" and hit_rate < 0.85:
            await self._optimize_context_cache(stats)
        elif level == "L4" and hit_rate < 0.70:
            await self._optimize_result_cache(stats)
    
    async def _optimize_prompt_cache(self, stats):
        """Optimize L1 prompt cache"""
        # Analyze miss patterns
        miss_patterns = await self._analyze_miss_patterns("L1")
        
        # Pre-warm frequently missed prompts
        for pattern in miss_patterns[:10]:
            await self._prewarm_prompt(pattern)
        
        # Adjust TTL based on usage
        if stats.get_hit_rate("L1") < 0.90:
            # Increase TTL for better retention
            await self._adjust_ttl("L1", multiplier=1.5)
    
    async def _optimize_module_cache(self, stats):
        """Optimize L2 module cache"""
        # Identify hot modules
        hot_modules = await self._identify_hot_modules()
        
        # Pin hot modules in cache
        for module in hot_modules:
            await self._pin_in_cache("L2", module)
        
        # Compress large modules more aggressively
        await self._optimize_compression("L2")
    
    async def _prewarm_prompt(self, pattern: dict):
        """Pre-warm a prompt template"""
        # Generate common variations
        variations = self._generate_prompt_variations(pattern)
        
        for variation in variations:
            key = self.key_gen.generate_prompt_key(
                variation['command'],
                variation['params']
            )
            # Compute and cache
            await self.cache_manager.get_or_compute(
                "L1", variation, 
                lambda: self._compute_prompt(variation)
            )
```

## 🎯 Performance Targets

### Hit Rate Goals
- **L1 Prompt Cache**: 95% (achieved through pre-warming)
- **L2 Module Cache**: 90% (achieved through pinning)
- **L3 Context Cache**: 85% (achieved through smart invalidation)
- **L4 Results Cache**: 70% (achieved through pattern matching)

### Response Time Targets
- **Cache Hit**: <5ms for any level
- **Cache Miss + Compute**: <5s for any operation
- **Cache Optimization**: <100ms overhead

### Cost Reduction
- **Token Savings**: 90% for cached operations
- **Monthly Savings**: $259 (60% of baseline)
- **ROI**: 240% in first year

## 🔧 Configuration

### Redis Configuration
```yaml
redis:
  host: localhost
  port: 6379
  db: 0
  max_connections: 100
  socket_keepalive: true
  socket_keepalive_options:
    TCP_KEEPIDLE: 120
    TCP_KEEPINTVL: 30
    TCP_KEEPCNT: 3
```

### Cache Policies
```yaml
eviction_policies:
  L1: allkeys-lru  # Evict least recently used
  L2: volatile-lru # Evict LRU among keys with TTL
  L3: volatile-ttl # Evict keys with shortest TTL
  L4: allkeys-lfu  # Evict least frequently used

memory_limits:
  L1: 10mb
  L2: 50mb
  L3: 100mb
  L4: 200mb
  total: 360mb
```

## 🚀 Usage Examples

### Basic Caching
```python
# Cache a prompt template
result, cached = await cache_manager.get_or_compute(
    "L1",
    {"command": "task", "params": {"file": "app.py"}},
    compute_func=lambda: generate_task_prompt(params)
)

# Cache a module response
module_result, cached = await cache_manager.get_or_compute(
    "L2", 
    {"module": "tdd-cycle", "context_hash": ctx_hash},
    compute_func=lambda: load_module("tdd-cycle", context)
)
```

### Advanced Patterns
```python
# Batch cache operations
async with cache_manager.batch() as batch:
    batch.get("L1", key1)
    batch.get("L2", key2)
    batch.get("L3", key3)
    results = await batch.execute()  # Parallel execution

# Cache with custom TTL
await cache_manager.get_or_compute(
    "L3",
    components,
    compute_func,
    ttl=7200  # 2 hours instead of default
)

# Force cache refresh
await cache_manager.invalidate_pattern("L1:prompt:3.0.0:task:*")
```

## 📊 Monitoring Dashboard

```python
# Prometheus metrics exposed
cache_hits = Counter('claude_cache_hits_total', 'Cache hits', ['level'])
cache_misses = Counter('claude_cache_misses_total', 'Cache misses', ['level'])
cache_hit_rate = Gauge('claude_cache_hit_rate', 'Cache hit rate', ['level'])
cache_size = Gauge('claude_cache_size_bytes', 'Cache size', ['level'])
cache_evictions = Counter('claude_cache_evictions_total', 'Cache evictions', ['level'])
```

## 🎯 Success Metrics

The caching engine will be considered successful when:
- ✅ 90%+ overall cache hit rate achieved
- ✅ Sub-5ms cache access times maintained
- ✅ 60% token reduction demonstrated
- ✅ $259/month cost savings realized
- ✅ Zero functionality degradation
- ✅ Automatic optimization keeps hit rates high

---
*Caching Engine Specifications v1.0 | Agent 8 | 2025-07-19*