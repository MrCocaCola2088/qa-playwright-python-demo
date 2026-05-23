# QA Automation Strategy Demo – Playwright + Python

This repository demonstrates how I approach test automation for a complex, multi-tenant CRM platform, similar to financial systems handling customer data, debt flows, and tenant isolation.

The goal is not just to automate tests, but to design a **scalable, maintainable, and risk-based testing strategy**.

---

## 🧠 Testing Philosophy

For systems like CRMs with financial logic and multi-tenancy, I prioritize:

- **API and contract testing** for core business logic
- **Data integrity validation** at the database level
- **Tenant isolation validation** (critical in multi-tenant systems)
- **UI automation only for critical user journeys**
- **Deterministic CI pipelines using mocks and isolation**



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

## 🔍 Test Coverage Overview

### ✅ API Testing
- Customer creation
- Tenant-based data isolation
- Financial logic validation (e.g., debt calculations)
- Mocked external dependencies for CI stability

### ✅ Contract Testing
- Schema validation using Pydantic
- Ensures API responses meet expected structure
- Prevents breaking changes between services

### ✅ Database Validation
- Verifies data persistence after API operations
- Includes mocked DB tests for CI
- Real DB tests are intentionally skipped in CI

### ✅ Multi-Tenant Testing
- Ensures strict separation of tenant data
- Validates access control boundaries
- Critical for SaaS and financial platforms

### ✅ UI Testing (Playwright)
- Login flow
- Tenant dashboard validation
- Designed using Page Object Model (POM)

### ✅ Integration Testing
- UI + API combined validation
- Example: Create via UI → Validate via API

---

## ⚙️ CI/CD Strategy (GitHub Actions)

This project is designed with **real-world CI constraints in mind**.

### In CI we:

- ✅ Run **API + contract tests**
- ✅ Run **mocked DB tests**
- ❌ Skip UI tests (require browser + environment)
- ❌ Skip integration tests (depend on full system)

### Command used in CI:

```bash
pytest -v -m "not ui and not integration"
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


