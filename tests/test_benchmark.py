import json

import pytest

from benchmarks.evaluate import evaluate, load_cases


def test_exact_match_required_for_both_type_and_span():
    cases = [{
        "id": "exact", "country": "MX", "text": "abcdef",
        "entities": [{"type": "RFC", "start": 0, "end": 6}],
    }]
    for finding in [("CURP", 0, 6), ("RFC", 0, 5)]:
        results, errors = evaluate(cases, lambda text: [finding])
        assert results["total"] == {
            "tp": 0, "fp": 1, "fn": 1, "precision": 0.0, "recall": 0.0, "f1": 0.0
        }
        assert errors == [{"id": "exact", "fp": [finding], "fn": [("RFC", 0, 6)]}]


def test_missing_detections_are_reported_by_entity_and_country():
    cases = [{
        "id": "missing", "country": "BO", "text": "12345",
        "entities": [{"type": "CI_BO", "start": 0, "end": 5}],
    }]
    results, _ = evaluate(cases, lambda text: [])
    for group in ("total", "country/BO", "entity/CI_BO", "country/BO/entity/CI_BO"):
        assert results[group]["fn"] == 1
        assert results[group]["precision"] is None
        assert results[group]["recall"] == 0.0


def test_negative_only_country_preserved_with_undefined_metrics():
    results, errors = evaluate(
        [{"id": "negative", "country": "MX", "text": "pedido", "entities": []}],
        lambda text: [],
    )
    assert results["country/MX"] == {
        "tp": 0, "fp": 0, "fn": 0, "precision": None, "recall": None, "f1": None
    }
    assert errors == []


def test_mixed_results_use_micro_averages_and_separate_countries():
    cases = [
        {"id": "mx", "country": "MX", "text": "ab", "entities": [
            {"type": "RFC", "start": 0, "end": 1}
        ]},
        {"id": "bo", "country": "BO", "text": "cd", "entities": [
            {"type": "CI_BO", "start": 0, "end": 1}
        ]},
    ]
    predictions = {"ab": [("RFC", 0, 1), ("EMAIL", 1, 2), ("NIT", 0, 2)], "cd": []}
    results, errors = evaluate(cases, predictions.__getitem__)
    assert results["total"] == {
        "tp": 1, "fp": 2, "fn": 1,
        "precision": pytest.approx(1 / 3), "recall": 0.5, "f1": 0.4,
    }
    assert results["country/MX"]["tp"] == 1
    assert results["country/MX"]["fn"] == 0
    assert results["country/BO"]["tp"] == 0
    assert results["country/BO"]["fn"] == 1
    assert len(errors) == 2


@pytest.mark.parametrize("entities", [
    [{"type": "RFC", "start": -1, "end": 3}],
    [{"type": "RFC", "start": 0, "end": 9}],
    [{"type": "RFC", "start": 1, "end": 1}],
    [{"type": "RFC", "start": 0, "end": 3}, {"type": "CURP", "start": 2, "end": 4}],
])
def test_invalid_labels_rejected(entities):
    data = json.dumps({"id": "bad", "text": "abcd", "entities": entities}).encode()
    with pytest.raises(ValueError, match="span"):
        load_cases(data)


def test_duplicate_case_ids_rejected():
    row = json.dumps({"id": "same", "text": "abcd", "entities": []})
    with pytest.raises(ValueError, match="Duplicate"):
        load_cases((row + "\n" + row).encode())
