class StoryMode:

    def start(self):

        print("\n🌌 STORY MODE")

        chapters = [
            "Village Arena",
            "Forest Kingdom",
            "Ice Castle",
            "Shadow Realm",
            "Dragon Mountain"
        ]

        for i, chapter in enumerate(chapters, start=1):

            print(f"Chapter {i}: {chapter}")

        print("\n🐉 Final Battle Awaits...")