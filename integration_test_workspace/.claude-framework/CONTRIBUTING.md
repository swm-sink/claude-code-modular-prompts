# Contributing to Claude Code Template Library

Thank you for your interest in contributing! This project thrives on community contributions, especially **adaptation patterns** that help others customize the templates for their specific use cases.

## 🤝 Types of Contributions We Welcome

### 1. **Adaptation Patterns** (Most Valuable!)
Share how you customized the templates for your specific project:
- Domain-specific adaptations (e.g., fintech, healthcare, e-commerce)
- Technology stack patterns (e.g., MEAN stack, JAMstack, serverless)
- Team size optimizations (solo developer vs. enterprise team)
- Workflow customizations (agile, DevOps, research-focused)

### 2. **Bug Reports**
Found an issue with the templates or documentation?
- Incorrect placeholders
- Broken command syntax
- Documentation errors
- Setup script issues

### 3. **Template Improvements**
Suggestions for better templates:
- New placeholders that would be useful
- Better command descriptions
- Improved prompt engineering patterns
- Additional examples

### 4. **New Command Templates**
Propose new commands that would benefit the community:
- Must be generic enough to adapt
- Should follow existing patterns
- Include proper placeholders

### 5. **Documentation Enhancements**
Help others understand and use the library:
- Clearer instructions
- Additional examples
- Video tutorials or guides
- Translation to other languages

## 📝 How to Contribute

### Sharing an Adaptation Pattern

1. **Document Your Adaptation**
   Use the `/share-adaptation` command to generate a template:
   ```bash
   /share-adaptation
   ```
   This provides a structured format for documenting:
   - What placeholders you replaced
   - What values you used
   - Why you made specific choices
   - Any custom modifications

2. **Create an Adaptation File**
   Save your pattern as: `adaptations/[domain]-[stack]-pattern.md`
   
   Example: `adaptations/ecommerce-nodejs-pattern.md`
   ```markdown
   # E-commerce Node.js Adaptation Pattern
   
   ## Overview
   - **Domain**: E-commerce
   - **Stack**: Node.js, Express, PostgreSQL, React
   - **Team Size**: 5-10 developers
   - **Special Requirements**: PCI compliance, real-time inventory
   
   ## Placeholder Mappings
   - `[INSERT_PROJECT_NAME]` → "CommerceAPI"
   - `[INSERT_DOMAIN]` → "e-commerce"
   - `[INSERT_TECH_STACK]` → "Node.js/Express/PostgreSQL"
   - `[INSERT_COMPLIANCE_REQUIREMENTS]` → "PCI-DSS"
   ...
   
   ## Custom Modifications
   - Added custom `/inventory-sync` command
   - Modified `/deploy` for blue-green deployments
   - Enhanced `/secure-assess` for PCI compliance
   
   ## Lessons Learned
   - Real-time features required WebSocket placeholders
   - Payment processing needed additional security commands
   ```

3. **Submit via GitHub**
   - Fork the repository
   - Add your adaptation file
   - Create a pull request with tag `adaptation-pattern`

### Reporting Bugs

1. **Check Existing Issues**
   Search [existing issues](https://github.com/swm-sink/claude-code-modular-prompts/issues) first

2. **Create Bug Report**
   Use this template:
   ```markdown
   **Describe the bug**
   Clear description of what's wrong
   
   **To Reproduce**
   1. Run command '...'
   2. See error
   
   **Expected behavior**
   What should happen instead
   
   **Environment**
   - OS: [e.g., macOS 13.0]
   - Claude Code version: [e.g., 1.0.0]
   - Shell: [e.g., zsh]
   
   **Additional context**
   Any other relevant information
   ```

3. **Tag Appropriately**
   - `bug` - Something isn't working
   - `documentation` - Documentation issues
   - `setup` - Installation problems

### Suggesting Improvements

1. **Open a Discussion**
   Start with a GitHub Discussion for:
   - Major changes
   - New features
   - Architecture decisions

2. **Proposal Template**
   ```markdown
   **Problem Statement**
   What limitation or issue does this address?
   
   **Proposed Solution**
   How would you solve it?
   
   **Alternatives Considered**
   What other approaches did you think about?
   
   **Impact**
   - Who benefits?
   - Any breaking changes?
   - Implementation effort?
   ```

## 🔧 Development Setup

If you want to contribute code or test changes:

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR-USERNAME/claude-code-modular-prompts.git
   cd claude-code-modular-prompts
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Test Your Changes**
   ```bash
   # Run validation
   ./tests/validate-command.sh .claude/commands/**/*.md
   
   # Test setup script
   ./setup.sh test-directory
   ```

4. **Commit Guidelines**
   - Use clear, descriptive commit messages
   - Reference issues: `fixes #123`
   - Keep commits atomic and focused

5. **Submit Pull Request**
   - Fill out the PR template
   - Link related issues
   - Describe testing performed

## 📋 Contribution Guidelines

### For Adaptation Patterns
- **Be Specific**: Include actual values, not just descriptions
- **Explain Why**: Document reasoning behind choices
- **Show Results**: Include examples of customized commands
- **List Challenges**: What was difficult? How did you solve it?

### For Command Templates
- **Use Standard Placeholders**: Stick to the 15 standard placeholders
- **Keep Generic**: Templates should work for multiple use cases
- **Follow Patterns**: Match existing command structure
- **Document Well**: Clear descriptions and usage examples

### For Documentation
- **Test Instructions**: Ensure steps actually work
- **Use Examples**: Show, don't just tell
- **Consider Beginners**: Don't assume deep Claude Code knowledge
- **Stay Focused**: One topic per contribution

### Code Style
- **Markdown**: Follow existing formatting patterns
- **YAML Front Matter**: Required for all commands
- **Placeholders**: Always use `[INSERT_XXX]` format
- **Line Length**: Keep under 100 characters when possible

## 🏆 Recognition

We value all contributions! Contributors are:
- Listed in CONTRIBUTORS.md
- Credited in release notes
- Thanked in project documentation

### Adaptation Pattern Hall of Fame
Outstanding adaptation patterns may be:
- Featured in EXAMPLES.md
- Included as reference implementations
- Used as templates for new domains

## 🚦 Review Process

1. **Initial Review** (1-3 days)
   - Maintainers check for completeness
   - Verify it follows guidelines
   - Test basic functionality

2. **Community Feedback** (3-7 days)
   - Other users may comment
   - Suggestions for improvements
   - Testing in different environments

3. **Final Review**
   - Address any feedback
   - Final testing
   - Merge or request changes

## 📞 Getting Help

- **Questions**: Use GitHub Discussions
- **Chat**: Join our community (coming soon)
- **Email**: support@example.com (placeholder)

## 🌟 Tips for Great Contributions

1. **Start Small**: First contribution? Try documenting your adaptation
2. **Ask Questions**: Unsure? Open a discussion first
3. **Share Early**: WIP pull requests are welcome
4. **Help Others**: Review other contributions
5. **Be Patient**: Maintainers are volunteers

## 📜 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

Key points:
- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as this project (MIT License).

---

**Thank you for making Claude Code Template Library better for everyone!** 🙏

*Remember: The best contributions come from real-world usage. Share what worked for you!*