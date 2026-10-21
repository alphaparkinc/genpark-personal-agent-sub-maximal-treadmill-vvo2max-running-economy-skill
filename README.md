# Sub-Maximal Treadmill Running Economy & vVO2max Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Sub-maximal running economy oxygen cost (ml O2/kg/km), velocity at VO2max (vVO2max), and marathon finishing time prediction. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_running_economy_and_vvo2max`: Compute running economy and velocity at VO2 max (vVO2max km/h) from treadmill oxygen uptake telemetry.
- `predict_marathon_finish_time`: Predict marathon finish time based on vVO2max and fractional aerobic utilization (80-85%).

## 🚀 Installation & Usage
```bash
python -m genpark_personal_agent_sub_maximal_treadmill_vvo2max_running_economy_skill.server --test
```
