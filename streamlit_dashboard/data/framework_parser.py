"""
Framework Parser for .claude directory structure
Parses and analyzes the modular prompt framework components
"""

from pathlib import Path
import re
from typing import Dict, List, Optional, Any


# Sentinel value to distinguish between no argument and explicit None
_UNSET = object()

# Constants for directory and file structure
class FrameworkConstants:
    """Constants for framework structure"""
    COMMANDS_DIR = "commands"
    MODULES_DIR = "modules"
    FILE_EXTENSION = "*.md"
    DEFAULT_CATEGORY = "general"
    COMMAND_CATEGORY = "command"
    
    # Error messages
    ERROR_NOT_FOUND = "Framework directory not found"
    ERROR_NOT_DIR = "Framework path is not a directory"
    ERROR_NO_COMMANDS = "No commands found in framework"
    ERROR_NO_MODULES = "No modules found in framework"


class FrameworkParser:
    """Parser for .claude directory structure and framework components"""
    
    def __init__(self, framework_path=_UNSET):
        """Initialize the framework parser"""
        if framework_path is _UNSET:
            # Default to .claude directory in parent of parent directory
            self.framework_path = Path(__file__).parent.parent.parent / ".claude"
        elif framework_path is None:
            raise ValueError("framework_path cannot be None")
        else:
            if not isinstance(framework_path, Path):
                raise TypeError("framework_path must be a Path object")
            self.framework_path = framework_path
        
        self._parsed_data: Optional[Dict[str, Any]] = None
    
    def parse(self) -> Dict[str, Any]:
        """Parse the framework directory and return structured data"""
        if not self.framework_path.exists():
            return self._create_empty_result(is_valid=False, error=FrameworkConstants.ERROR_NOT_FOUND)
        
        if not self.framework_path.is_dir():
            return self._create_empty_result(is_valid=False, error=FrameworkConstants.ERROR_NOT_DIR)
        
        # Scan the directory structure
        scan_result = self._scan_directory()
        
        # Create structured result
        result = {
            'commands': scan_result.get('commands', []),
            'modules': scan_result.get('modules', []),
            'structure': scan_result.get('structure', {}),
            'metadata': {
                'framework_path': str(self.framework_path),
                'is_valid': True,
                'total_files': len(list(self.framework_path.glob('**/*.md'))),
                'parsed_at': self._get_current_timestamp()
            }
        }
        
        # Store parsed data for later access
        self._parsed_data = result
        return result
    
    def get_commands(self) -> List[Dict[str, Any]]:
        """Get list of parsed commands"""
        if self._parsed_data is None:
            raise RuntimeError("Must call parse() before accessing commands")
        return self._parsed_data['commands']
    
    def get_modules(self) -> List[Dict[str, Any]]:
        """Get list of parsed modules"""
        if self._parsed_data is None:
            raise RuntimeError("Must call parse() before accessing modules")
        return self._parsed_data['modules']
    
    def get_directory_structure(self) -> Dict[str, Any]:
        """Get directory structure information"""
        if self._parsed_data is None:
            raise RuntimeError("Must call parse() before accessing structure")
        return self._parsed_data['structure']
    
    def validate_framework(self) -> Dict[str, Any]:
        """Validate the parsed framework data"""
        if self._parsed_data is None:
            raise RuntimeError("Must call parse() before validation")
        
        errors = []
        warnings = []
        
        # Validate commands
        commands = self._parsed_data['commands']
        if len(commands) == 0:
            errors.append(FrameworkConstants.ERROR_NO_COMMANDS)
        
        # Validate modules
        modules = self._parsed_data['modules']
        if len(modules) == 0:
            errors.append(FrameworkConstants.ERROR_NO_MODULES)
        
        # Create validation result
        is_valid = len(errors) == 0
        
        # Get total files from metadata if available, otherwise calculate from structure
        total_files = 0
        if 'metadata' in self._parsed_data:
            total_files = self._parsed_data['metadata']['total_files']
        elif 'structure' in self._parsed_data:
            total_files = self._parsed_data['structure'].get('total_files', 0)
        
        return {
            'is_valid': is_valid,
            'errors': errors,
            'warnings': warnings,
            'statistics': {
                'commands_count': len(commands),
                'modules_count': len(modules),
                'total_files': total_files
            }
        }
    
    def _scan_directory(self) -> Dict[str, Any]:
        """Scan the .claude directory and extract components"""
        commands = []
        modules = []
        structure = {}
        
        # Scan commands directory
        commands_dir = self.framework_path / FrameworkConstants.COMMANDS_DIR
        if commands_dir.exists():
            for command_file in commands_dir.glob(FrameworkConstants.FILE_EXTENSION):
                commands.append(self._create_command_entry(command_file))
        
        # Scan modules directory
        modules_dir = self.framework_path / FrameworkConstants.MODULES_DIR
        if modules_dir.exists():
            for module_file in modules_dir.glob("**/" + FrameworkConstants.FILE_EXTENSION):
                modules.append(self._create_module_entry(module_file, modules_dir))
        
        # Build structure information
        structure = self._build_structure_info(commands, modules)
        
        return {
            'commands': commands,
            'modules': modules,
            'structure': structure
        }
    
    def _group_modules_by_category(self, modules: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Group modules by category"""
        categories = {}
        for module in modules:
            category = module['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(module)
        return categories
    
    def _build_structure_info(self, commands: List[Dict[str, Any]], modules: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Build structure information from commands and modules"""
        return {
            'commands': {
                'count': len(commands),
                'files': commands
            },
            'modules': {
                'count': len(modules),
                'categories': self._group_modules_by_category(modules)
            },
            'total_files': len(commands) + len(modules)
        }
    
    def _create_command_entry(self, command_file: Path) -> Dict[str, Any]:
        """Create a command entry from a file path with rich content parsing"""
        # Parse command file content for rich information
        command_data = self._parse_command_file(command_file)
        
        # Extract metadata fields for direct access
        metadata = command_data.get('metadata', {})
        
        command_entry = {
            'name': command_file.stem,
            'path': str(command_file),
            'category': command_data.get('category', FrameworkConstants.COMMAND_CATEGORY),
            'purpose': command_data.get('purpose', ''),
            'description': command_data.get('description', ''),
            'scope': command_data.get('scope', {}),
            'usage': command_data.get('usage', ''),
            'when_to_use': command_data.get('when_to_use', []),
            'examples': command_data.get('examples', []),
            'workflow': command_data.get('workflow', []),
            'metadata': metadata,
            'thinking_pattern': command_data.get('thinking_pattern', ''),
            'complexity_level': command_data.get('complexity_level', 'medium'),
            'delegation_targets': command_data.get('delegation_targets', []),
            # Expose metadata fields as direct attributes for UI access
            'version': metadata.get('version', 'unknown'),
            'last_updated': metadata.get('last_updated', 'unknown'),
            'status': metadata.get('status', 'unknown'),
            'readiness': metadata.get('readiness', 'unknown')
        }
        
        # Log warning for missing metadata
        if not metadata or metadata.get('version') == 'unknown':
            import warnings
            warnings.warn(f"Command file {command_file.name} is missing metadata table", UserWarning)
        
        return command_entry
    
    def _create_module_entry(self, module_file: Path, modules_dir: Path) -> Dict[str, Any]:
        """Create a module entry from a file path with deep parsing"""
        # Determine category from path
        parts = module_file.relative_to(modules_dir).parts
        category = parts[0] if len(parts) > 1 else FrameworkConstants.DEFAULT_CATEGORY
        
        # Parse module content for rich information
        module_data = self._parse_module_file(module_file)
        
        return {
            'name': module_file.stem,
            'path': str(module_file),
            'category': category,
            'purpose': module_data.get('purpose', ''),
            'description': module_data.get('description', ''),
            'interfaces': module_data.get('interfaces', {}),
            'dependencies': module_data.get('dependencies', []),
            'thinking_patterns': module_data.get('thinking_patterns', []),
            'usage_examples': module_data.get('usage_examples', []),
            'integration_points': module_data.get('integration_points', []),
            'performance_characteristics': module_data.get('performance_characteristics', {}),
            'complexity_metrics': module_data.get('complexity_metrics', {}),
            'enforcement_level': module_data.get('enforcement_level', 'advisory'),
            'validation_criteria': module_data.get('validation_criteria', []),
            'success_patterns': module_data.get('success_patterns', []),
            'common_failures': module_data.get('common_failures', [])
        }
    
    def _create_empty_result(self, is_valid: bool = True, error: str = None) -> Dict[str, Any]:
        """Create an empty result structure"""
        return {
            'commands': [],
            'modules': [],
            'structure': {
                'commands': {'count': 0, 'files': []},
                'modules': {'count': 0, 'categories': {}},
                'total_files': 0
            },
            'metadata': {
                'framework_path': str(self.framework_path),
                'is_valid': is_valid,
                'total_files': 0,
                'parsed_at': self._get_current_timestamp(),
                'error': error
            }
        }
    
    def _get_current_timestamp(self) -> str:
        """Get current timestamp for metadata"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def _parse_command_file(self, command_file: Path) -> Dict[str, Any]:
        """Parse command markdown file for rich content"""
        try:
            content = command_file.read_text(encoding='utf-8')
            
            # Extract command data from markdown content
            command_data = {}
            
            # Extract metadata table - more robust parsing
            metadata = {}
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if 'version' in line and 'last_updated' in line and 'status' in line:
                    # Found header line, data should be 2 lines down
                    if i + 2 < len(lines):
                        data_line = lines[i + 2]
                        parts = [p.strip() for p in data_line.split('|')]
                        if len(parts) >= 4:
                            metadata['version'] = parts[1] if len(parts) > 1 else 'unknown'
                            metadata['last_updated'] = parts[2] if len(parts) > 2 else 'unknown'
                            metadata['status'] = parts[3] if len(parts) > 3 else 'unknown'
                            metadata['readiness'] = parts[4] if len(parts) > 4 else 'unknown'
                        break
            
            command_data['metadata'] = metadata
            
            # Extract XML command definition
            xml_match = re.search(r'<command\s+name="([^"]*)"[^>]*>(.*?)</command>', content, re.DOTALL)
            if xml_match:
                command_name = xml_match.group(1)
                xml_content = xml_match.group(2)
                
                # Extract category from XML
                category_match = re.search(r'category="([^"]*)"', xml_match.group(0))
                if category_match:
                    command_data['category'] = category_match.group(1)
                
                # Extract purpose
                purpose_match = re.search(r'<purpose>(.*?)</purpose>', xml_content, re.DOTALL)
                if purpose_match:
                    command_data['purpose'] = purpose_match.group(1).strip()
                
                # Extract scope
                scope_match = re.search(r'<scope>(.*?)</scope>', xml_content, re.DOTALL)
                if scope_match:
                    scope_content = scope_match.group(1)
                    scope_data = {}
                    
                    includes_match = re.search(r'<includes>(.*?)</includes>', scope_content, re.DOTALL)
                    if includes_match:
                        scope_data['includes'] = includes_match.group(1).strip()
                    
                    excludes_match = re.search(r'<excludes>(.*?)</excludes>', scope_content, re.DOTALL)
                    if excludes_match:
                        scope_data['excludes'] = excludes_match.group(1).strip()
                    
                    boundaries_match = re.search(r'<boundaries>(.*?)</boundaries>', scope_content, re.DOTALL)
                    if boundaries_match:
                        scope_data['boundaries'] = boundaries_match.group(1).strip()
                    
                    command_data['scope'] = scope_data
            
            # Extract thinking pattern
            thinking_match = re.search(r'<thinking_pattern[^>]*>(.*?)</thinking_pattern>', content, re.DOTALL)
            if thinking_match:
                command_data['thinking_pattern'] = thinking_match.group(1).strip()
            
            # Extract description from title or first paragraph
            title_match = re.search(r'# ([^#\n]*)', content)
            if title_match:
                command_data['description'] = title_match.group(1).strip()
            
            # Determine complexity level based on content analysis
            complexity_indicators = {
                'simple': ['single', 'focused', 'one', 'basic'],
                'medium': ['multiple', 'moderate', 'standard'],
                'complex': ['comprehensive', 'system-wide', 'advanced', 'coordination']
            }
            
            content_lower = content.lower()
            complexity_scores = {}
            for level, indicators in complexity_indicators.items():
                complexity_scores[level] = sum(1 for indicator in indicators if indicator in content_lower)
            
            command_data['complexity_level'] = max(complexity_scores, key=complexity_scores.get)
            
            # Extract usage patterns and workflows
            if 'workflow' in content_lower or 'steps' in content_lower:
                workflow_steps = []
                # Look for numbered steps or workflow patterns
                step_matches = re.findall(r'(?:step|phase)\s*\d+[:\-\s]+([^\n]+)', content_lower)
                if step_matches:
                    workflow_steps = step_matches
                command_data['workflow'] = workflow_steps
            
            # Extract when to use guidance
            when_to_use = []
            if 'when to use' in content_lower:
                when_section = re.search(r'when to use[:\-\s]*([^#]*)', content_lower, re.DOTALL)
                if when_section:
                    when_content = when_section.group(1).strip()
                    when_to_use = [line.strip() for line in when_content.split('\n') if line.strip()]
            
            # Infer when to use from scope and purpose
            if not when_to_use and command_data.get('scope'):
                includes = command_data['scope'].get('includes', '')
                if includes:
                    when_to_use = [f"Use for: {includes}"]
            
            command_data['when_to_use'] = when_to_use
            
            # Extract examples
            examples = []
            example_matches = re.findall(r'(?:example|usage)[:\-\s]*([^\n]+)', content_lower)
            if example_matches:
                examples = example_matches
            command_data['examples'] = examples
            
            return command_data
            
        except Exception as e:
            # Return minimal data if parsing fails
            return {
                'description': f"Error parsing command file: {str(e)}",
                'category': FrameworkConstants.DEFAULT_CATEGORY,
                'complexity_level': 'medium',
                'metadata': {},
                'scope': {},
                'when_to_use': [],
                'examples': [],
                'workflow': []
            }
    
    def _parse_module_file(self, module_file: Path) -> Dict[str, Any]:
        """Parse module markdown file for rich content and metadata"""
        try:
            content = module_file.read_text(encoding='utf-8')
            
            # Extract module data from markdown content
            module_data = {}
            
            # Extract purpose/description
            purpose_match = re.search(r'(?:purpose|description)[:\-\s]*\n*([^\n#]*)', content, re.IGNORECASE)
            if purpose_match:
                module_data['purpose'] = purpose_match.group(1).strip()
            
            # Extract description from title or first paragraph
            title_match = re.search(r'# ([^#\n]*)', content)
            if title_match:
                module_data['description'] = title_match.group(1).strip()
            
            # Extract interfaces and contracts
            interfaces = {}
            interface_sections = re.findall(r'##?\s*interface[s]?\s*\n(.*?)(?=\n##|\n\n|$)', content, re.IGNORECASE | re.DOTALL)
            for section in interface_sections:
                # Parse interface definitions
                interfaces['input'] = self._extract_interface_spec(section, 'input')
                interfaces['output'] = self._extract_interface_spec(section, 'output')
                interfaces['dependencies'] = self._extract_interface_spec(section, 'dependencies')
            module_data['interfaces'] = interfaces
            
            # Extract dependencies
            dependencies = []
            dep_patterns = [
                r'(?:depends on|requires|uses)[:\-\s]*([^\n]*)',
                r'@import[:\-\s]*([^\n]*)',
                r'delegate[s]?\s+to[:\-\s]*([^\n]*)'
            ]
            for pattern in dep_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                dependencies.extend([dep.strip() for dep in matches if dep.strip()])
            module_data['dependencies'] = list(set(dependencies))
            
            # Extract thinking patterns
            thinking_patterns = []
            thinking_sections = re.findall(r'thinking[_\s]*pattern[s]?[:\-\s]*\n(.*?)(?=\n##|\n\n|$)', content, re.IGNORECASE | re.DOTALL)
            for section in thinking_sections:
                patterns = re.findall(r'[→\-\*]\s*([^\n]*)', section)
                thinking_patterns.extend([p.strip() for p in patterns if p.strip()])
            module_data['thinking_patterns'] = thinking_patterns
            
            # Extract usage examples
            usage_examples = []
            example_sections = re.findall(r'(?:example|usage)[s]?[:\-\s]*\n(.*?)(?=\n##|\n\n|$)', content, re.IGNORECASE | re.DOTALL)
            for section in example_sections:
                examples = re.findall(r'(?:```[^\n]*\n(.*?)\n```|`([^`]*)`)', section, re.DOTALL)
                for ex in examples:
                    example_text = ex[0] if ex[0] else ex[1]
                    if example_text.strip():
                        usage_examples.append(example_text.strip())
            module_data['usage_examples'] = usage_examples
            
            # Extract integration points
            integration_points = []
            integration_sections = re.findall(r'integrat[es|ion]*[:\-\s]*\n(.*?)(?=\n##|\n\n|$)', content, re.IGNORECASE | re.DOTALL)
            for section in integration_sections:
                points = re.findall(r'[→\-\*]\s*([^\n]*)', section)
                integration_points.extend([p.strip() for p in points if p.strip()])
            module_data['integration_points'] = integration_points
            
            # Extract performance characteristics
            performance_characteristics = {}
            perf_sections = re.findall(r'performance[:\-\s]*\n(.*?)(?=\n##|\n\n|$)', content, re.IGNORECASE | re.DOTALL)
            for section in perf_sections:
                # Extract time complexity
                time_match = re.search(r'time[:\-\s]*([^\n]*)', section, re.IGNORECASE)
                if time_match:
                    performance_characteristics['time_complexity'] = time_match.group(1).strip()
                
                # Extract space complexity
                space_match = re.search(r'space[:\-\s]*([^\n]*)', section, re.IGNORECASE)
                if space_match:
                    performance_characteristics['space_complexity'] = space_match.group(1).strip()
                
                # Extract optimization notes
                opt_matches = re.findall(r'optim[a-z]*[:\-\s]*([^\n]*)', section, re.IGNORECASE)
                if opt_matches:
                    performance_characteristics['optimizations'] = opt_matches
            module_data['performance_characteristics'] = performance_characteristics
            
            # Extract complexity metrics
            complexity_metrics = {}
            complexity_indicators = {
                'cognitive_load': ['cognitive', 'mental', 'complexity', 'difficult'],
                'integration_complexity': ['integration', 'coupling', 'dependency'],
                'maintenance_burden': ['maintenance', 'update', 'change', 'modify']
            }
            
            content_lower = content.lower()
            for metric, indicators in complexity_indicators.items():
                score = sum(1 for indicator in indicators if indicator in content_lower)
                complexity_metrics[metric] = min(score, 5)  # Cap at 5
            module_data['complexity_metrics'] = complexity_metrics
            
            # Extract enforcement level
            enforcement_level = 'advisory'
            enforcement_patterns = [
                r'enforcement[:\-\s]*(mandatory|critical|blocking|advisory|warning)',
                r'(mandatory|critical|blocking|advisory|warning)[:\-\s]*enforcement'
            ]
            for pattern in enforcement_patterns:
                match = re.search(pattern, content, re.IGNORECASE)
                if match:
                    enforcement_level = match.group(1).lower()
                    break
            module_data['enforcement_level'] = enforcement_level
            
            # Extract validation criteria
            validation_criteria = []
            validation_sections = re.findall(r'validat[ion|e]*[:\-\s]*\n(.*?)(?=\n##|\n\n|$)', content, re.IGNORECASE | re.DOTALL)
            for section in validation_sections:
                criteria = re.findall(r'[→\-\*]\s*([^\n]*)', section)
                validation_criteria.extend([c.strip() for c in criteria if c.strip()])
            module_data['validation_criteria'] = validation_criteria
            
            # Extract success patterns
            success_patterns = []
            success_sections = re.findall(r'success[:\-\s]*\n(.*?)(?=\n##|\n\n|$)', content, re.IGNORECASE | re.DOTALL)
            for section in success_sections:
                patterns = re.findall(r'[→\-\*]\s*([^\n]*)', section)
                success_patterns.extend([p.strip() for p in patterns if p.strip()])
            module_data['success_patterns'] = success_patterns
            
            # Extract common failures
            common_failures = []
            failure_sections = re.findall(r'(?:failure|error|problem|issue)[s]?[:\-\s]*\n(.*?)(?=\n##|\n\n|$)', content, re.IGNORECASE | re.DOTALL)
            for section in failure_sections:
                failures = re.findall(r'[→\-\*]\s*([^\n]*)', section)
                common_failures.extend([f.strip() for f in failures if f.strip()])
            module_data['common_failures'] = common_failures
            
            return module_data
            
        except Exception as e:
            # Return minimal data if parsing fails
            return {
                'description': f"Error parsing module file: {str(e)}",
                'purpose': '',
                'interfaces': {},
                'dependencies': [],
                'thinking_patterns': [],
                'usage_examples': [],
                'integration_points': [],
                'performance_characteristics': {},
                'complexity_metrics': {},
                'enforcement_level': 'advisory',
                'validation_criteria': [],
                'success_patterns': [],
                'common_failures': []
            }
    
    def _extract_interface_spec(self, content: str, spec_type: str) -> List[str]:
        """Extract interface specifications from content"""
        pattern = rf'{spec_type}[:\-\s]*\n(.*?)(?=\n\n|{spec_type}|\n[a-z]+:|$)'
        matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
        
        specs = []
        for match in matches:
            # Extract list items
            items = re.findall(r'[→\-\*]\s*([^\n]*)', match)
            specs.extend([item.strip() for item in items if item.strip()])
        
        return specs