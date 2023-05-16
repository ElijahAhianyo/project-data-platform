from pynecone import constants, pc

if __name__ == "__main__":
    # pc.init()
    pc.run(env=constants.Env.DEV, loglevel=constants.LogLevel.INFO, port="3000")

