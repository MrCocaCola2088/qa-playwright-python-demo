# QA Automation Demo – Playwright + Python

This project demonstrates a comprehensive test automation approach for a multi-tenant CRM system using Playwright, Python, and modern testing practices.

## Project Structure

```
qa-playwright-python-demo/
├── README.md
├── requirements.txt
├── pytest.ini
├── tests/
│   ├── ui/
│   │   ├── test_login.py
│   │   └── test_tenant_dashboard.py
│   ├── api/
│   │   ├── test_create_customer.py
│   │   ├── test_tenant_isolation.py
│   │   ├── test_debt_logic.py
│   │   ├── test_contract_customer.py
│   │   └── test_db_validation.py
│   └── integration/
│       ├── test_ui_api_flow.py
│       └── test_ui_api_customer.py
├── pages/
│   ├── login_page.py
│   └── dashboard_page.py
├── fixtures/
│   ├── base_fixture.py
│   └── test_data.py
├── utils/
│   ├── config.py
│   ├── api_client.py
│   ├── db_client.py
│   └── schemas.py
└── .github/
    └── workflows/
        └── tests.yml
```

## Features

### UI Automation
- **Playwright-based** browser automation with Python
- **Page Object Model** for maintainable and reusable tests
- Multi-tenant dashboard validation
- Login flow automation

### API Testing
- RESTful API testing with realistic CRM scenarios
- Multi-tenant customer creation and retrieval
- Business logic validation (debt calculations)
- Tenant isolation verification

### Contract Testing
- **Pydantic schemas** for API response validation
- Type-safe contract enforcement
- Early detection of API contract violations

### Database Testing
- PostgreSQL integration for data persistence verification
- Multi-tenant data isolation validation
- End-to-end data integrity checks

### Integration Testing
- UI + API hybrid workflows
- Cross-layer validation
- Real-world CRM scenarios

### CI/CD
- GitHub Actions automation
- Containerized PostgreSQL for consistent test environments
- Automated test execution on push
- Scalable parallel test execution

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
playwright install
```

3. Configure environment variables (if needed):
```bash
export DB_HOST=localhost
export DB_USER=postgres
export DB_PASSWORD=password
export DB_NAME=crm_db
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run UI tests only
```bash
pytest tests/ui/
```

### Run API tests only
```bash
pytest tests/api/
```

### Run integration tests only
```bash
pytest tests/integration/
```

### Run with verbose output
```bash
pytest -v
```

### Run with headless browser off (see UI)
```bash
pytest tests/ui/ --headed
```

## Test Coverage

- ✅ **UI Automation**: Login flows, multi-tenant dashboard switching
- ✅ **API Testing**: Customer CRUD operations, multi-tenant isolation
- ✅ **Contract Testing**: Pydantic schema validation
- ✅ **Database Testing**: Data persistence and tenant isolation
- ✅ **Integration**: UI + API end-to-end flows

## Key Concepts

### Page Object Model
Pages are abstracted into reusable classes (`pages/login_page.py`, `pages/dashboard_page.py`) for maintainability and clarity.

### Multi-Tenant Architecture
All tests validate tenant isolation:
- Data is scoped to specific tenants
- Cross-tenant access is blocked (403/404 responses)
- Database queries enforce tenant boundaries

### Fixtures
Centralized test fixtures (`fixtures/base_fixture.py`) provide consistent browser setup and teardown.

### Test Data
Reusable test data payloads (`fixtures/test_data.py`) ensure consistency across tests.

## CI/CD Pipeline

GitHub Actions workflow (`.github/workflows/tests.yml`):
- Runs on every push
- Spins up PostgreSQL container
- Installs dependencies and Playwright browsers
- Executes full test suite

## Real-World Scenarios

This demo covers actual CRM workflows:
1. **User Login**: Authentication and session management
2. **Tenant Selection**: Multi-tenant UI navigation
3. **Customer Creation**: UI form submission + API validation
4. **Data Verification**: API + Database cross-layer validation
5. **Tenant Isolation**: Security boundary testing

## Dependencies

See `requirements.txt` for the full list. Key dependencies:
- `playwright` — UI automation
- `pytest` — Test framework
- `pytest-playwright` — Playwright pytest plugin
- `requests` — HTTP client for API testing
- `pydantic` — Data schema validation
- `psycopg2-binary` — PostgreSQL driver

## Notes

- Tests use mock/fake tokens for API authentication
- Database tests require a running PostgreSQL instance
- UI tests are headless by default (use `--headed` to see browser)
- All tests support parallel execution via pytest-xdist

## Future Enhancements

- Performance testing with k6
- Visual regression testing
- Accessibility testing
- Load testing for API endpoints
