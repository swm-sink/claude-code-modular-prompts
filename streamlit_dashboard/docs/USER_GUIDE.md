# Claude Code Modular Prompts Dashboard - User Guide

## Overview

The Claude Code Modular Prompts Dashboard is a comprehensive web application built with Streamlit that provides an interactive interface for managing, visualizing, and working with the Claude Code modular prompts framework. This guide will help you understand and effectively use all the features available in the dashboard.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Dashboard Overview](#dashboard-overview)
3. [Core Components](#core-components)
4. [Framework Explorer](#framework-explorer)
5. [Template Manager](#template-manager)
6. [URL Sharing](#url-sharing)
7. [Performance Monitoring](#performance-monitoring)
8. [Advanced Features](#advanced-features)
9. [Troubleshooting](#troubleshooting)
10. [Best Practices](#best-practices)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit 1.28.0 or higher
- All dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/swm-sink/claude-code-modular-prompts.git
   cd claude-code-modular-prompts/streamlit_dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the dashboard:
   ```bash
   streamlit run app.py
   ```

4. Open your browser to `http://localhost:8501`

## Dashboard Overview

The dashboard is organized into several main sections accessible through the sidebar navigation:

### Main Navigation

- **🏠 Home**: Overview and quick access to key features
- **🔍 Framework Explorer**: Browse and explore framework components
- **📄 Template Manager**: Manage and organize templates
- **🔗 URL Sharing**: Share templates securely via URLs
- **📊 Performance Monitor**: Monitor application performance and usage

### Key Features

- **Interactive Visualization**: Real-time visual representations of framework components
- **Template Management**: Create, edit, and organize prompt templates
- **Secure Sharing**: Share templates with controlled access and expiration
- **Performance Tracking**: Monitor application usage and performance metrics
- **Responsive Design**: Works on desktop and mobile devices

## Core Components

### 1. Framework Explorer

The Framework Explorer provides a comprehensive view of the Claude Code modular prompts framework structure.

#### Features:
- **Interactive Directory Tree**: Navigate through framework components
- **Component Details**: View detailed information about each component
- **Dependency Visualization**: See relationships between components
- **Search and Filter**: Find specific components quickly

#### Usage:
1. Navigate to the Framework Explorer section
2. Use the directory tree to browse components
3. Click on any component to view its details
4. Use the search bar to find specific components
5. View dependency graphs to understand component relationships

### 2. Visual Flow Builder

Build and visualize prompt workflows using a drag-and-drop interface.

#### Features:
- **Node-based Interface**: Drag and drop components to build workflows
- **Real-time Preview**: See your workflow as you build it
- **Connection Management**: Link components with visual connections
- **Export Options**: Save workflows in various formats

#### Usage:
1. Access the Visual Flow Builder from the main dashboard
2. Drag components from the palette onto the canvas
3. Connect components by dragging from output to input ports
4. Configure component properties in the properties panel
5. Preview and test your workflow
6. Export your completed workflow

### 3. Template Gallery

Browse and manage a collection of pre-built templates.

#### Features:
- **Template Browser**: Browse templates by category
- **Preview and Details**: View template information before use
- **Import/Export**: Share templates with others
- **Version Control**: Track template versions and changes

#### Usage:
1. Navigate to the Template Gallery
2. Browse templates by category or use search
3. Click on a template to view details and preview
4. Use the import/export functions to manage templates
5. Clone templates to create customized versions

## Framework Explorer

### Navigation

The Framework Explorer uses a hierarchical tree structure to represent the framework components:

```
📁 .claude/
├── 📁 commands/
├── 📁 modules/
├── 📁 system/
├── 📁 prompt_eng/
└── 📁 templates/
```

### Component Types

1. **Commands**: High-level workflow orchestrators
2. **Modules**: Reusable functional components
3. **System**: Infrastructure and quality components
4. **Prompt Engineering**: Advanced prompt patterns
5. **Templates**: Pre-configured setups

### Viewing Component Details

Click on any component to view:
- **Content**: Full component content
- **Metadata**: Version, author, dependencies
- **Usage**: How to use the component
- **Examples**: Practical usage examples

## Template Manager

### Creating Templates

1. Navigate to the Template Manager
2. Click "Create New Template"
3. Fill in template details:
   - Name and description
   - Category classification
   - Component selection
   - Metadata configuration
4. Save and validate the template

### Managing Templates

- **Edit**: Modify existing templates
- **Delete**: Remove unused templates
- **Duplicate**: Create copies for customization
- **Export**: Share templates with others
- **Import**: Load templates from files

### Template Structure

Templates follow a standardized format:

```json
{
  "id": "unique_template_id",
  "name": "Template Name",
  "description": "Template description",
  "category": "development",
  "author": "Author Name",
  "version": "1.0.0",
  "components": [
    {
      "type": "command",
      "name": "task",
      "file": "commands/task.md"
    }
  ],
  "metadata": {
    "framework_version": "3.0.0",
    "tags": ["development", "automation"],
    "difficulty": "intermediate"
  }
}
```

## URL Sharing

### Sharing Templates

1. Navigate to the URL Sharing section
2. Select a template to share
3. Configure sharing options:
   - **Expiration**: Set when the link expires
   - **Access Limit**: Maximum number of accesses
   - **Permissions**: Control what recipients can do
4. Generate the sharing URL
5. Copy and share the URL with others

### Accessing Shared Templates

1. Click on a shared URL
2. View the template details
3. Import the template if desired
4. Use the template in your workflows

### Security Features

- **Secure Tokens**: Cryptographically secure sharing tokens
- **Access Control**: Limit who can access shared templates
- **Expiration**: Automatic link expiration
- **Audit Trail**: Track access and usage
- **Revocation**: Revoke access at any time

## Performance Monitoring

### Real-time Metrics

The Performance Monitor provides real-time insights into:

- **Memory Usage**: Current and historical memory consumption
- **CPU Usage**: Processor utilization patterns
- **Response Times**: Application performance metrics
- **Error Rates**: Error frequency and types
- **Session Data**: User session information

### Monitoring Dashboard

The monitoring dashboard displays:

1. **System Metrics**: CPU, memory, and performance data
2. **Application Metrics**: Response times and throughput
3. **Error Tracking**: Error logs and frequencies
4. **Usage Statistics**: User activity and feature usage

### Performance Optimization

Use the monitoring data to:
- Identify performance bottlenecks
- Optimize resource usage
- Improve user experience
- Plan capacity requirements

## Advanced Features

### Custom Components

Create custom components by:
1. Defining component structure
2. Implementing component logic
3. Adding to the framework
4. Testing and validation

### API Integration

The dashboard provides REST API endpoints for:
- Template management
- Component access
- Performance data
- Sharing functionality

### Batch Operations

Perform bulk operations on:
- Multiple templates
- Component updates
- Data exports
- System maintenance

## Troubleshooting

### Common Issues

1. **Dashboard Won't Load**
   - Check Python version (3.8+)
   - Verify all dependencies are installed
   - Ensure port 8501 is available

2. **Components Not Displaying**
   - Verify framework files are present
   - Check file permissions
   - Validate JSON syntax

3. **Performance Issues**
   - Monitor system resources
   - Check for memory leaks
   - Optimize component usage

4. **Sharing Not Working**
   - Verify network connectivity
   - Check sharing permissions
   - Validate token expiration

### Debug Mode

Enable debug mode for detailed logging:
```bash
streamlit run app.py --logger.level=debug
```

### Support Resources

- **Documentation**: Check the API documentation
- **Community**: Join the discussion forums
- **Issues**: Report bugs on GitHub
- **Examples**: Browse the examples repository

## Best Practices

### Template Organization

1. **Use Descriptive Names**: Clear, descriptive template names
2. **Categorize Properly**: Organize templates by logical categories
3. **Document Dependencies**: List all component dependencies
4. **Version Control**: Track template versions and changes
5. **Test Thoroughly**: Validate templates before sharing

### Performance Optimization

1. **Monitor Resource Usage**: Keep track of memory and CPU usage
2. **Optimize Components**: Remove unused components
3. **Cache Frequently Used Data**: Use caching for improved performance
4. **Regular Maintenance**: Clean up old data and expired shares

### Security Considerations

1. **Secure Sharing**: Use secure tokens and access controls
2. **Regular Audits**: Monitor sharing activity and access logs
3. **Expire Unused Links**: Set appropriate expiration times
4. **Protect Sensitive Data**: Avoid sharing sensitive information

### Collaboration Guidelines

1. **Clear Documentation**: Document templates and workflows
2. **Version Management**: Use semantic versioning for templates
3. **Code Reviews**: Review templates before sharing
4. **Testing Standards**: Maintain consistent testing practices

## Support and Resources

### Getting Help

- **User Manual**: This comprehensive guide
- **API Documentation**: Technical API reference
- **Video Tutorials**: Step-by-step video guides
- **Community Forums**: Connect with other users
- **GitHub Issues**: Report bugs and request features

### Contributing

To contribute to the project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
5. Follow the contribution guidelines

### License

This project is licensed under the MIT License. See the LICENSE file for details.

---

*Last Updated: 2025-07-18*
*Version: 1.0.0*