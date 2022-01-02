""" Models for the storage layer """
import datetime
from typing import List
from constants import TEAM_SIZE, NUM_TEAMS
from base_logger import logger


class PokemonTeamSnapshot:
    """Model for Pokémon Team Snapshots"""

    def __init__(self):
        self.date: datetime.MINYEAR
        self.format_id = ""
        self.team_list = []

    def set_date(self, date: datetime) -> None:
        """Set date"""
        self.date = date

    def get_date(self) -> datetime:
        """Get date"""
        return self.date

    def set_format_id(self, format_id: str) -> None:
        """Set format ID"""
        self.format_id = format_id

    def get_format_id(self) -> str:
        """Get format ID"""
        return self.format_id

    def set_team_list(self, team_list: List[List[str]]) -> None:
        """Set team list"""
        if len(team_list) > NUM_TEAMS:
            logger.warning(
                f"Cannot add team list greater than maximum size of {NUM_TEAMS}"
            )
        else:
            self.team_list = team_list

    def add_team(self, team: List[str]) -> None:
        """Add team to team list"""
        if len(self.team_list) > NUM_TEAMS - 1:
            logger.warning(f"Cannot add team, team list limited to {NUM_TEAMS}")
        else:
            self.team_list.append(team)

    def get_team_list(self) -> List[List[str]]:
        """Get team list"""
        return self.team_list


class PokemonTeam:
    """Model for teams in Pokémon Team Snapshots"""

    def __init__(self):
        self.pokemon_roster = []
        self.rating = 0
        self.replay_upload_date = datetime.MINYEAR

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

    def set_replay_upload_date(self, replay_upload_date: datetime) -> None:
        """Set replay upload date"""
        self.replay_upload_date = replay_upload_date

    def get_replay_upload_date(self) -> datetime:
        """Get replay upload date"""
        return self.replay_upload_date


class PokemonUsageSnapshot:
    """Model for Pokémon Usage Snapshot"""

    def __init__(self):
        self.date = datetime.MINYEAR
        self.format_id = ""
        # {Pokémon -> number of apperances}
        self.pokemon_usage = {}
        # {Pokémon -> {partner -> number of apperances}}
        self.pokemon_partner_usage = {}
        # {Pokémon -> average rating}
        self.pokemon_average_rating_usage = {}

    def set_date(self, date: datetime) -> None:
        """Set date"""
        self.date = date

    def get_date(self) -> datetime:
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

    def get_pokemon_average_rating_usage(self, pokemon: str) -> int:
        """Get Pokémon average rating normalized by usage"""
        if pokemon not in self.pokemon_average_rating_usage:
            logger.warning(
                "Pokémon not found in Pokémon average rating usage, cannot retrieve"
            )
            return 0
        return self.pokemon_average_rating_usage[pokemon]