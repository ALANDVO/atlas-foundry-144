# SYNC History

This file tracks sync history from current source code tree, NOT cleaned-room reimplementation.

## Sync Operations

### License Structure Migration
- Added `LICENSES/` directory with AGPL-3.0-only, GPL-3.0, Apache-2.0
- Updated `LICENSE` to MIT with Alan Vo copyright
- Created `LICENSES/README.md` for license overview

### Model Availability Endpoints
- Added model configs for DeepSeek V4.1 Flash, Kimi K3, GLM 5.3 Flash
- Created `/models` endpoint for listing free models
- Created `/v1/{provider}/chat` proxy endpoint

### Documentation
- Updated README with model availability information
- Added contact footer with alanvo.net and X profile

## Notes
- Source history preserved from current code tree
- Not a clean-room reimplementation
- FCC, local, and RTK correspondence preserved where applicable
