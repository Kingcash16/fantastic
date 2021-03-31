# Joshua Jaja ID:1543343 Zylab 10.15
class Team:
    def __init__(self):
        self.t_n = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def s_team_name(self, team_n):
        self.t_n = team_n

    def s_team_wins(self, team_wins):
        self.team_wins = team_wins

    def s_team_losses(self, team_losses):
        self.team_losses = team_losses


    def get_win_percentage(self):
        percent = self.team_wins / (self.team_wins + self.team_losses)
        return percent


if __name__ == "__main__":

    team = Team()

    t_n = input()
    team_wins = int(input())
    team_losses = int(input())

    team.s_team_name(t_n)
    team.s_team_wins(team_wins)
    team.s_team_losses(team_losses)

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.t_n, 'has a winning average!')
    else:
        print('Team', team.t_n, 'has a losing average.')

