# AI Automation Framework

Automated test suite for the Agentic Platform covering:

- **Agent Integration**: Data extraction & schema compliance  
- **Model Integration**: AI model input/output validation, safety & explainability  
- **UX/UI Validation**: UI/UX scenarios including file uploads, error handling, accessibility  

Includes automation with **Pytest + Selenium** and **CI/CD integration via GitHub Actions**.

---

## Folder Structure

```
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
```

---

## Prerequisites

- Python 3.9+  
- Google Chrome & ChromeDriver  
- Pip packages in `requirements.txt`  

---

## Installation

```bash
git clone https://github.com/<your-username>/ai_automation.git
cd ai_automation
pip install -r requirements.txt
```

---

## Running Tests

```bash
# Run all tests
pytest --html=reports/report.html --self-contained-html

# Run only high-priority tests
pytest -m "high" --html=reports/report.html --self-contained-html
```

> **Note:** Only tests with `RunMode=Yes` in `test_cases.xlsx` will execute.

---

## CI/CD Integration

- GitHub Actions workflow (`.github/workflows/ci.yml`) runs tests automatically on push  
- Generates **HTML report** and saves as artifact  
- Filters tests by **RunMode=Yes** and **priority markers** (`@pytest.mark.high`, `@pytest.mark.medium`, `@pytest.mark.low`)  

---

## Notes

- Update `test_cases.xlsx` for new test cases  
- Ensure `RunMode` column is set to **Yes** for tests you want to execute  
- Selenium actions use **Chrome headless mode** by default  

---

## Contact / Support

For issues, please create an **issue** in this repository.
