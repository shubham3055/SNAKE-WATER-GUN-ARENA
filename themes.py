class ThemeManager:

    themes = [
        "Cyberpunk",
        "Galaxy",
        "Matrix",
        "Fire",
        "Ice"
    ]

    def show(self):

        print("\n🎨 THEMES")

        for i, theme in enumerate(self.themes):

            print(i+1, theme)