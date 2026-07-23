#!/usr/bin/env python3
"""Build, validate, search, publish, and monitor the research knowledge base."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import sqlite3
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml


ROOT = Path(__file__).resolve().parents[1]
INDEX_DIR = ROOT / "index"
PUBLIC_DIR = ROOT / "public"
SCHEMA_PATH = ROOT / "schemas" / "document-types.yaml"
DOC_DIRS = (ROOT / "papers", ROOT / "claims", ROOT / "concepts")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
PRIVATE_MARKERS = ("/home/", "sources/files/", "worklog/")
TEXT_SCAN_SUFFIXES = {".md", ".yaml", ".yml", ".bib"}
TEXT_SCAN_EXCLUDED = {".git", "index", "public", "sources", "__pycache__"}


@dataclass(frozen=True)
class Document:
    path: Path
    meta: dict[str, Any]
    body: str

    @property
    def doc_id(self) -> str:
        return str(
            self.meta.get("citation_key")
            or self.meta.get("claim_id")
            or self.meta.get("concept_id")
            or self.path.stem
        )

    @property
    def kind(self) -> str:
        return str(self.meta.get("kind", ""))

    @property
    def title(self) -> str:
        return str(self.meta.get("title", ""))

    @property
    def year(self) -> int | None:
        value = self.meta.get("year")
        try:
            return int(value) if value is not None else None
        except (TypeError, ValueError):
            return None


def load_schema() -> dict[str, Any]:
    return yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))


def parse_document(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing YAML frontmatter")
    meta = yaml.safe_load(match.group(1))
    if not isinstance(meta, dict):
        raise ValueError("frontmatter must be a mapping")
    return Document(path=path, meta=meta, body=text[match.end() :].strip())


def iter_documents() -> Iterable[Document]:
    for directory in DOC_DIRS:
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name.startswith("_"):
                continue
            yield parse_document(path)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def normalize_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def source_paper_keys(meta: dict[str, Any]) -> set[str]:
    result: set[str] = set()
    for source in normalize_list(meta.get("sources")):
        if isinstance(source, str):
            result.add(source)
        elif isinstance(source, dict) and source.get("paper"):
            result.add(str(source["paper"]))
    return result


def validate_documents(documents: list[Document]) -> list[str]:
    schema = load_schema()
    errors: list[str] = []
    ids: dict[str, Path] = {}
    paper_keys = {doc.doc_id for doc in documents if doc.kind == "paper"}

    for doc in documents:
        label = relative(doc.path)
        required = list(schema["common_required"])
        required.extend(schema.get(f"{doc.kind}_required", []))
        if doc.kind not in schema["controlled_values"]["kind"]:
            errors.append(f"{label}: invalid kind {doc.kind!r}")
        for field in required:
            if field not in doc.meta or doc.meta[field] is None:
                errors.append(f"{label}: missing required field {field}")
        for field, choices in schema["controlled_values"].items():
            if field in doc.meta and doc.meta[field] not in choices:
                errors.append(f"{label}: {field}={doc.meta[field]!r} is not controlled")
        if doc.doc_id in ids:
            errors.append(f"{label}: duplicate id {doc.doc_id!r} (also {relative(ids[doc.doc_id])})")
        ids[doc.doc_id] = doc.path

        if doc.kind == "paper":
            if not isinstance(doc.meta.get("authors"), list) or not doc.meta.get("authors"):
                errors.append(f"{label}: authors must be a non-empty list")
            if not isinstance(doc.meta.get("topics"), list):
                errors.append(f"{label}: topics must be a list")
            if not isinstance(doc.meta.get("references"), list):
                errors.append(f"{label}: references must be a list")
            acquired = doc.meta.get("source_acquired") is True
            verified = doc.meta.get("source_verified_against_original") is True
            method = doc.meta.get("source_verification_method")
            if verified and (not acquired or method not in {"codex_audit", "manual_grep", "vision_check"}):
                errors.append(f"{label}: verified source requires acquisition and a real method")
            if not acquired and doc.meta.get("description_last_audit") != "none":
                errors.append(f'{label}: unacquired source requires description_last_audit="none"')
            for forbidden in ("human_read_source", "human_read_at"):
                if forbidden in doc.meta:
                    errors.append(f"{label}: {forbidden} is user-owned and forbidden in paper metadata")

        links = set(normalize_list(doc.meta.get("references"))) | source_paper_keys(doc.meta)
        for key in sorted(links):
            if key and key not in paper_keys:
                errors.append(f"{label}: dangling paper reference {key!r}")

        if doc.kind in {"claim", "concept"} and not doc.meta.get("sources"):
            errors.append(f"{label}: at least one source is required")
        if doc.kind == "claim" and not doc.meta.get("statement"):
            errors.append(f"{label}: empty claim statement")

        if "" in doc.body or re.search(r"turn\d+(?:view|search|academia)\d+", doc.body):
            errors.append(f"{label}: contains private citation marker")

    return errors


def validate_repository_texts() -> list[str]:
    """Reject leaked internal citation tokens outside the card corpus too."""
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SCAN_SUFFIXES:
            continue
        if any(part in TEXT_SCAN_EXCLUDED for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        if "" in text or re.search(r"turn\d+(?:view|search|academia)\d+", text):
            errors.append(f"{relative(path)}: contains private citation marker")
    return errors


def catalog_entry(doc: Document) -> dict[str, Any]:
    authors = normalize_list(doc.meta.get("authors"))
    tags = normalize_list(doc.meta.get("topics"))
    return {
        "id": doc.doc_id,
        "kind": doc.kind,
        "title": doc.title,
        "authors": authors,
        "year": doc.year,
        "date": doc.meta.get("first_publication_date"),
        "publication_status": doc.meta.get("publication_status"),
        "assessment_status": doc.meta.get("assessment_status"),
        "reading_status": doc.meta.get("reading_status"),
        "claim_status": doc.meta.get("claim_status"),
        "corpus_tier": doc.meta.get("corpus_tier"),
        "topics": tags,
        "path": relative(doc.path),
        "body": doc.body,
        "references": normalize_list(doc.meta.get("references")),
        "sources": normalize_list(doc.meta.get("sources")),
        "visibility": doc.meta.get("visibility"),
        "last_checked": str(doc.meta.get("last_checked")),
    }


def write_json_catalog(entries: list[dict[str, Any]], output_dir: Path = INDEX_DIR) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "catalog.json"
    path.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def write_timeline(entries: list[dict[str, Any]], output_dir: Path = INDEX_DIR) -> Path:
    papers = sorted(
        (entry for entry in entries if entry["kind"] == "paper"),
        key=lambda item: (item.get("date") or f"{item.get('year') or 9999}-12-31", item["id"]),
    )
    lines = ["# 文献时间线", "", "> 由 `python scripts/kb.py build` 生成。", ""]
    current_year: int | None = None
    for paper in papers:
        first_date = str(paper.get("date") or "")
        try:
            year = int(first_date[:4])
        except (TypeError, ValueError):
            year = paper.get("year")
        if year != current_year:
            current_year = year
            lines.extend([f"## {year or '年代不明'}", ""])
        author_text = ", ".join(paper.get("authors") or [])
        status = paper.get("publication_status") or "unknown"
        assessment = paper.get("assessment_status") or "unknown"
        published_year = paper.get("year") or "?"
        date_label = first_date or str(published_year)
        lines.append(
            f"- {date_label} · [{paper['title']}](../{paper['path']}) — {author_text}; "
            f"出版年 {published_year}; `{status}` / `{assessment}`"
        )
    lines.append("")
    path = output_dir / "timeline.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_graph(entries: list[dict[str, Any]], output_dir: Path = INDEX_DIR) -> Path:
    papers = {entry["id"]: entry for entry in entries if entry["kind"] == "paper"}
    lines = ["flowchart LR"]
    for key, paper in sorted(papers.items()):
        label = f"{paper.get('year') or '?'} {paper['title']}".replace('"', "'")
        lines.append(f'    {safe_mermaid_id(key)}["{label}"]')
    for key, paper in sorted(papers.items()):
        for cited in paper.get("references", []):
            if cited in papers:
                lines.append(f"    {safe_mermaid_id(key)} --> {safe_mermaid_id(str(cited))}")
    path = output_dir / "citation-graph.mmd"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def safe_mermaid_id(value: str) -> str:
    return "n_" + re.sub(r"[^A-Za-z0-9_]", "_", value)


def write_sqlite(entries: list[dict[str, Any]], output_dir: Path = INDEX_DIR) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "kb.sqlite"
    with tempfile.NamedTemporaryFile(dir=output_dir, suffix=".sqlite", delete=False) as handle:
        temp_path = Path(handle.name)
    try:
        connection = sqlite3.connect(temp_path)
        connection.executescript(
            """
            CREATE TABLE documents (
                id TEXT PRIMARY KEY,
                kind TEXT NOT NULL,
                title TEXT NOT NULL,
                authors TEXT,
                year INTEGER,
                topics TEXT,
                status TEXT,
                path TEXT NOT NULL,
                body TEXT NOT NULL,
                metadata TEXT NOT NULL
            );
            CREATE VIRTUAL TABLE documents_fts USING fts5(
                id UNINDEXED, title, authors, topics, body,
                tokenize='unicode61 remove_diacritics 2'
            );
            """
        )
        for entry in entries:
            authors = " ; ".join(entry.get("authors") or [])
            topics = " ".join(entry.get("topics") or [])
            status = entry.get("assessment_status") or entry.get("claim_status") or entry.get("reading_status")
            metadata = json.dumps(entry, ensure_ascii=False)
            values = (
                entry["id"], entry["kind"], entry["title"], authors, entry.get("year"), topics,
                status, entry["path"], entry.get("body", ""), metadata,
            )
            connection.execute("INSERT INTO documents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
            connection.execute(
                "INSERT INTO documents_fts VALUES (?, ?, ?, ?, ?)",
                (entry["id"], entry["title"], authors, topics, entry.get("body", "")),
            )
        connection.commit()
        connection.close()
        temp_path.replace(destination)
    finally:
        temp_path.unlink(missing_ok=True)
    return destination


def command_validate(_: argparse.Namespace) -> int:
    try:
        documents = list(iter_documents())
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    errors = validate_documents(documents) + validate_repository_texts()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Validation failed: {len(errors)} error(s).")
        return 1
    print(f"Validation passed: {len(documents)} document(s).")
    return 0


def build_all(documents: list[Document], output_dir: Path = INDEX_DIR) -> list[Path]:
    entries = [catalog_entry(doc) for doc in documents]
    entries.sort(key=lambda item: (item["kind"], item.get("date") or "9999-12-31", item["id"]))
    return [
        write_json_catalog(entries, output_dir),
        write_timeline(entries, output_dir),
        write_graph(entries, output_dir),
        write_sqlite(entries, output_dir),
    ]


def command_build(_: argparse.Namespace) -> int:
    documents = list(iter_documents())
    errors = validate_documents(documents) + validate_repository_texts()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    outputs = build_all(documents)
    for output in outputs:
        print(relative(output))
    print(f"Built indexes for {len(documents)} document(s).")
    return 0


def ensure_index() -> None:
    database = INDEX_DIR / "kb.sqlite"
    if not database.exists():
        documents = list(iter_documents())
        errors = validate_documents(documents)
        if errors:
            raise RuntimeError("knowledge base is invalid; run validate")
        build_all(documents)


def command_search(args: argparse.Namespace) -> int:
    ensure_index()
    connection = sqlite3.connect(INDEX_DIR / "kb.sqlite")
    connection.row_factory = sqlite3.Row
    conditions = ["documents_fts MATCH ?", "documents.id = documents_fts.id"]
    parameters: list[Any] = [args.query]
    if args.type:
        conditions.append("documents.kind = ?")
        parameters.append(args.type)
    if args.year_from is not None:
        conditions.append("documents.year >= ?")
        parameters.append(args.year_from)
    if args.year_to is not None:
        conditions.append("documents.year <= ?")
        parameters.append(args.year_to)
    if args.tag:
        conditions.append("documents.topics LIKE ?")
        parameters.append(f"%{args.tag}%")
    query = f"""
        SELECT documents.*, bm25(documents_fts) AS score,
               snippet(documents_fts, 4, '[', ']', ' … ', 24) AS excerpt
        FROM documents_fts, documents
        WHERE {' AND '.join(conditions)}
        ORDER BY score, documents.year, documents.id
        LIMIT ?
    """
    parameters.append(args.limit)
    try:
        rows = connection.execute(query, parameters).fetchall()
    except sqlite3.OperationalError as exc:
        print(f"Invalid FTS query: {exc}", file=sys.stderr)
        return 2
    finally:
        connection.close()
    for row in rows:
        year = row["year"] if row["year"] is not None else "?"
        print(f"{row['id']}\t{row['kind']}\t{year}\t{row['title']}\t{row['path']}")
        if row["excerpt"]:
            print(f"  {row['excerpt'].replace(chr(10), ' ')}")
    print(f"{len(rows)} result(s).")
    return 0


def command_status(_: argparse.Namespace) -> int:
    documents = list(iter_documents())
    kinds = Counter(doc.kind for doc in documents)
    papers = [doc for doc in documents if doc.kind == "paper"]
    by_reading = Counter(str(doc.meta.get("reading_status")) for doc in papers)
    by_tier = Counter(str(doc.meta.get("corpus_tier")) for doc in papers)
    by_publication = Counter(str(doc.meta.get("publication_status")) for doc in papers)
    by_assessment = Counter(str(doc.meta.get("assessment_status")) for doc in papers)
    print(f"documents={len(documents)} papers={kinds['paper']} claims={kinds['claim']} concepts={kinds['concept']}")
    print("corpus_tier=" + json.dumps(dict(sorted(by_tier.items())), ensure_ascii=False))
    print("reading_status=" + json.dumps(dict(sorted(by_reading.items())), ensure_ascii=False))
    print("publication_status=" + json.dumps(dict(sorted(by_publication.items())), ensure_ascii=False))
    print("assessment_status=" + json.dumps(dict(sorted(by_assessment.items())), ensure_ascii=False))
    blocked = [doc.doc_id for doc in papers if doc.meta.get("reading_status") == "source_blocked"]
    queued = [doc.doc_id for doc in papers if doc.meta.get("reading_status") in {"queued", "metadata_verified"}]
    print("source_blocked=" + (", ".join(blocked) if blocked else "none"))
    print("remaining=" + (", ".join(queued) if queued else "none"))
    return 0


def copy_public_document(doc: Document, destination_root: Path) -> None:
    if doc.meta.get("visibility") != "public":
        return
    destination = destination_root / relative(doc.path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    text = doc.path.read_text(encoding="utf-8")
    if any(marker in text for marker in PRIVATE_MARKERS):
        raise RuntimeError(f"private marker in public document: {relative(doc.path)}")
    destination.write_text(text, encoding="utf-8")


def command_publish(_: argparse.Namespace) -> int:
    documents = list(iter_documents())
    errors = validate_documents(documents) + validate_repository_texts()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    with tempfile.TemporaryDirectory(dir=ROOT, prefix=".public-") as temp:
        staging = Path(temp)
        for name in ("README.md", "研究进展综述.md"):
            source = ROOT / name
            if source.exists():
                shutil.copy2(source, staging / name)
        for doc in documents:
            copy_public_document(doc, staging)
        bibliography_target = staging / "bibliography"
        bibliography_target.mkdir(parents=True, exist_ok=True)
        for name in ("library.bib", "candidates.yaml", "search-protocol.md", "search-log.md"):
            source = ROOT / "bibliography" / name
            if source.exists():
                shutil.copy2(source, bibliography_target / name)
        reproduction_target = staging / "reproductions"
        reproduction_target.mkdir(parents=True, exist_ok=True)
        for name in ("README.md", "esc_reproduce.py", "results.json"):
            source = ROOT / "reproductions" / name
            if source.exists():
                shutil.copy2(source, reproduction_target / name)
        public_index = staging / "index"
        build_all([doc for doc in documents if doc.meta.get("visibility") == "public"], public_index)
        for path in staging.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SCAN_SUFFIXES | {".py", ".json"}:
                continue
            text = path.read_text(encoding="utf-8")
            marker = next((item for item in PRIVATE_MARKERS if item in text), None)
            if marker:
                raise RuntimeError(f"private marker {marker!r} in public file {path.relative_to(staging)}")
            if "" in text or re.search(r"turn\d+(?:view|search|academia)\d+", text):
                raise RuntimeError(f"private citation marker in public file {path.relative_to(staging)}")
        replacement = ROOT / ".public-ready"
        if replacement.exists():
            shutil.rmtree(replacement)
        shutil.copytree(staging, replacement)
    old = ROOT / ".public-old"
    if old.exists():
        shutil.rmtree(old)
    if PUBLIC_DIR.exists():
        PUBLIC_DIR.replace(old)
    replacement.replace(PUBLIC_DIR)
    if old.exists():
        shutil.rmtree(old)
    print(f"Published to {relative(PUBLIC_DIR)}/")
    return 0


def fetch_json(url: str, timeout: int = 20) -> Any:
    request = urllib.request.Request(url, headers={"User-Agent": "erdos-straus-kb/1.0 (research)"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def known_external_ids(documents: list[Document]) -> tuple[set[str], set[str]]:
    dois: set[str] = set()
    arxiv_ids: set[str] = set()
    for doc in documents:
        if doc.kind != "paper":
            continue
        if doc.meta.get("doi"):
            dois.add(str(doc.meta["doi"]).lower())
        if doc.meta.get("arxiv"):
            arxiv_ids.add(str(doc.meta["arxiv"]).lower())
    return dois, arxiv_ids


def command_monitor(args: argparse.Namespace) -> int:
    documents = list(iter_documents())
    dois, arxiv_ids = known_external_ids(documents)
    since = args.since or str(dt.date.today() - dt.timedelta(days=365))
    candidates: dict[str, dict[str, Any]] = {}
    errors: list[str] = []

    openalex_params = urllib.parse.urlencode(
        {
            "search": '"Erdos Straus"',
            "filter": f"from_publication_date:{since}",
            "per-page": 100,
            "select": "id,doi,display_name,publication_year,publication_date,authorships,primary_location",
        }
    )
    try:
        payload = fetch_json(f"https://api.openalex.org/works?{openalex_params}")
        for item in payload.get("results", []):
            title = item.get("display_name") or ""
            if "straus" not in title.lower() and "erdős" not in title.lower() and "erdos" not in title.lower():
                continue
            doi = (item.get("doi") or "").removeprefix("https://doi.org/").lower()
            if doi and doi in dois:
                continue
            key = doi or item.get("id") or title
            candidates[key] = {
                "title": title,
                "date": item.get("publication_date"),
                "doi": doi or None,
                "provider": "OpenAlex",
                "url": item.get("id"),
            }
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        errors.append(f"OpenAlex: {exc}")

    s2_params = urllib.parse.urlencode(
        {
            "query": "Erdos Straus conjecture",
            "limit": 100,
            "fields": "title,year,publicationDate,externalIds,url",
        }
    )
    try:
        payload = fetch_json(f"https://api.semanticscholar.org/graph/v1/paper/search?{s2_params}")
        for item in payload.get("data", []):
            date = item.get("publicationDate") or f"{item.get('year') or 0}-01-01"
            if date < since:
                continue
            external = item.get("externalIds") or {}
            doi = str(external.get("DOI") or "").lower()
            arxiv = str(external.get("ArXiv") or "").lower()
            if (doi and doi in dois) or (arxiv and arxiv in arxiv_ids):
                continue
            key = doi or arxiv or item.get("paperId") or item.get("title")
            candidates[key] = {
                "title": item.get("title"),
                "date": date,
                "doi": doi or None,
                "arxiv": arxiv or None,
                "provider": "Semantic Scholar",
                "url": item.get("url"),
            }
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        errors.append(f"Semantic Scholar: {exc}")

    print(json.dumps(sorted(candidates.values(), key=lambda item: (item.get("date") or "", item.get("title") or "")), ensure_ascii=False, indent=2))
    for error in errors:
        print(f"WARNING: {error}", file=sys.stderr)
    print(f"candidate_count={len(candidates)} since={since}")
    return 0 if not errors or candidates else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="validate schemas, references, and markers").set_defaults(func=command_validate)
    subparsers.add_parser("build", help="rebuild JSON, Markdown, Mermaid, and SQLite indexes").set_defaults(func=command_build)
    subparsers.add_parser("status", help="show corpus and reading status").set_defaults(func=command_status)
    subparsers.add_parser("publish", help="build the public-only knowledge base").set_defaults(func=command_publish)

    search = subparsers.add_parser("search", help="full-text search the knowledge base")
    search.add_argument("query")
    search.add_argument("--type", choices=["paper", "claim", "concept"])
    search.add_argument("--year-from", type=int)
    search.add_argument("--year-to", type=int)
    search.add_argument("--tag")
    search.add_argument("--limit", type=int, default=20)
    search.set_defaults(func=command_search)

    monitor = subparsers.add_parser("monitor", help="query current literature providers")
    monitor.add_argument("--since", help="ISO date; defaults to one year ago")
    monitor.set_defaults(func=command_monitor)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
