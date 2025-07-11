# /docs - Documentation Generation

**Version**: 1.0.0 | **Status**: Basic | **Last Updated**: 2025-07-09

---

## Purpose

Create, update, and manage comprehensive documentation for projects, APIs, and systems. Ideal for generating user guides, API documentation, technical specifications, and knowledge base articles.

**Note**: This is a simplified version that focuses on core documentation functionality without complex FOCUS framework enforcement.

---

## How It Works

### 1. Documentation Planning
- **Content Strategy**: Define documentation goals and audience
- **Structure Planning**: Plan document organization and hierarchy
- **Content Inventory**: Identify existing content and gaps
- **Style Guidelines**: Establish documentation standards and style

### 2. Content Creation
- **Document Generation**: Create new documentation content
- **Content Organization**: Structure content logically and clearly
- **Visual Elements**: Add diagrams, examples, and illustrations
- **Cross-References**: Link related content and resources

### 3. Quality Assurance
- **Content Review**: Review for accuracy and completeness
- **Style Consistency**: Ensure consistent formatting and style
- **Accessibility**: Ensure documentation is accessible to all users
- **Validation**: Verify technical accuracy and usability

### 4. Maintenance & Updates
- **Version Control**: Track documentation changes and versions
- **Regular Updates**: Keep documentation current and relevant
- **User Feedback**: Incorporate user feedback and improvements
- **Knowledge Management**: Organize and preserve institutional knowledge

---

## Usage Examples

```bash
# Generate API documentation
/docs "API reference guide"

# Create user guide
/docs "User manual for authentication system"

# Update existing documentation
/docs --update "installation guide"

# Generate technical specification
/docs "Database schema documentation" --type technical

# Create troubleshooting guide
/docs "Common issues and solutions" --type troubleshooting
```

---

## What It Does

### Documentation Creation
- Generates comprehensive documentation from scratch
- Creates user guides, API docs, and technical specifications
- Structures content for optimal usability
- Includes examples, diagrams, and code samples

### Content Organization
- Organizes documentation in logical hierarchies
- Creates clear navigation and structure
- Establishes consistent formatting and style
- Implements effective cross-referencing

### Quality Assurance
- Reviews content for accuracy and completeness
- Ensures consistent style and formatting
- Validates technical accuracy
- Optimizes for user experience

### Maintenance Support
- Tracks changes and updates over time
- Maintains documentation currency
- Incorporates user feedback
- Preserves institutional knowledge

---

## Documentation Types

### User Documentation
```
PURPOSE: Help users understand and use the system
AUDIENCE: End users, customers, stakeholders
CONTENT: User guides, tutorials, FAQs, troubleshooting
```

### Technical Documentation
```
PURPOSE: Support developers and technical teams
AUDIENCE: Developers, system administrators, architects
CONTENT: API docs, technical specs, architecture guides
```

### Process Documentation
```
PURPOSE: Document procedures and workflows
AUDIENCE: Team members, new hires, stakeholders
CONTENT: Process guides, workflows, standards, policies
```

### Knowledge Base
```
PURPOSE: Capture and preserve institutional knowledge
AUDIENCE: Team members, future developers, stakeholders
CONTENT: Lessons learned, best practices, decision records
```

---

## Output Format

### Documentation Summary
```
DOCUMENT_TYPE: [user/technical/process/knowledge-base]
TITLE: [document-title]
AUDIENCE: [target-audience]
STATUS: [draft/review/published]
```

### Content Structure
```
SECTIONS: [main-sections-and-subsections]
ORGANIZATION: [document-organization-approach]
NAVIGATION: [navigation-structure]
CROSS_REFERENCES: [related-documents-and-links]
```

### Quality Metrics
```
COMPLETENESS: [content-completeness-assessment]
ACCURACY: [technical-accuracy-validation]
USABILITY: [user-experience-evaluation]
CONSISTENCY: [style-and-format-consistency]
```

### Maintenance Plan
```
UPDATE_SCHEDULE: [planned-update-frequency]
REVIEW_PROCESS: [content-review-procedures]
FEEDBACK_INTEGRATION: [user-feedback-incorporation]
VERSION_CONTROL: [version-tracking-approach]
```

---

## Documentation Standards

### Structure Guidelines
- **Clear Hierarchy**: Logical organization with clear headings
- **Consistent Formatting**: Uniform style and formatting
- **Navigation**: Easy-to-use navigation and cross-references
- **Accessibility**: Accessible to all users and devices

### Content Standards
- **Accuracy**: Technically accurate and current information
- **Completeness**: Comprehensive coverage of topics
- **Clarity**: Clear, concise, and understandable language
- **Examples**: Practical examples and code samples

### Style Guidelines
- **Tone**: Appropriate tone for target audience
- **Language**: Clear, professional language
- **Formatting**: Consistent formatting and style
- **Visual Elements**: Effective use of diagrams and illustrations

---

## Key Features

### ✅ Comprehensive Coverage
- User guides and tutorials
- API and technical documentation
- Process and workflow documentation
- Knowledge base and best practices

### ✅ User-Focused Design
- Audience-appropriate content
- Clear navigation and structure
- Practical examples and illustrations
- Accessibility considerations

### ✅ Quality Assurance
- Content accuracy validation
- Style consistency enforcement
- Usability optimization
- Regular review and updates

### ✅ Maintenance Support
- Version control and tracking
- Update scheduling and management
- User feedback integration
- Knowledge preservation

---

## Documentation Process

### 1. Planning Phase
- Define documentation goals and objectives
- Identify target audience and use cases
- Plan content structure and organization
- Establish style guidelines and standards

### 2. Content Creation Phase
- Generate documentation content
- Structure information logically
- Add examples, diagrams, and code samples
- Create cross-references and navigation

### 3. Review Phase
- Review content for accuracy and completeness
- Validate technical information
- Ensure style consistency
- Optimize for user experience

### 4. Publication Phase
- Finalize documentation format
- Publish to appropriate channels
- Set up maintenance procedures
- Establish feedback collection

---

## Content Types

### User Guides
- **Getting Started**: Introduction and setup guides
- **Tutorials**: Step-by-step learning materials
- **How-To Guides**: Task-focused instructions
- **Reference**: Comprehensive reference materials

### API Documentation
- **API Reference**: Complete API endpoint documentation
- **Authentication**: Authentication and authorization guides
- **Examples**: Code examples and sample requests
- **SDKs**: SDK documentation and usage guides

### Technical Specifications
- **Architecture**: System architecture documentation
- **Database**: Database schema and design documentation
- **Integrations**: Third-party integration documentation
- **Security**: Security implementation and guidelines

### Process Documentation
- **Workflows**: Process and workflow documentation
- **Standards**: Coding and development standards
- **Procedures**: Operational procedures and guidelines
- **Policies**: Company policies and guidelines

---

## Best Practices

### When to Use
- **New Features**: When new functionality is added
- **System Changes**: When system architecture changes
- **User Onboarding**: When new users need guidance
- **Knowledge Preservation**: When capturing institutional knowledge

### Documentation Tips
- Write for your audience
- Use clear, simple language
- Include practical examples
- Keep content current and accurate
- Make it easy to navigate

### Quality Guidelines
- Ensure technical accuracy
- Maintain consistent style
- Optimize for usability
- Include visual elements when helpful
- Regular review and updates

---

## Error Handling

### Common Issues
- **Complex Topics**: Breaks down complex information into digestible chunks
- **Technical Accuracy**: Validates technical information with experts
- **User Experience**: Optimizes for user understanding and navigation
- **Maintenance**: Establishes sustainable update procedures

### Graceful Degradation
- Provides partial documentation when complete coverage complex
- Suggests iterative improvement approach
- Maintains existing quality while adding new content
- Documents limitations and future improvements

---

## Integration

### Works Well With
- `/context-prime` - For project context before documentation
- `/research` - For gathering information and background
- `/review` - For documentation quality review
- `/task` - For implementing documentation updates

### Typical Workflow
1. **Context**: `/context-prime` to understand project context
2. **Research**: `/research` to gather information and background
3. **Documentation**: `/docs` to create and structure content
4. **Review**: `/review` to ensure quality and accuracy

---

## Documentation Formats

### Markdown Documentation
- **Advantages**: Version control friendly, easy to edit
- **Use Cases**: Technical documentation, README files
- **Tools**: Markdown editors, static site generators
- **Maintenance**: Easy to update and maintain

### HTML Documentation
- **Advantages**: Rich formatting, interactive elements
- **Use Cases**: User guides, online help systems
- **Tools**: Documentation generators, CMS systems
- **Maintenance**: Requires web maintenance skills

### PDF Documentation
- **Advantages**: Professional appearance, offline access
- **Use Cases**: Formal documentation, reports
- **Tools**: Document processors, PDF generators
- **Maintenance**: More complex update process

### Interactive Documentation
- **Advantages**: Hands-on learning, immediate feedback
- **Use Cases**: API documentation, tutorials
- **Tools**: Interactive documentation platforms
- **Maintenance**: Requires specialized tools

---

## Quality Metrics

### Content Quality
- **Accuracy**: Technical accuracy and correctness
- **Completeness**: Comprehensive coverage of topics
- **Clarity**: Clear and understandable language
- **Relevance**: Relevance to user needs and goals

### User Experience
- **Usability**: Ease of finding and using information
- **Navigation**: Clear structure and navigation
- **Accessibility**: Accessible to all users
- **Performance**: Fast loading and responsive design

### Maintenance
- **Currency**: Up-to-date and current information
- **Consistency**: Consistent style and formatting
- **Feedback**: User feedback integration
- **Sustainability**: Maintainable update processes

---

## Documentation Tools

### Generation Tools
- **Static Site Generators**: Jekyll, Hugo, Gatsby
- **Documentation Platforms**: GitBook, Notion, Confluence
- **API Documentation**: Swagger, Postman, Insomnia
- **Code Documentation**: JSDoc, Sphinx, Doxygen

### Collaboration Tools
- **Version Control**: Git, GitHub, GitLab
- **Review Tools**: Pull request reviews, collaborative editing
- **Feedback Collection**: User feedback systems
- **Analytics**: Documentation usage analytics

---

## Differences from Full Framework

### Simplified Approach
- **No Complex XML**: Simple documentation workflow
- **No Module Dependencies**: Self-contained documentation logic
- **No Advanced Frameworks**: Basic documentation patterns
- **No Mandatory Enforcement**: Supportive documentation guidance

### Core Focus
- **Essential Documentation**: Core content creation and organization
- **Practical Quality**: Basic quality assurance and validation
- **Fast Execution**: Minimal overhead for quick documentation
- **Clear Results**: Well-structured, usable documentation

---

**Note**: This simplified command provides core documentation functionality without the complexity of the full framework. For advanced features like FOCUS framework integration, complex content management, or multi-agent documentation coordination, use the full framework commands.