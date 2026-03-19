# VaultBeacon Sentinel

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-Lido-VaultMonitor
- **Primary track:** Lido Vault Position Monitor + Alert Agent
- **Overlap targets:** Venice Private Agents, ENS, Bankr Gateway, Filecoin, OpenServ
- **Primary contract:** VaultAlertRegistry
- **Primary operator module:** vault_monitor
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

A monitoring agent that tracks vault allocations, benchmark yield shifts, and operator thresholds, then emits plain-language alerts and MCP-callable responses.

## Track evidence

- `artifacts/onchain_intents/lido_vault_monitor_vault_alert.json`
- `artifacts/onchain_intents/ens_ens_publish.json`
- `artifacts/filecoin/0x279e5946ecc0c673a483cdc1b222c4561d46b32c9706c1ca3a33f14d108613aa.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "VaultBeacon Sentinel",
  "track": "Lido Vault Position Monitor + Alert Agent",
  "plan_id": "0x279e5946ecc0c673a483cdc1b222c4561d46b32c9706c1ca3a33f14d108613aa",
  "simulation_hash": "0x40815574f0adc7672759de7fd99fe926d36d1fd8635198bee9c039a37b4d24c8",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/lido_vault_monitor_vault_alert.json",
    "artifacts/onchain_intents/ens_ens_publish.json",
    "artifacts/filecoin/0x279e5946ecc0c673a483cdc1b222c4561d46b32c9706c1ca3a33f14d108613aa.json"
  ],
  "partner_statuses": {
    "Lido Vault Monitor": "prepared_contract_call",
    "Venice": "awaiting_credentials",
    "ENS": "prepared_contract_call",
    "Bankr Gateway": "awaiting_credentials",
    "Filecoin": "prepared_filecoin_bundle",
    "OpenServ": "awaiting_credentials"
  },
  "created_at": "2026-03-19T03:52:13+00:00"
}
```
