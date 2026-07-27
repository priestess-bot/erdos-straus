import importlib.util
import argparse
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("kb", ROOT / "scripts" / "kb.py")
assert SPEC and SPEC.loader
kb = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = kb
SPEC.loader.exec_module(kb)


class KnowledgeBaseTests(unittest.TestCase):
    def test_documents_validate(self):
        documents = list(kb.iter_documents())
        self.assertEqual(kb.validate_documents(documents), [])

    def test_document_ids_are_unique(self):
        ids = [document.doc_id for document in kb.iter_documents()]
        self.assertEqual(len(ids), len(set(ids)))

    def test_build_outputs(self):
        documents = list(kb.iter_documents())
        with tempfile.TemporaryDirectory() as directory:
            outputs = kb.build_all(documents, Path(directory))
            self.assertTrue(all(path.exists() for path in outputs))

    def test_overview_has_no_private_citation_markers(self):
        text = (ROOT / "研究进展综述.md").read_text(encoding="utf-8")
        self.assertNotIn("", text)

    def test_malformed_qquad_is_rejected(self):
        self.assertIsNotNone(kb.MALFORMED_LATEX_RE.search(r"x=1,qquad y=2"))
        self.assertIsNone(kb.MALFORMED_LATEX_RE.search(r"x=1,\qquad y=2"))

    def test_chinese_substring_search_fallback(self):
        output = io.StringIO()
        args = argparse.Namespace(
            query="研究路线",
            type="concept",
            year_from=None,
            year_to=None,
            tag=None,
            limit=20,
        )
        with contextlib.redirect_stdout(output):
            result = kb.command_search(args)
        self.assertEqual(result, 0)
        self.assertIn("research-directions-and-proof-gap", output.getvalue())

    def test_hyphenated_id_search_falls_back_to_literal_match(self):
        output = io.StringIO()
        args = argparse.Namespace(
            query="gap-three-two-denominator",
            type="claim",
            year_from=None,
            year_to=None,
            tag=None,
            limit=20,
        )
        with contextlib.redirect_stdout(output):
            result = kb.command_search(args)
        self.assertEqual(result, 0)
        self.assertIn("gap-three-two-denominator-lift-obstruction", output.getvalue())


if __name__ == "__main__":
    unittest.main()
