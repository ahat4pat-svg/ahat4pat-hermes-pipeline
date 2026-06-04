"""
hermes/agent.py — Hermès Agent entry point (scaffold only)

This is the orchestrator entry point. Real implementation pending.

Hermès Agent (NousResearch/hermes-agent) framework :
- composition d'agents (specialist delegation)
- function-calling JSON typé
- mémoire multi-couches (FTS5 + résumés LLM persistants)
- topologie Swarm pour parallel execution

License: MIT (Hermès framework). 140k GitHub stars.
"""

import os
from pathlib import Path
from typing import Optional


# ===== Scaffold placeholder =====
class HermesAgentScaffold:
    """
    Placeholder class — real Hermès Agent SDK integration pending.
    Clone official SDK : https://github.com/mz2/hermes-agent-sdk
    """

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.memory_path = project_root / "memory.md"
        self.project_json_path = project_root / "project.json"

    def load_memory(self) -> str:
        """Load global lexicon + verrouillage architectural."""
        return self.memory_path.read_text() if self.memory_path.exists() else ""

    def delegate_to_tl(self, tl_id: str, task: str) -> dict:
        """
        Délègue une tâche à un Team Leader sub-agent.

        tl_id ∈ {tl-faceless-yt, tl-juniors4pat, tl-freelance,
                 tl-voice-services, tl-kdp-newsletter, tl-musique}
        """
        tl_path = self.project_root / "tls" / tl_id
        if not tl_path.exists():
            raise ValueError(f"Unknown TL: {tl_id}")

        # TODO: real Hermès delegation
        return {"status": "scaffold_placeholder", "tl_id": tl_id, "task": task}

    def run(self, command: str) -> None:
        """Main entry point. To be implemented."""
        raise NotImplementedError(
            "Hermès Agent run loop scaffold only. "
            "Clone SDK and implement: https://github.com/mz2/hermes-agent-sdk"
        )


# ===== CLI usage =====
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python hermes/agent.py <command>", file=sys.stderr)
        sys.exit(1)

    agent = HermesAgentScaffold(project_root=Path(__file__).parent.parent)
    agent.run(sys.argv[1])
