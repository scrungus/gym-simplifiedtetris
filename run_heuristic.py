import numpy as np

from gym_simplifiedtetris.agents import DellacherieAgent
from gym_simplifiedtetris.envs import SimplifiedTetrisBinaryEnv as Tetris


def main():
    num_episodes = 10
    ep_returns = np.zeros(num_episodes)

    agent = DellacherieAgent()
    env = Tetris(
        grid_dims=(6, 10),
        piece_size=4,
    )
    obs = env.reset()

    episode_num = 0
    while episode_num < num_episodes:
        env.render()

        heuristic_scores = env._engine._get_dellacherie_scores()

        action = agent.predict(heuristic_scores)
        obs, rwd, done, info = env.step(action)
        ep_returns[episode_num] += info["num_rows_cleared"]

        if done:
            print(f"Episode {episode_num + 1} has terminated.")
            episode_num += 1
            obs = env.reset()

    env.close()

    print(
        f"\nScore obtained from averaging over {num_episodes} "
        f"games: {np.mean(ep_returns):.1f} +/- {np.std(ep_returns):.1f}"
    )


if __name__ == "__main__":
    main()
