# Modern FastAPI Enterprise Boilerplate

A highly modular, app-based FastAPI template designed for scalability and flexibility, drawing inspiration from Django's project structure while maintaining FastAPI's performance benefits.
Whether you're building a small API or a large-scale enterprise system, this template provides the foundation and flexibility to grow with your needs, combining modern Python practices with proven architectural patterns.

## 🎯 Design Philosophy

- **App-Based Architecture**: Modular structure where each business domain is a separate app
- **Plugin System**: Optional features as plugins that can be enabled/disabled
- **Configuration Driven**: All components are configurable via environment variables
- **Loose Coupling**: Apps communicate via well-defined interfaces
- **Domain-Driven**: Each app represents a bounded context


## Installation & Getting Started

1. Clone the repository
```bash
git clone https://github.com/AliMuhammadOfficial/FastAPI-enterprise-boilerplate.git
cd FastAPI-enterprise-boilerplate
```

2. Install `uv` (Optional but recommended)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# On Windows:
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. Create and activate virtual environment
```bash
uv venv
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

4. Install dependencies and run
```bash
uv sync  # Install dependencies from pyproject.toml
uv run uvicorn main:app --reload  # Start the development server
```

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add some awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

Please ensure your PR follows our coding standards and includes appropriate tests.
