"""Validation tests for motto-appraisal-service-privacy (static HTML privacy page)."""
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent


def test_index_html_exists_and_has_doctype():
    """Verify index.html exists and starts with a DOCTYPE declaration."""
    path = REPO / "index.html"
    assert path.is_file(), "Missing index.html"
    content = path.read_text(encoding="utf-8")
    assert len(content) > 500, f"index.html too small ({len(content)} bytes)"
    assert "<!DOCTYPE html>" in content, "index.html missing DOCTYPE"
    assert "<html" in content, "index.html missing <html> tag"
    assert "</html>" in content, "index.html missing closing </html> tag"


def test_index_html_has_head_and_body():
    """Verify index.html has <head> and <body> elements."""
    content = (REPO / "index.html").read_text(encoding="utf-8")
    assert "<head>" in content or "<head " in content, "index.html missing <head>"
    assert "</head>" in content, "index.html missing closing </head>"
    assert "<body>" in content or "<body " in content, "index.html missing <body>"
    assert "</body>" in content, "index.html missing closing </body>"


def test_readme_exists_and_nonempty():
    """Verify README.md exists with content."""
    path = REPO / "README.md"
    assert path.is_file(), "Missing README.md"
    content = path.read_text(encoding="utf-8")
    assert len(content) > 0, "README.md is empty"


def test_contributing_exists():
    """Verify CONTRIBUTING.md exists."""
    path = REPO / "CONTRIBUTING.md"
    assert path.is_file(), "Missing CONTRIBUTING.md"
    content = path.read_text(encoding="utf-8")
    assert len(content) > 0, "CONTRIBUTING.md is empty"


def test_release_please_config_is_valid_json():
    """Verify release-please-config.json is valid JSON."""
    import json
    path = REPO / "release-please-config.json"
    assert path.is_file(), "Missing release-please-config.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict), "release-please-config.json is not a JSON object"


def test_pre_commit_config_is_valid_yaml():
    """Verify .pre-commit-config.yaml exists and contains YAML."""
    path = REPO / ".pre-commit-config.yaml"
    assert path.is_file(), "Missing .pre-commit-config.yaml"
    content = path.read_text(encoding="utf-8")
    assert len(content) > 0, ".pre-commit-config.yaml is empty"
    assert "repo" in content or "repos" in content, \
        ".pre-commit-config.yaml missing repo/repos keys"
