import pynecone as pc

config = pc.Config(
    app_name="okparser_web",
    frontend_packages=[
        "@focus-reactive/react-yaml",
    ],
    env=pc.Env.DEV,
)
