from start_venv import open_venv_shell
  
if __name__ == "__main__":
    open_venv_shell("jupyter nbconvert notebooks/04_presentation.ipynb --to slides --SlidesExporter.reveal_number='c/t' --SlidesExporter.reveal_scroll=True --output-dir presentazione --output presentation & exit")