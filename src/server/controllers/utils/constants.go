package utils

// PS! terms
// gen8vgc2021series11 is a legacy format primarily for tests
var Formats []string = []string{"gen8vgc2021series11", "gen8vgc2022", "gen8doublesou", "gen8ou", "gen8nationaldexag", "gen8nationaldex", "gen8anythinggoes"}

// Usage Pipeline Type Enums
type UsageType int

const (
	Usage        UsageType = iota
	PartnerUsage UsageType = iota
	RatingUsage  UsageType = iota
)

// Function for converting usage type enum to string
func (utype UsageType) String() string {
	return [...]string{"Usage", "PartnerUsage", "RatingUsage"}[utype]
}

// DB terms
var DbClusterName string = "babiri-dev-cluster"
var PokemonTeamsSnapshotsCollection string = "pokemon_teams_snapshots"
var PokemonUsageSnapshotsCollection string = "pokemon_usage_snapshots"
var DbEnvPrefix string = Env + "_"
var PokemonTeamSnapshotsCollectionName = DbEnvPrefix + PokemonTeamsSnapshotsCollection
var PokemonUsageSnapshotsCollectionName = DbEnvPrefix + PokemonUsageSnapshotsCollection
var UsageLimit int = 10
