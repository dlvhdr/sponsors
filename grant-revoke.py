import os
from pathlib import Path

from insiders import GitHub, Polar, update_sponsors_file, update_numbers_file


GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
POLAR_TOKEN = os.environ["POLAR_TOKEN"]
TEAM = "dlvhdr-insiders/insiders"
MIN_AMOUNT = 10

beneficiaries = {
    "github": {
    },
}

include_users = {
    "dlvhdr",  # Myself.
}

exclude_users = {
    "medecau",  # Doesn't want to join the team.
}


def main():
    with GitHub(GITHUB_TOKEN) as github, Polar(POLAR_TOKEN) as polar:
        sponsors = github.get_sponsors() + polar.get_sponsors()
        github.consolidate_beneficiaries(sponsors, beneficiaries)  # type: ignore[arg-type]
        github.sync_team(
            TEAM,
            sponsors=sponsors,
            min_amount=MIN_AMOUNT,
            include_users=include_users,
            exclude_users=exclude_users,
        )

    update_numbers_file(sponsors.sponsorships, filepath=Path("numbers.json"))
    update_sponsors_file(sponsors.sponsorships, filepath=Path("sponsors.json"), exclude_private=True)


if __name__ == "__main__":
    raise SystemExit(main())
