
# AI Automation Framework
Automated test suite for Agentic platform:
- Agent Integration
- Model Integration
- UX/UI Validation
This framework validates:
- Data extraction & schema compliance
- AI model input/output & safety
- UI/UX scenarios including file uploads, error handling, accessibility

Includes automation with Pytest + Selenium and CI/CD integration via GitHub Actions.
## Folder Structure

ai_automation/
├── tests/                  # All test files (Agent/Model/UI)
├── pages/                  # Page Object Models
├── locators/               # UI locators
├── utils/                  # Utility scripts (Excel reader)
├── test_cases.xlsx         # Test data
├── conftest.py             # Pytest fixtures
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration
└── .github/workflows/ci.yml # GitHub Actions workflow
