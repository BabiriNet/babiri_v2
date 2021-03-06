""" Models for the storage layer """
from typing import List
from utils.constants import (
    TEAM_SIZE,
)
from utils.base_logger import logger


class PokemonTeam:
    """Model for teams in Pokémon Team Snapshots"""

    def __init__(
        self,
        pokemon_roster: List[str] = None,
        rating: int = 0,
        replay_upload_date: str = "1970-01-1970",
    ):
        self.pokemon_roster = [] if pokemon_roster is None else pokemon_roster
        self.rating = rating
        self.replay_upload_date = replay_upload_date

    def set_pokemon_roster(self, pokemon_roster: List[str]) -> None:
        """Set Pokémon list"""
        if len(pokemon_roster) > TEAM_SIZE:
            logger.warning(f"Cannot set roster, roster limited to {TEAM_SIZE}")
        else:
            self.pokemon_roster = pokemon_roster

    def add_pokemon(self, pokemon: str) -> None:
        """Add Pokémon to Pokémon roster"""
        if len(self.pokemon_roster) > TEAM_SIZE - 1:
            logger.warning(f"Cannot add Pokémon ({pokemon}), team roster already full")
        elif pokemon in self.pokemon_roster:
            logger.warning(f"Cannot add Pokémon ({pokemon}), already in team roster")
        else:
            self.pokemon_roster.append(pokemon)

    def get_pokemon_roster(self) -> List[str]:
        """Get Pokémon list"""
        return self.pokemon_roster

    def set_rating(self, rating: int) -> None:
        """Set rating"""
        self.rating = rating

    def get_rating(self) -> int:
        """Get rating"""
        return self.rating

    def set_replay_upload_date(self, replay_upload_date: str) -> None:
        """Set replay upload date"""
        self.replay_upload_date = replay_upload_date

    def get_replay_upload_date(self) -> str:
        """Get replay upload date"""
        return self.replay_upload_date


class PokemonTeamsSnapshot:
    """Model for Pokémon Team Snapshots"""

    def __init__(
        self,
        date: str = "1970-01-01",
        format_id: str = "",
        pokemon_team_list: List[PokemonTeam] = None,
    ):
        self.date = date
        self.format_id = format_id
        self.pokemon_team_list = [] if pokemon_team_list is None else pokemon_team_list

    def set_date(self, date: str) -> None:
        """Set date"""
        self.date = date

    def get_date(self) -> str:
        """Get date"""
        return self.date

    def set_format_id(self, format_id: str) -> None:
        """Set format ID"""
        self.format_id = format_id

    def get_format_id(self) -> str:
        """Get format ID"""
        return self.format_id

    def set_pokemon_team_list(self, pokemon_team_list: List[PokemonTeam]) -> None:
        """Set pokemon team list"""
        self.pokemon_team_list = pokemon_team_list

    def get_pokemon_team_list(self) -> List[PokemonTeam]:
        """Get pokemon team list"""
        return self.pokemon_team_list

    def make_model(self) -> dict:
        """Generate model for database as dictionary"""
        return {
            "Date": self.get_date(),
            "FormatId": self.get_format_id(),
            "Teams": [
                {
                    "PokemonRoster": team.get_pokemon_roster(),
                    "Rating": team.get_rating(),
                    "ReplayUploadDate": team.get_replay_upload_date(),
                }
                for team in self.get_pokemon_team_list()
            ],
        }


class PokemonUsageSnapshot:
    """Model for Pokémon Usage Snapshot"""

    def __init__(
        self,
        date: str = "1970-01-01",
        format_id: str = "",
        pokemon_usage: dict = None,
        pokemon_partner_usage: dict = None,
        pokemon_average_rating_usage: dict = None,
    ):
        self.date = date
        self.format_id = format_id
        # {Pokémon -> number of apperances}
        self.pokemon_usage = {} if pokemon_usage is None else pokemon_usage
        # {Pokémon -> {partner -> number of apperances}}
        self.pokemon_partner_usage = (
            {} if pokemon_partner_usage is None else pokemon_partner_usage
        )
        # {Pokémon -> average rating}
        self.pokemon_average_rating_usage = (
            {} if pokemon_average_rating_usage is None else pokemon_average_rating_usage
        )

    def set_date(self, date: str) -> None:
        """Set date"""
        self.date = date

    def get_date(self) -> str:
        """Get date"""
        return self.date

    def set_format_id(self, format_id: str) -> None:
        """Set format ID"""
        self.format_id = format_id

    def get_format_id(self) -> str:
        """Get format ID"""
        return self.format_id

    def set_pokemon_usage(self, pokemon: str, usage: int) -> None:
        """Set Pokémon usage"""
        if pokemon in self.pokemon_usage:
            logger.warning(f"Pokémon ({pokemon}) already in Pokémon usage, cannot set")
        else:
            self.pokemon_usage[pokemon] = usage

    def get_all_pokemon_usage(self) -> dict:
        """Get all Pokémon usage"""
        return self.pokemon_usage

    def get_pokemon_usage(self, pokemon: str) -> int:
        """Get Pokémon usage"""
        if pokemon not in self.pokemon_usage:
            logger.warning("Pokémon not found in Pokémon usage, cannot retrieve")
            return 0
        return self.pokemon_usage[pokemon]

    def set_pokemon_partner_usage(
        self, pokemon: str, partner_pokemon: str, usage: int
    ) -> None:
        """Set Pokémon partner usage for specified Pokémon"""
        # Initialize if Pokémon not previously recorded
        if pokemon not in self.pokemon_partner_usage:
            self.pokemon_partner_usage[pokemon] = {}
        if partner_pokemon in self.pokemon_partner_usage[pokemon]:
            logger.warning(
                f"Partner Pokémon ({partner_pokemon}) already in Pokémon partner usage \
            for {pokemon}, cannot set"
            )
        else:
            self.pokemon_partner_usage[pokemon][partner_pokemon] = usage

    def get_all_pokemon_partner_usage(self) -> dict:
        """Get all Pokémon partner usage for specified Pokémon"""
        return self.pokemon_partner_usage

    def get_pokemon_partner_usage(self, pokemon: str, partner_pokemon: str) -> int:
        """Get Pokémon partner usage for specified Pokémon"""
        if pokemon not in self.pokemon_partner_usage:
            logger.warning(
                f"Pokémon ({pokemon}) not in Pokémon partner usage, cannot retrieve"
            )
            return 0
        if partner_pokemon not in self.pokemon_partner_usage[pokemon]:
            logger.warning(
                f"Partner Pokémon ({partner_pokemon}) not found in Pokémon partner usage \
            for {pokemon}, cannot retrieve"
            )
            return 0
        return self.pokemon_partner_usage[pokemon][partner_pokemon]

    def set_pokemon_average_rating_usage(self, pokemon: str, rating: int) -> None:
        """Set Pokémon average rating normalized by usage"""
        if pokemon in self.pokemon_average_rating_usage:
            logger.warning(
                f"Pokémon ({pokemon}) already in Pokémon average rating usage, cannot set"
            )
        else:
            self.pokemon_average_rating_usage[pokemon] = rating

    def get_all_pokemon_average_rating_usage(self) -> dict:
        """Get all Pokémon average rating normalized by usage"""
        return self.pokemon_average_rating_usage

    def get_pokemon_average_rating_usage(self, pokemon: str) -> int:
        """Get Pokémon average rating normalized by usage"""
        if pokemon not in self.pokemon_average_rating_usage:
            logger.warning(
                "Pokémon not found in Pokémon average rating usage, cannot retrieve"
            )
            return 0
        return self.pokemon_average_rating_usage[pokemon]

    def make_model(self) -> dict:
        """Generate model for database as dictionary"""
        return {
            "Date": self.get_date(),
            "FormatId": self.get_format_id(),
            "PokemonUsage": self.get_all_pokemon_usage(),
            "PokemonPartnerUsage": self.get_all_pokemon_partner_usage(),
            "PokemonAverageRatingUsage": self.get_all_pokemon_average_rating_usage(),
        }
