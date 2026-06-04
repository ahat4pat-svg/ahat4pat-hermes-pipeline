"""
overseer/patou_overseer.py — Patou-Overseer watchdog (scaffold)

Surveille 7 sources (Claude director + 6 TLs) indépendamment.
Alerte Pat DIRECTEMENT via Telegram si dérive (pas via Claude — pas de boucle fermée).

Cron schedule : 09:00 + 20:00 par défaut.
Mode DRY_RUN=1 par défaut (log only, pas de Telegram send).

Real implementation pending. Scaffold only.
"""

import os
import json
import sys
from pathlib import Path
from typing import Dict, Any


# ===== Config loading =====
def load_targets(targets_path: Path) -> Dict[str, Any]:
    """Load Patou targets from JSON config."""
    if not targets_path.exists():
        raise FileNotFoundError(f"targets.json missing: {targets_path}")
    return json.loads(targets_path.read_text())


def get_env_or_fail(var_name: str) -> str:
    """Read env var, fail if missing."""
    value = os.getenv(var_name)
    if not value:
        raise RuntimeError(f"Required env var missing: {var_name}")
    return value


# ===== Scan placeholder =====
def scan_target(target: Dict[str, Any], dry_run: bool = True) -> Dict[str, Any]:
    """
    Scan a single target.

    target = dict from targets.json["targets"]
    Returns scan result dict.

    Real implementation pending.
    """
    result = {
        "target_name": target.get("name"),
        "target_type": target.get("type"),
        "status": "scaffold_placeholder",
        "checks_ran": [],
        "alerts_triggered": [],
    }
    # TODO: implement each check method per target schema
    return result


def alert_pat(message: str, dry_run: bool = True) -> None:
    """Send alert to Pat via Telegram (or log if dry_run)."""
    if dry_run:
        print(f"[DRY_RUN] Would send to Pat: {message}", file=sys.stderr)
        return

    # TODO: real Telegram send via TELEGRAM_BOT_TOKEN_PATOU + TELEGRAM_CHAT_ID_PAT
    raise NotImplementedError("Telegram send not yet implemented")


# ===== Main run loop =====
def run_scan(targets_path: Path, dry_run: bool = True) -> None:
    """Main scan loop. Called by cron at 09:00 + 20:00."""
    config = load_targets(targets_path)
    results = []

    for target in config.get("targets", []):
        result = scan_target(target, dry_run=dry_run)
        results.append(result)
        if result.get("alerts_triggered"):
            for alert in result["alerts_triggered"]:
                alert_pat(alert, dry_run=dry_run)

    print(f"✓ Scan complete. {len(results)} targets checked. dry_run={dry_run}")


if __name__ == "__main__":
    targets_path = Path(__file__).parent / "targets.json"
    dry_run = os.getenv("DRY_RUN", "1") == "1"
    run_scan(targets_path, dry_run=dry_run)
