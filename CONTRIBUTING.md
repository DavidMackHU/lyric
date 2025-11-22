# Contributing to LyrIQ

Thank you for your interest in contributing to LyrIQ! This document provides guidelines and instructions for contributing.

## Development Setup

Please refer to the main [README.md](README.md) for setup instructions.

## Git Workflow

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes** and test thoroughly

3. **Commit your changes** with clear, descriptive messages:
   ```bash
   git commit -m "Add feature: description of what you added"
   git commit -m "Fix: description of what you fixed"
   ```

4. **Push to your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** on GitHub

## Code Style

### Frontend (React/TypeScript)
- Use TypeScript for all new files
- Follow React best practices and hooks patterns
- Use Material UI components for consistency
- Keep components small and focused
- Use meaningful variable and function names

### Backend (Django/Python)
- Follow PEP 8 style guide
- Use Django conventions and best practices
- Write docstrings for functions and classes
- Keep views and serializers organized

## Testing

Before submitting a PR:
- Test your changes locally
- Ensure the application runs without errors
- Test on different screen sizes (responsive design)
- Verify authentication flows work correctly

## Pull Request Guidelines

- Provide a clear description of what the PR does
- Reference any related issues
- Ensure all tests pass
- Update documentation if needed
- Request review from at least one team member

## Questions?

If you have questions, please reach out to the team or create an issue on GitHub.


