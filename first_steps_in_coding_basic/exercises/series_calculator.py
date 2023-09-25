from math import floor
name_of_series = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
timing_of_episode_without_advertisements = float(input())
time_per_special_episode = number_of_seasons * 10
advertisements = timing_of_episode_without_advertisements * 0.2
total_time_to_watch = (timing_of_episode_without_advertisements + advertisements) \
                      * number_of_episodes \
                      * number_of_seasons + time_per_special_episode
print(f"Total time needed to watch the {name_of_series} series is {floor(total_time_to_watch)} minutes.")
