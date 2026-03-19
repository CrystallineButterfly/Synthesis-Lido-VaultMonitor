# Live readiness

- **Project:** VaultBeacon Sentinel
- **Track:** Lido Vault Position Monitor + Alert Agent
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:13+00:00`

## Trust boundaries

- **Lido Vault Monitor** — `contract_call` — Monitor vault state and anchor alert digests.
- **Venice** — `rest_json` — Run private reasoning over sensitive inputs.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.
- **Bankr Gateway** — `rest_json` — Route inference through cost-aware model selection.
- **Filecoin** — `file_upload` — Persist proofs, logs, and evidence bundles offchain.
- **OpenServ** — `rest_json` — Dispatch jobs and expose swarm service endpoints.

## Offline-ready partner paths

- **Lido Vault Monitor** — prepared_contract_call
- **ENS** — prepared_contract_call
- **Filecoin** — prepared_filecoin_bundle

## Live-only partner blockers

- **Venice**: VENICE_API_KEY, VENICE_CHAT_COMPLETIONS_URL, VENICE_MODEL — https://docs.venice.ai/
- **Bankr Gateway**: BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/
- **OpenServ**: OPENSERV_API_KEY, OPENSERV_AGENT_URL — https://docs.openserv.ai/

## Highest-sensitivity actions

- `venice_private_analysis` — Venice — Use Venice for a bounded action in this repo.
- `bankr_gateway_compute_route` — Bankr Gateway — Use Bankr Gateway for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for VaultAlertRegistry.
- Run python3 scripts/run_agent.py to produce a dry run for vault_monitor.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
