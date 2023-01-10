class PlayerDataKeys:

    def __init__(self, data):
        self.data = data
        self.matchesPlayed = data["matchesPlayed"]["value"]
        self.matchesWon = data["matchesWon"]["value"]
        self.matchesLost = data["matchesLost"]["value"]
        self.matchesTied = data["matchesTied"]["value"]
        self.matchesWinPct = data["matchesWinPct"]["value"]
        self.matchesDuration = data["matchesDuration"]["value"]
        self.timePlayed = data["timePlayed"]["value"]
        self.roundsPlayed = data["roundsPlayed"]["value"]
        self.roundsWon = data["roundsWon"]["value"]
        self.roundsLost = data["roundsLost"]["value"]
        self.roundsWinPct = data["roundsWinPct"]["value"]
        self.roundsDuration = data["roundsDuration"]["value"]
        self.score = data["score"]["value"]
        self.scorePerMatch = data["scorePerMatch"]["value"]
        self.scorePerRound = data["scorePerRound"]["value"]
        self.kills = data["kills"]["value"]
        self.killsPerRound = data["killsPerRound"]["value"]
        self.killsPerMatch = data["killsPerMatch"]["value"]
        self.deaths = data["deaths"]["value"]
        self.deathsPerRound = data["deathsPerRound"]["value"]
        self.deathsPerMatch = data["deathsPerMatch"]["value"]
        self.assists = data["assists"]["value"]
        self.assistsPerRound = data["assistsPerRound"]["value"]
        self.assistsPerMatch = data["assistsPerMatch"]["value"]
        self.kDRatio = data["kDRatio"]["value"]
        self.kDARatio = data["kDARatio"]["value"]
        self.kADRatio = data["kADRatio"]["value"]
        self.damage = data["damage"]["value"]
        self.damagePerRound = data["damagePerRound"]["value"]
        self.damagePerMatch = data["damagePerMatch"]["value"]
        self.damagePerMinute = data["damagePerMinute"]["value"]
        self.damageReceived = data["damageReceived"]["value"]
        self.headshots = data["headshots"]["value"]
        self.headshotsPerRound = data["headshotsPerRound"]["value"]
        self.headshotsPercentage = data["headshotsPercentage"]["value"]
        self.grenadeCasts = data["grenadeCasts"]["value"]
        self.grenadeCastsPerRound = data["grenadeCastsPerRound"]["value"]
        self.grenadeCastsPerMatch = data["grenadeCastsPerMatch"]["value"]
        self.ability1Casts = data["ability1Casts"]["value"]
        self.ability1CastsPerRound = self.get_dict_path("ability1CastsPerRound")
        self.ability1CastsPerMatch = self.get_dict_path("ability1CastsPerMatch")
        self.ability2Casts = self.get_dict_path("ability2Casts")
        self.ability2CastsPerRound = self.get_dict_path("ability2CastsPerRound")
        self.ability2CastsPerMatch = self.get_dict_path("ability2CastsPerMatch")
        self.ultimateCasts = self.get_dict_path("ultimateCasts")
        self.ultimateCastsPerRound = self.get_dict_path("ultimateCastsPerRound")
        self.ultimateCastsPerMatch = self.get_dict_path("ultimateCastsPerMatch")
        self.dealtHeadshots = self.get_dict_path("dealtHeadshots")
        self.dealtBodyshots = self.get_dict_path("dealtBodyshots")
        self.dealtLegshots = self.get_dict_path("dealtLegshots")
        self.receivedHeadshots = self.get_dict_path("receivedHeadshots")
        self.receivedBodyshots = self.get_dict_path("receivedBodyshots")
        self.receivedLegshots = self.get_dict_path("receivedLegshots")
        self.econRating = self.get_dict_path("econRating")
        self.econRatingPerMatch = self.get_dict_path("econRatingPerMatch")
        self.econRatingPerRound = self.get_dict_path("econRatingPerRound")
        self.suicides = self.get_dict_path("suicides")
        self.firstBloods = self.get_dict_path("firstBloods")
        self.firstBloodsPerMatch = self.get_dict_path("firstBloodsPerMatch")
        self.firstDeaths = self.get_dict_path("firstDeaths")
        self.lastDeaths = self.get_dict_path("lastDeaths")
        self.survived = self.get_dict_path("survived")
        self.traded = self.get_dict_path("traded")
        self.kAST = self.get_dict_path("kAST")
        self.mostKillsInMatch = self.get_dict_path("mostKillsInMatch")
        self.flawless = self.get_dict_path("flawless")
        self.thrifty = self.get_dict_path("thrifty")
        self.aces = self.get_dict_path("aces")
        self.teamAces = self.get_dict_path("teamAces")
        self.clutches = self.get_dict_path("clutches")
        self.clutchesLost = self.get_dict_path("clutchesLost")
        self.clutches1v1 = self.get_dict_path("clutches1v1")
        self.clutches1v2 = self.get_dict_path("clutches1v2")
        self.clutches1v3 = self.get_dict_path("clutches1v3")
        self.clutches1v4 = self.get_dict_path("clutches1v4")
        self.clutches1v5 = self.get_dict_path("clutches1v5")
        self.clutchesLost1v1 = self.get_dict_path("clutchesLost1v1")
        self.clutchesLost1v2 = self.get_dict_path("clutchesLost1v2")
        self.clutchesLost1v3 = self.get_dict_path("clutchesLost1v3")
        self.clutchesLost1v4 = self.get_dict_path("clutchesLost1v4")
        self.clutchesLost1v5 = self.get_dict_path("clutchesLost1v5")
        self.kills1K = self.get_dict_path("kills1K")
        self.kills2K = self.get_dict_path("kills2K")
        self.kills3K = self.get_dict_path("kills3K")
        self.kills4K = self.get_dict_path("kills4K")
        self.kills5K = self.get_dict_path("kills5K")
        self.kills6K = self.get_dict_path("kills6K")
        self.plants = self.get_dict_path("plants")
        self.plantsPerMatch = self.get_dict_path("plantsPerMatch")
        self.plantsPerRound = self.get_dict_path("plantsPerRound")
        self.attackKills = self.get_dict_path("attackKills")
        self.attackDeaths = self.get_dict_path("attackDeaths")
        self.attackKDRatio = self.get_dict_path("attackKDRatio")
        self.attackAssists = self.get_dict_path("attackAssists")
        self.attackRoundsWon = self.get_dict_path("attackRoundsWon")
        self.attackRoundsLost = self.get_dict_path("attackRoundsLost")
        self.attackRoundsWinPct = self.get_dict_path("attackRoundsWinPct")
        self.attackScore = self.get_dict_path("attackScore")
        self.attackDamage = self.get_dict_path("attackDamage")
        self.attackHeadshots = self.get_dict_path("attackHeadshots")
        self.attackTraded = self.get_dict_path("attackTraded")
        self.attackSurvived = self.get_dict_path("attackSurvived")
        self.attackFirstBloods = self.get_dict_path("attackFirstBloods")
        self.attackFirstDeaths = self.get_dict_path("attackFirstDeaths")
        self.attackKAST = self.get_dict_path("attackKAST")
        self.defuses = self.get_dict_path("defuses")
        self.defusesPerMatch = self.get_dict_path("defusesPerMatch")
        self.defusesPerRound = self.get_dict_path("defusesPerRound")
        self.defenseKills = self.get_dict_path("defenseKills")
        self.defenseDeaths = self.get_dict_path("defenseDeaths")
        self.defenseKDRatio = self.get_dict_path("defenseKDRatio")
        self.defenseAssists = self.get_dict_path("defenseAssists")
        self.defenseRoundsWon = self.get_dict_path("defenseRoundsWon")
        self.defenseRoundsLost = self.get_dict_path("defenseRoundsLost")
        self.defenseRoundsWinPct = self.get_dict_path("defenseRoundsWinPct")
        self.defenseScore = self.get_dict_path("defenseScore")
        self.defenseDamage = self.get_dict_path("defenseDamage")
        self.defenseHeadshots = self.get_dict_path("defenseHeadshots")
        self.defenseTraded = self.get_dict_path("defenseTraded")
        self.defenseSurvived = self.get_dict_path("defenseSurvived")
        self.defenseFirstBloods = self.get_dict_path("defenseFirstBloods")
        self.defenseFirstDeaths = self.get_dict_path("defenseFirstDeaths")
        self.defenseKAST = self.get_dict_path("defenseKAST")
        self.rank = self.get_dict_path("rank")
        self.peakRank = self.get_dict_path("peakRank")

    def get_dict_path(self, key):
        return self.data[key]['value']