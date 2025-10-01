import os
from pathlib import Path

from insiders import GitHub, update_sponsors_file, update_numbers_file


GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
TEAM = "dlvhdr-insiders/insiders"
MIN_AMOUNT = 5

beneficiaries = {
    "github": {
    },
}

include_users = {
    "dlvhdr",  # Myself.
}

exclude_users = {
}


def main():
    with GitHub(GITHUB_TOKEN) as github:
        sponsors = github.get_sponsors()
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
