# /cost analyze Command

Purpose: Analyze and optimize costs with 40-98% reduction potential

## Usage
```
/cost analyze [scope] [--breakdown] [--optimize] [--forecast]
```

## Examples
- `/cost analyze` - Overall cost analysis
- `/cost analyze api/ --breakdown` - Detailed API cost breakdown
- `/cost analyze --optimize` - Get optimization suggestions
- `/cost analyze --forecast 6m` - 6-month cost projection

## Process

Leveraging R18 Cost Optimization Research:
1. Identify cost drivers:
   - API calls and token usage
   - Database queries
   - Storage usage
   - Compute resources
   - Third-party services
2. Analyze usage patterns:
   - Peak usage times
   - Inefficient operations
   - Redundant processes
   - Caching opportunities
3. Calculate current costs:
   - Per operation
   - Per user/feature
   - Growth projections
4. Generate optimization plan:
   - Quick wins (immediate)
   - Strategic changes (1-3 months)
   - Architecture evolution (3-6 months)

## Cost Categories
- **API/Token Usage**: LLM API calls, token consumption
- **Infrastructure**: Compute, storage, bandwidth
- **Database**: Queries, storage, backups
- **Services**: Third-party APIs, SaaS tools
- **Development**: Time costs, inefficiencies

## Output Format
```
COST ANALYSIS REPORT
━━━━━━━━━━━━━━━━━━━
Current Monthly Cost: $4,850

BREAKDOWN:
━━━━━━━━━━━━━━━━━━━
API Calls:      $2,100 (43%)
├─ LLM APIs:    $1,800
├─ Search APIs: $200
└─ Other:       $100

Infrastructure: $1,850 (38%)
├─ Compute:     $1,200
├─ Storage:     $400
└─ Bandwidth:   $250

Database:       $900 (19%)

OPTIMIZATION OPPORTUNITIES:
━━━━━━━━━━━━━━━━━━━━━━━━━
1. Implement caching (Save: $840/mo)
   - Cache API responses
   - 40% reduction possible

2. Optimize queries (Save: $450/mo)
   - Add indexes
   - Batch operations
   
3. Use spot instances (Save: $360/mo)
   - 30% compute savings

TOTAL SAVINGS: $1,650/mo (34%)
━━━━━━━━━━━━━━━━━━━━━━━━━
Optimized Cost: $3,200/mo
Annual Savings: $19,800
```

## Options
- `--breakdown`: Detailed cost breakdown
- `--optimize`: Generate optimization plan
- `--forecast`: Cost projections
- `--compare`: Compare periods

## Related Commands
- `/cost optimize` - Apply optimizations
- `/perf optimize` - Performance tuning
- `/monitor costs` - Cost monitoring