"""Project-specific context for VaultBeacon Sentinel."""

        from __future__ import annotations

        PROJECT_CONTEXT = {
    "project_name": "VaultBeacon Sentinel",
    "track": "Lido Vault Position Monitor + Alert Agent",
    "pitch": "A monitoring agent that tracks vault allocations, benchmark yield shifts, and operator thresholds, then emits plain-language alerts and MCP-callable responses.",
    "overlap_targets": [
        "Venice Private Agents",
        "ENS",
        "Bankr Gateway",
        "Filecoin",
        "OpenServ"
    ],
    "goals": [
        "discover a bounded opportunity",
        "plan a dry-run-first action",
        "verify receipts and proofs"
    ]
}


        def seed_targets() -> list[str]:
            """Return the first batch of overlap targets for planning."""
            return list(PROJECT_CONTEXT['overlap_targets'])
