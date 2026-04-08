# Hey Cindy Project Log

##### 2026-02-21 — Environment Stabilization & Local Pipeline Refactor #####
# 🔧 Infrastructure Cleanup
- Rebuilt Python virtual environment to resolve dependency inconsistencies
- Standardized runtime to Python 3.11 for compatibility and stability
- Resolved interpreter conflicts between system Python and venv

# 🧩 Local Pipeline Validation
- Verified full wake word → speech recognition → command parsing → execution pipeline
- Confirmed stable audio capture using sounddevice
- Ensured consistent command parsing behavior using regex patterns

# 🛠 System Reliability Improvements
- Added support for "quit" command to allow graceful shutdown
- Identified and resolved local port conflict issue (5050) during Flask light server execution

# 🧠 Engineering Insights
- Importance of controlled runtime environments
- Managing local service ports to prevent collision
- Structured debugging of multi-stage pipelines
- Separation between detection, parsing, and execution layers

--------------------------------------------------------------------------------

##### 2026-02-22 — Cloud Architecture & Persistence Upgrade #####

# 🚀 Major Achievements
- Deployed FastAPI backend to AWS EC2 (Ubuntu)
- Configured Security Groups and public access
- Implemented Bearer Token authentication
- Built local agent → cloud API integration
- Added SQLite persistence layer
- Implemented state recovery after service restart
- Deployed as systemd service (auto-restart + auto-start on boot)
- Built local dashboard with real-time state sync

# 🏗 Architecture Evolution
Before:
Local-only execution, state stored in memory.

After:
Distributed architecture:
- Local voice agent
- Cloud API on EC2
- Persistent SQLite storage
- systemd-managed service
- Web dashboard for monitoring

# 🧠 Engineering Concepts Learned
- EC2 provisioning and SSH
- Linux process management
- Security Group networking
- HTTP + REST API design
- Token-based authentication
- Persistence vs in-memory state
- Service lifecycle management (systemd)
- Recovery after restart

# 🧪 Testing & Validation
- Verified database writes
- Confirmed state persistence after restart
- Validated auto-restart using systemctl
- Confirmed dashboard sync with cloud state

# 🎯 Reflection
Today marked the transition from a local script to a cloud-deployed distributed system.

--------------------------------------------------------------------------------
##### 2026-02-24 — Observability & Network Debug Upgrade ##### 

# 🚀 Major Achievements
- Resolved SSH timeout by debugging Security Group IP restrictions
- Updated inbound rules to support campus-wide access (128.54.0.0/16)
- Implemented /metrics endpoint for system observability
- Added command aggregation via SQLite (total / on / off counts)
- Implemented uptime tracking for cloud service
- Verified full public cloud access from local client
- Validated token-protected metrics endpoint
- Confirmed production-level public API availability

# 🏗 Architecture Evolution
Before:
Cloud API functional but opaque. No system-level monitoring.
Network access fragile due to single-IP restriction.

After:
Cloud service with structured observability:
- /metrics telemetry endpoint
- Command aggregation via database queries
- Uptime tracking
- Stable campus-wide SSH + API access
- Clear separation of client vs server execution context

System now includes:
- Local voice agent
- Cloud FastAPI backend
- SQLite persistence
- systemd-managed service
- Public REST endpoints
- Metrics monitoring layer

# 🧠 Engineering Concepts Learned
- Deep SSH debugging using verbose flags (ssh -vvv)
- Security Group IP scoping and network boundaries
- Public IP changes in NAT environments
- Client vs server request path distinction
- Observability design for backend services
- SQL aggregation queries for telemetry
- Service verification across network layers
- Production-style endpoint validation workflow

# 🧪 Testing & Validation
- Confirmed SSH restoration after Security Group fix
- Verified /health from both server and local client
- Validated /metrics with Bearer authentication
- Confirmed accurate aggregation of command history
- Verified uptime calculation increments correctly
- Ensured public endpoint accessible from campus network

# 🎯 Reflection
Today marked the transition from a “working cloud service” to a monitored and production-aware system.

The project now supports:
- Stable remote access
- Security-aware networking
- Runtime observability
- Verified external client communication

This was a shift from feature-building to infrastructure-level engineering.

--------------------------------------------------------------------------------

##### 2026-05-02 — Dashboard Toggle & API Contract Fix ##### 

# 🚀 Major Achievements
Added dashboard Toggle action (cloud state read + inverse dispatch)
Fixed frontend/backend JSON mismatch (cmd → text)
Resolved DOM id inconsistency (light vs status)
Restored proper JS execution inside <script> block
Enabled dynamic UI state styling (on / off)

# 🏗 Architecture Update
Standardized command payload schema
Confirmed end-to-end flow:
Browser → Flask → Cloud API → SQLite → UI refresh
Ensured dashboard actions properly persist to cloud

# 🧪 Validation
Verified ON / OFF / TOGGLE all function correctly
Confirmed real-time UI sync with cloud state
No regression to existing persistence layer

--------------------------------------------------------------------------------