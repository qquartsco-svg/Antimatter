"""
Guard against wrong-file uploads (e.g. contracts/__init__ swapped with another engine).

This repo's canonical contracts define Antimatter* dataclasses; imports must succeed.
"""
from __future__ import annotations

import importlib
import inspect


def test_contracts_module_defines_antimatter_dataclasses() -> None:
    from antimatter_phenomenology import contracts as c

    assert c.AntimatterInventory.__module__ == "antimatter_phenomenology.contracts"
    assert c.AntimatterConfinementContext.__module__ == "antimatter_phenomenology.contracts"
    assert c.AntimatterAsymmetryContext.__module__ == "antimatter_phenomenology.contracts"
    assert c.AntimatterFoundationReport.__module__ == "antimatter_phenomenology.contracts"
    assert c.AntimatterDomain.PHENOMENOLOGY.value == "phenomenology"

    src = inspect.getsource(c)
    assert "class AntimatterInventory" in src
    assert "class AntimatterFoundationReport" in src


def test_root_init_exports_match_readme_entrypoint() -> None:
    import antimatter_phenomenology as ap

    assert ap.__version__
    for name in (
        "assess_antimatter_foundation",
        "AntimatterInventory",
        "AntimatterConfinementContext",
        "AntimatterAsymmetryContext",
        "AntimatterAssessmentStage",
        "assess_trap_transport",
        "assess_rarity_foundation",
        "screen_claim",
    ):
        assert hasattr(ap, name), f"missing top-level export: {name}"
    init_src = inspect.getsource(importlib.import_module("antimatter_phenomenology.__init__"))
    assert "memory_engine" not in init_src
    assert "SNN" not in init_src


def test_foundation_import_chain() -> None:
    """foundation.py must resolve contracts from this package only."""
    from antimatter_phenomenology.foundation import assess_antimatter_foundation

    assert callable(assess_antimatter_foundation)
