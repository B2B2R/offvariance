import pandas as pd
from pandas import DataFrame


def filter_games(df: DataFrame) -> DataFrame:
    away_win_games_df = filter_away_win_games(df)
    away_win_games_df['bet_type'] = '2'
    away_win_games_df['odds_open'] = away_win_games_df['odds_open_win2']
    away_win_games_df['odds_close'] = away_win_games_df['odds_close_win2']
    away_win_games_df['udi'] = away_win_games_df['udi_win2']

    home_win_games_df = filter_home_win_games(df)
    home_win_games_df['bet_type'] = '1'
    home_win_games_df['odds_open'] = home_win_games_df['odds_open_win1']
    home_win_games_df['odds_close'] = home_win_games_df['odds_close_win1']
    home_win_games_df['udi'] = home_win_games_df['udi_win1']

    total_under_games_df = filter_total_under_games(df)
    total_under_games_df['bet_type'] = 'U2.5'
    total_under_games_df['odds_open'] = total_under_games_df['odds_open_tm25']
    total_under_games_df['odds_close'] = total_under_games_df['odds_close_tm25']
    total_under_games_df['udi'] = total_under_games_df['udi_tm25']

    total_over_games_df = filter_total_over_games(df)
    total_over_games_df['bet_type'] = 'O2.5'
    total_over_games_df['odds_open'] = total_over_games_df['odds_open_tb25']
    total_over_games_df['odds_close'] = total_over_games_df['odds_close_tb25']
    total_over_games_df['udi'] = total_over_games_df['udi_tb25']

    result_df = pd.concat([away_win_games_df, total_under_games_df, total_over_games_df, home_win_games_df])
    result_df = result_df.sort_values(by=['date_match'])

    return result_df[
        [
            'id',
            'date_match',
            'country_name',
            'team_1_name',
            'team_2_name',
            'bet_type',
            'odds_open',
            'odds_close',
            'odds_min',
            'udi'
        ]
    ]


def filter_games_segment(df: DataFrame, conditions, open_column, expected_udi_value):
    result = df.loc[conditions].copy()
    result['odds_min'] = result[open_column] / (expected_udi_value + 1)

    return result


def filter_total_under_games(df: DataFrame) -> DataFrame:
    return pd.concat([
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tm25'] >= 1.9) & (df['odds_open_tm25'] <= 1.97)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tm25'] >= 1.971) & (df['odds_open_tm25'] <= 2.03)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tm25'] >= 2.031) & (df['odds_open_tm25'] <= 2.1)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tm25'] >= 2.101) & (df['odds_open_tm25'] <= 2.2)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tm25'] >= 2.201) & (df['odds_open_tm25'] <= 2.32)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tm25'] >= 2.321) & (df['odds_open_tm25'] <= 2.47)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tm25'] >= 2.471) & (df['odds_open_tm25'] <= 2.65)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tm25'] >= 2.651) & (df['odds_open_tm25'] <= 3.50)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tm25'] >= 1.74) & (df['odds_open_tm25'] <= 1.77)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tm25'] >= 1.771) & (df['odds_open_tm25'] <= 1.81)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tm25'] >= 1.811) & (df['odds_open_tm25'] <= 1.85)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tm25'] >= 1.851) & (df['odds_open_tm25'] <= 1.9)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tm25'] >= 1.901) & (df['odds_open_tm25'] <= 1.95)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tm25'] >= 1.951) & (df['odds_open_tm25'] <= 2)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tm25'] >= 2.001) & (df['odds_open_tm25'] <= 2.06)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tm25'] >= 2.061) & (df['odds_open_tm25'] <= 2.16)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tm25'] >= 2.161) & (df['odds_open_tm25'] <= 2.3)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tm25'] >= 2.301) & (df['odds_open_tm25'] <= 3.5)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tm25'] >= 1.75) & (df['odds_open_tm25'] <= 1.81)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tm25'] >= 1.811) & (df['odds_open_tm25'] <= 1.88)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tm25'] >= 1.881) & (df['odds_open_tm25'] <= 1.96)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tm25'] >= 1.961) & (df['odds_open_tm25'] <= 2.03)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tm25'] >= 2.031) & (df['odds_open_tm25'] <= 2.13)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tm25'] >= 2.131) & (df['odds_open_tm25'] <= 2.25)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tm25'] >= 2.251) & (df['odds_open_tm25'] <= 2.44)
                )
            ),
            'odds_open_tm25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tm25'] >= 2.441) & (df['odds_open_tm25'] <= 3.5)
                )
            ),
            'odds_open_tm25',
            0.05
        )
    ])


def filter_total_over_games(df: DataFrame) -> DataFrame:
    return pd.concat([
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tb25'] >= 1.6) & (df['odds_open_tb25'] <= 1.66)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tb25'] >= 1.661) & (df['odds_open_tb25'] <= 1.74)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tb25'] >= 1.741) & (df['odds_open_tb25'] <= 1.82)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tb25'] >= 1.821) & (df['odds_open_tb25'] <= 1.91)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tb25'] >= 1.911) & (df['odds_open_tb25'] <= 2)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tb25'] >= 2.001) & (df['odds_open_tb25'] <= 2.11)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tb25'] >= 2.111) & (df['odds_open_tb25'] <= 2.27)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.3) & (df['odds_open_win1'] <= 1.85) &
                        (df['odds_open_tb25'] >= 2.271) & (df['odds_open_tb25'] <= 3)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 1.6) & (df['odds_open_tb25'] <= 1.69)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 1.691) & (df['odds_open_tb25'] <= 1.77)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 1.771) & (df['odds_open_tb25'] <= 1.83)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 1.831) & (df['odds_open_tb25'] <= 1.89)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 1.891) & (df['odds_open_tb25'] <= 1.95)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 1.951) & (df['odds_open_tb25'] <= 2)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 2.001) & (df['odds_open_tb25'] <= 2.04)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 2.041) & (df['odds_open_tb25'] <= 2.09)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 2.091) & (df['odds_open_tb25'] <= 2.14)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 2.141) & (df['odds_open_tb25'] <= 2.20)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 2.201) & (df['odds_open_tb25'] <= 2.26)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 2.261) & (df['odds_open_tb25'] <= 2.33)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 2.331) & (df['odds_open_tb25'] <= 2.41)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 2.411) & (df['odds_open_tb25'] <= 2.52)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 2.521) & (df['odds_open_tb25'] <= 2.65)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.851) & (df['odds_open_win1'] <= 2.8) &
                        (df['odds_open_tb25'] >= 2.651) & (df['odds_open_tb25'] <= 3)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tb25'] >= 1.711) & (df['odds_open_tb25'] <= 1.81)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tb25'] >= 1.811) & (df['odds_open_tb25'] <= 1.91)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tb25'] >= 1.911) & (df['odds_open_tb25'] <= 2.01)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tb25'] >= 2.011) & (df['odds_open_tb25'] <= 2.11)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tb25'] >= 2.111) & (df['odds_open_tb25'] <= 2.25)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tb25'] >= 2.251) & (df['odds_open_tb25'] <= 2.47)
                )
            ),
            'odds_open_tb25',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 2.801) & (df['odds_open_win1'] <= 10) &
                        (df['odds_open_tb25'] >= 2.471) & (df['odds_open_tb25'] <= 3)
                )
            ),
            'odds_open_tb25',
            0.05
        )
    ])


def filter_away_win_games(df: DataFrame) -> DataFrame:
    return pd.concat([
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win2'] >= 1.8) & (df['odds_open_win2'] <= 2.7) &
                        (df['odds_open_tb25'] >= 2.0) & (df['odds_open_tb25'] <= 2.5)
                )
            ),
            'odds_open_win2',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win2'] >= 1.8) & (df['odds_open_win2'] <= 2.7) &
                        (df['odds_open_tb25'] >= 1.6) & (df['odds_open_tb25'] <= 2)
                )
            ),
            'odds_open_win2',
            0.07
        )
    ])


def filter_home_win_games(df: DataFrame) -> DataFrame:
    return pd.concat([
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.2) & (df['odds_open_win1'] <= 4.0) &
                        (df['odds_open_tb25'] >= 2.0) & (df['odds_open_tb25'] <= 2.5)
                )
            ),
            'odds_open_win1',
            0.05
        ),
        filter_games_segment(
            df,
            (df['team1_home_classic_minutes'] >= 90 * 3) & (df['team2_away_classic_minutes'] >= 90 * 3) &
            (
                (
                        (df['odds_open_win1'] >= 1.2) & (df['odds_open_win1'] <= 4.0) &
                        (df['odds_open_tb25'] >= 1.1) & (df['odds_open_tb25'] <= 2)
                )
            ),
            'odds_open_win1',
            0.07
        )
    ])
