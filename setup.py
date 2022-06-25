import cx_Freeze

arquivo = [cx_Freeze.Executable(
    script="game2.py", icon="imgs/birdicon.ico"
)]


cx_Freeze.setup(
    name="Flappy bird",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["imgs"]}},
    executables=arquivo
)


# python setup.py build (aqui ele vair gerar uma pasta com os arquivos dentro)
# python setup.py bdist_msi (aqui ele gera um instalador de windows)