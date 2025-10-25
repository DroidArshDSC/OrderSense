# 🤝 OrderSense — Contributing Guidelines

## 1. Purpose

This document defines contribution standards for **OrderSense**.  
The objective is to maintain **code quality, version control discipline, and documentation integrity** as the project scales.



## 2. Contribution Philosophy

- **Clarity over cleverness.** Write readable, maintainable code.  
- **One change → one PR.** No bundled, multi-purpose commits.  
- **Documentation is mandatory.** Every new module or endpoint must include a matching doc update.  
- **Predictable delivery.** Follow the roadmap and respect scope — no unreviewed features.


## 3. Branching Strategy

| Branch | Purpose |
|---------|----------|
| **main** | Production-ready releases |
| **dev** | Active development and integration |
| **feature/*** | One feature per branch |
| **hotfix/*** | Emergency patches for production |
| **docs/*** | Documentation-only changes |

**Rules:**
- No direct commits to `main`.  
- All feature branches must be merged via Pull Request.  
- Each PR requires at least one reviewer approval.  

## 4. Commit Message Convention

Follow the [Conventional Commits](https://www.conventionalcommits.org/) standard.

**Format:** <type>(scope): <short summary>

**Examples:**
feat(api): add forecast generation endpoint
fix(validation): handle negative quantities properly
docs(ui): update Streamlit layout in blueprint
chore: update dependencies

**Allowed Types:**
`feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## 5. Pull Request Checklist

Before creating a PR:
- [ ] Code runs locally without errors  
- [ ] All tests pass (`pytest` or equivalent)  
- [ ] Updated related `/docs/*.md` if functionality changed  
- [ ] Added type hints and inline comments where relevant  
- [ ] Linted code with `black` or `flake8`  
- [ ] Included screenshot or test data (if UI or visual)  
- [ ] PR title follows commit message convention 

## 6. Code Quality Standards

| Category | Guideline |
|-----------|------------|
| **Style** | Follow PEP8 + black formatting |
| **Typing** | All public functions must have type hints |
| **Logging** | Use `logging` module, no print statements |
| **Config** | Environment variables handled via `.env` and Pydantic settings |
| **Security** | Never hardcode credentials or API keys |
| **Dependencies** | Keep minimal; list explicitly in `requirements.txt` |

## 7. Testing Guidelines

- **Framework:** `pytest`
- **Minimum coverage:** 80% for core modules
- Tests must exist for:
  - Data validation
  - Forecast generation
  - API endpoint responses
  - Recommendation logic
- Mock data stored under `/tests/data/`

Run all tests locally:
```bash
pytest -v
```

## 8. Documentation Policy

- Every new feature or endpoint must update:
    - /docs/api-design.md (if API-related)
    - /docs/model-lifecycle.md (if ML-related)
    - /docs/roadmap.md (if milestone change)
- Markdown only — no PDFs or screenshots.

## 9. Issue Reporting

When filing an issue:
- Use a clear, specific title.
- Describe expected vs. actual behavior.
- Include steps to reproduce.
- Label appropriately (`bug`, `enhancement`, `docs`, `question`).

## 10. Release Protocol

| Stage                | Action                               |
| -------------------- | ------------------------------------ |
| 1. Code freeze       | Merge only hotfixes to `dev`         |
| 2. QA validation     | Run tests + validation reports       |
| 3. Tag release       | `git tag -a v0.x -m "Release notes"` |
| 4. Merge → `main`    | Via approved PR                      |
| 5. Update roadmap.md | Document version changes             |

## 11. Communication Etiquette

- Keep PR and issue comments professional, brief, and actionable.
- No “nice-to-haves” mid-sprint — backlog them.
- Always link code changes to relevant roadmap phase.

## 12. Getting Started (Contributor Setup)

```bash
# Clone the repository
git clone https://github.com/DroidArshDSC/OrderSense.git
cd ordersense

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run local backend
uvicorn app.main:app --reload
```

**Maintainer:** Arsh Deep Singh  
📧 arshds289@gmail.com 

