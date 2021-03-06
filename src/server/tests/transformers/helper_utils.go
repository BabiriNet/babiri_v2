package tests

import "github.com/kelvinkoon/babiri_v2/models"

// Create mock team snapshots
func createMockTeamSnapshots() []models.PokemonTeamsSnapshot {
	return []models.PokemonTeamsSnapshot{
		{
			Date:     "2022-01-01",
			FormatId: "gen8vgc2021series11",
			Teams: []models.Team{
				{
					PokemonRoster:    []string{"a11", "b11", "c11"},
					Rating:           1511,
					ReplayUploadDate: "2022-01-01",
				},
				{
					PokemonRoster:    []string{"a12", "b12", "c12"},
					Rating:           1512,
					ReplayUploadDate: "2022-01-02",
				},
			},
		},
		{
			Date:     "2022-01-02",
			FormatId: "gen8vgc2021series11",
			Teams: []models.Team{
				{
					PokemonRoster:    []string{"a21", "b21", "c21"},
					Rating:           1521,
					ReplayUploadDate: "2022-02-01",
				},
				{
					PokemonRoster:    []string{"a22", "b22", "c22"},
					Rating:           1522,
					ReplayUploadDate: "2022-02-02",
				},
			},
		},
		{
			Date:     "2022-01-03",
			FormatId: "gen8vgc2021series11",
			Teams: []models.Team{
				{
					PokemonRoster:    []string{"a31", "b31", "c31"},
					Rating:           1531,
					ReplayUploadDate: "2022-03-01",
				},
				{
					PokemonRoster:    []string{"a32", "b32", "c32"},
					Rating:           1532,
					ReplayUploadDate: "2022-03-02",
				},
			},
		},
		{
			Date:     "2022-01-04",
			FormatId: "gen8vgc2021series11",
			Teams: []models.Team{
				{
					PokemonRoster:    []string{"a41", "b41", "c41"},
					Rating:           1541,
					ReplayUploadDate: "2022-04-01",
				},
				{
					PokemonRoster:    []string{"a42", "b42", "c42"},
					Rating:           1542,
					ReplayUploadDate: "2022-04-02",
				},
			},
		},
	}
}

// Create mock usage snapshots
func CreateMockUsageSnapshots() []models.PokemonUsageSnapshot {
	mockPokemonUsage := make(map[string]int)
	mockPokemonPartnerUsage := make(map[string]map[string]int)
	mockAvgRatingUsage := make(map[string]int)

	return []models.PokemonUsageSnapshot{
		{
			Date:                      "2022-01-01",
			FormatId:                  "gen8vgc2021series11",
			PokemonUsage:              mockPokemonUsage,
			PokemonPartnerUsage:       mockPokemonPartnerUsage,
			PokemonAverageRatingUsage: mockAvgRatingUsage,
		},
		{
			Date:                      "2022-01-02",
			FormatId:                  "gen8vgc2021series11",
			PokemonUsage:              mockPokemonUsage,
			PokemonPartnerUsage:       mockPokemonPartnerUsage,
			PokemonAverageRatingUsage: mockAvgRatingUsage,
		},
		{
			Date:                      "2022-01-03",
			FormatId:                  "gen8ou",
			PokemonUsage:              mockPokemonUsage,
			PokemonPartnerUsage:       mockPokemonPartnerUsage,
			PokemonAverageRatingUsage: mockAvgRatingUsage,
		},
		{
			Date:                      "2022-01-04",
			FormatId:                  "gen8ou",
			PokemonUsage:              mockPokemonUsage,
			PokemonPartnerUsage:       mockPokemonPartnerUsage,
			PokemonAverageRatingUsage: mockAvgRatingUsage,
		},
	}
}
