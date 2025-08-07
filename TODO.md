# Gmail MCP Server - Smithery Deployment TODO

This document tracks the necessary steps to prepare the Gmail MCP server for deployment on Smithery based on their deployment documentation requirements.

## 🎯 **Deployment Preparation Checklist**

### **Phase 1: Core Deployment Requirements**

- [ ] **Merge PR and update master branch with email enhancement features**
  - Merge PR #1 with the comprehensive email composition assistance
  - Ensure master branch has all the new prompts, resources, and tools

- [ ] **Create smithery.yaml configuration file in repository root**
  - Configure runtime settings for Smithery deployment
  - Specify deployment parameters and requirements

- [ ] **Update pyproject.toml with proper entry points for MCP server**
  - Ensure proper MCP server entry points are defined
  - Configure package metadata for Smithery compatibility

### **Phase 2: Technical Requirements**

- [ ] **Implement lazy loading to allow tool discovery without authentication**
  - Modify server to handle MCP discovery requests without requiring Gmail auth
  - Allow users to see available tools before authenticating
  - Critical for Smithery deployment success

- [ ] **Create Dockerfile for custom Docker deployment option**
  - Provide alternative deployment method via Docker
  - Ensure server listens on `PORT` environment variable
  - Implement `/mcp` endpoint with GET, POST, DELETE support

- [ ] **Test server startup and tool discovery without authentication**
  - Verify MCP protocol compliance
  - Ensure tools are discoverable before Gmail authentication
  - Test error handling for unauthenticated tool usage

- [ ] **Verify server responds properly to MCP discovery requests**
  - Test MCP protocol endpoints
  - Validate tool and prompt discovery
  - Ensure proper error responses

### **Phase 3: Documentation & Community**

- [ ] **Add MIT or Apache 2.0 license file to repository**
  - Choose appropriate open source license
  - Add LICENSE file to repository root
  - Ensure community can legally use and contribute

- [ ] **Create CONTRIBUTING.md guidelines for community contributions**
  - Define contribution process and standards
  - Include development setup instructions
  - Specify code quality requirements

- [ ] **Add GitHub issue templates for bug reports and feature requests**
  - Create `.github/ISSUE_TEMPLATE/` directory
  - Add bug report template
  - Add feature request template
  - Add support question template

- [ ] **Update README with Smithery deployment instructions**
  - Add section on installing from Smithery
  - Include Smithery-specific setup instructions
  - Maintain existing local installation docs

### **Phase 4: Deployment & Testing**

- [ ] **Deploy to Smithery and test end-to-end functionality**
  - Submit server to Smithery
  - Test deployment process
  - Verify all features work in deployed environment
  - Test with fresh user authentication flow

## 📚 **Reference Documentation**

- **Smithery Deployment Docs**: https://smithery.ai/docs/build/deployments
- **MCP Protocol Specification**: For implementation details
- **Current PR**: https://github.com/parthashirolkar/gmail-mcp/pull/1

## 🔧 **Technical Notes**

### **Key Smithery Requirements**
1. **Lazy Loading**: Tool discovery must work without authentication
2. **MCP Protocol**: Server must properly implement MCP endpoints
3. **Configuration**: `smithery.yaml` required in repository root
4. **Entry Points**: Proper `pyproject.toml` configuration needed

### **Deployment Options**
- **Option A**: Python package deployment (simpler)
- **Option B**: Custom Docker deployment (more control)

### **Current Status**
- ✅ Feature development complete (2,427 lines added)
- ✅ PR created and ready for merge
- ✅ Code quality verified (ruff linting passed)
- 🔄 Ready for deployment preparation phase

---

*Created: $(date)*
*Status: Ready for implementation*

## 📝 **Notes**

- Prioritize Phase 1 and Phase 2 items for successful Smithery deployment
- Phase 3 items enhance community adoption but are not strictly required
- Test thoroughly in Phase 4 before announcing public availability
- Consider creating a staging deployment first for testing